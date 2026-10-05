from sklearn.metrics import confusion_matrix, accuracy_score, average_precision_score, roc_auc_score
from sklearn.naive_bayes import MultinomialNB
def MultinomialNaiveBayes(x_train_vectorized, y_train, x_test_vectorized, y_test, new_data_vectorized):
    print("Multinomial Naive Bayes")
    mnb = MultinomialNB()
    mnb.fit(x_train_vectorized, y_train)
    y_pred_class = mnb.predict(x_test_vectorized)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred_class))
    print('Accuracy Score:', accuracy_score(y_test, y_pred_class))
    print('ROC and AUC:', roc_auc_score(y_test, y_pred_class))
    print('Average Precision Score:', average_precision_score(y_test, y_pred_class))
    prediction = "Positive" if mnb.predict(new_data_vectorized) == [1] else "Negative"
    return prediction
