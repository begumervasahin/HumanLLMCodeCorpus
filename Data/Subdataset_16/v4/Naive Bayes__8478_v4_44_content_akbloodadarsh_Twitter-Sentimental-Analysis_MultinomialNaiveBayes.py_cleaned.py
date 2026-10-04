from sklearn.metrics import confusion_matrix, accuracy_score, average_precision_score, roc_auc_score
from sklearn.naive_bayes import MultinomialNB
def fonk1(x_train_vft, y_train, x_test_vft, y_test, vec):
    """
    This function trains and evaluates a Multinomial Naive Bayes model.
    Parameters:
    x_train_vft : array-like, shape (n_samples, n_features)
        Training vectors, where n_samples is the number of samples and
        n_features is the number of features.
    y_train : array-like, shape (n_samples,)
        Target values for the training set.
    x_test_vft : array-like, shape (n_samples, n_features)
        Test vectors, where n_samples is the number of samples and
        n_features is the number of features.
    y_test : array-like, shape (n_samples,)
        True labels for the test set.
    vec : array-like, shape (1, n_features)
        A single vector to predict the class class1.
    Returns:
    str : "Positive" or "Negative"
        The b3 for the provided vector `vec`.
    """
    print("Multinomial Naive Bayes")
    b1 = MultinomialNB()
    b1.fit(x_train_vft, y_train)
    b2 = b1.predict(x_test_vft)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, b2))
    print('Accuracy Score:', accuracy_score(y_test, b2))
    print('ROC (Receiver Operating Characteristic) and AUC (Area Under Curve):', roc_auc_score(y_test, b2))
    print('Average Precision Score:', average_precision_score(y_test, b2))
    b3 = b1.predict(vec)
    return "Positive" if b3 = = [1] else "Negative"
