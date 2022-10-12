import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def get_heart_train_test(heart_data):
    X = heart_data.drop('target', axis=1)  # delete target
    y = heart_data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
    return (X_train, X_test, y_train, y_test)

def get_lr_classifier(X_train, y_train):
    # train model
    log_model = LogisticRegression()
    log_model.fit(X_train, y_train)
    return log_model

def get_nb_classifier(X_train, y_train):
    # train model
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)
    return nb_model

def get_predictions(trained_model, X_test):
    # predictions
    predictions = trained_model.predict(X_test)  # predicted y-s
    return predictions

def print_performance_results(y_test, predictions):
    # performance evaluation
    # classification report
    print('Classification Report:\n', classification_report(y_test, predictions))

    # confusion matrix (true positive, false positive, true negative, false negative)
    print('Confusion Matrix:\n', confusion_matrix(y_test, predictions))