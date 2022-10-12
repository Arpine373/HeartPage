import clustering
from classification import get_heart_train_test, \
    get_lr_classifier, get_nb_classifier, \
    get_predictions, print_performance_results

#generate clusters
clusters = clustering.get_clusters(clusters_number = 5)

#for each cluster solve classification task
for i in range(len(clusters)):
    #generate train and test data
    X_train, X_test, y_train, y_test = get_heart_train_test(clusters[i])

    #train models
    log_model = get_lr_classifier(X_train, y_train)
    nb_model = get_nb_classifier(X_train, y_train)

    #make models predictions
    log_predictions = get_predictions(log_model, X_test)
    nb_predictions = get_predictions(nb_model, X_test)

    #predictions performance assessment
    print('Performance results for cluster i=',i+1)
    print('Logistic Regression results:')
    print_performance_results(y_test, log_predictions)
    print('Naive Bayes results:')
    print_performance_results(y_test, nb_predictions)
    print()