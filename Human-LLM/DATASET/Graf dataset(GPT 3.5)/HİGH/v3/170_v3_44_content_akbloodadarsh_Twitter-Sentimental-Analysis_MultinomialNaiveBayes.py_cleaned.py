from sklearn.metrics import confusion_matrix, accuracy_score, average_precision_score, roc_auc_score
from sklearn.naive_bayes import MultinomialNB
def fonk1(x_train_vectorized, y_train, x_test_vectorized, y_test, new_data_vectorized):
    print("Multinomial Naive Bayes")
    b1 = MultinomialNB()
    b1.fit(x_train_vectorized, y_train)
    b2 = b1.predict(x_test_vectorized)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, b2))
    print('Accuracy Score:', accuracy_score(y_test, b2))
    print('ROC and AUC:', roc_auc_score(y_test, b2))
    print('Average Precision Score:', average_precision_score(y_test, b2))
    b3 = "Positive" if b1.predict(new_data_vectorized) == [1] else "Negative"
    return b3
