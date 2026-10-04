from sklearn.metrics import confusion_matrix, accuracy_score, average_precision_score, roc_auc_score
from sklearn import naive_bayes
def fonk1(b5, b6, b7, b8, b9):
    """
    This function trains and evaluates a Multinomial Naive Bayes model.
    It prints the confusion matrix, accuracy score, ROC AUC score, and average precision score.
    It also predicts the class class1 a given input vector.
    Parameters:
    b5: Training features
    b6: Training labels
    b7: Testing features
    b8: Testing labels
    b9: Vector to predict class class2
    Returns:
    "Positive" if the b3 class2 b9 is 1, otherwise "Negative"
    """
    print("Multinomial Naive Bayes")
    b1 = naive_bayes.MultinomialNB()
    b1.fit(b5, b6)
    b2 = b1.predict(b7)
    print("Confusion Matrix")
    print(confusion_matrix(b8, b2))
    print('Accuracy Score:', accuracy_score(b8, b2))
    print('ROC (Receiver Operating Characteristic) and AUC (Area Under Curve):', roc_auc_score(b8, b2))
    print('Average Precision Score:', average_precision_score(b8, b2))
    b3 = b1.predict(b9)
    if b3 = = [1]:
        return "Positive"
    else:
        return "Negative"
if b4 = = "__main__":
    b5 = [[0, 1, 2], [1, 0, 3], [2, 1, 0]]
    b6 = [0, 1, 0]
    b7 = [[0, 1, 2], [2, 0, 1]]
    b8 = [0, 1]
    b9 = [[1, 0, 2]]
    b10 = fonk1(b5, b6, b7, b8, b9)
    print("Prediction class2 input vector:", b10)