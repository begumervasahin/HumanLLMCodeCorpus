from sklearn.metrics import confusion_matrix, accuracy_score, average_precision_score, roc_auc_score
from sklearn.naive_bayes import MultinomialNB
def fonk1(b5, b6, b7, b8, b9):
    """
    Trains and evaluates a Multinomial Naive Bayes b1.
    Prints the confusion matrix, accuracy score, ROC AUC score, and average precision score.
    Predicts the class class1 a given input vector.
    Parameters:
    b5 (array-like): Training features
    b6 (array-like): Training labels
    b7 (array-like): Testing features
    b8 (array-like): Testing labels
    b9 (array-like): Vector to predict class class2
    Returns:
    str: "Positive" if the b3 class2 b9 is 1, otherwise "Negative"
    """
    print("Multinomial Naive Bayes Model Evaluation")
    b1 = MultinomialNB()
    b1.fit(b5, b6)
    b2 = b1.predict(b7)
    print("Confusion Matrix:")
    print(confusion_matrix(b8, b2))
    print("Accuracy Score:", accuracy_score(b8, b2))
    print("ROC AUC Score:", roc_auc_score(b8, b2))
    print("Average Precision Score:", average_precision_score(b8, b2))
    b3 = b1.predict(b9)
    return "Positive" if b3 = = [1] else "Negative"
if b4 = = "__main__":
    b5 = [[0, 1, 2], [1, 0, 3], [2, 1, 0]]
    b6 = [0, 1, 0]
    b7 = [[0, 1, 2], [2, 0, 1]]
    b8 = [0, 1]
    b9 = [[1, 0, 2]]
    b10 = fonk1(b5, b6, b7, b8, b9)
    print("Prediction class2 input vector:", b10)