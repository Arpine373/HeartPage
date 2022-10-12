import pandas as pd 
heart_data = pd.read_csv('heart.csv')

#split into train data and test data
from sklearn.model_selection import train_test_split
X = heart_data.drop('target', axis=1) #delete target
y = heart_data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
print('X_train:\n', X_train.head())
print('y_train:\n', y_train.head())

#train model
from sklearn.naive_bayes import GaussianNB
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

#predictions
predictions = nb_model.predict(X_test) #predicted y-s

#performance evaluation
#classification report
from sklearn.metrics import classification_report
print('Classification Report:\n', classification_report(y_test,predictions))

#confusion matrix (true positive, false positive, true negative, false negative)
from sklearn.metrics import confusion_matrix
print('Confusion Matrix:\n', confusion_matrix(y_test, predictions))