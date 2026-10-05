from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import naive_bayes
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score
def fonk1(x_train_vft, y_train, x_test_vft, y_test, vec):
    print("Multinomial Naive Bayes")
    b1 = naive_bayes.MultinomialNB()
    b1.fit(x_train_vft, y_train)
    b2 = b1.predict(x_test_vft)
    print("Confusion Matrix")
    print(confusion_matrix(y_test, b2))
    print('Accuracy Score :', accuracy_score(y_test, b2))
    print('ROC(Receiver Operating Characteristic) and AUC(Area Under Curve)', roc_auc_score(y_test, b2))
    print('Average Precision Score:', average_precision_score(y_test, b2))
    if b1.predict(vec) == [1]:
        return "Positive"
    else:
        return "Negative"