import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
def fonk1(b2):
    return np.loadtxt(open(b2, "rb"), b1 = ",", skiprows=0)
def fonk2(b11, b2 = "LinearSVMresult.csv"):
    b3 = np.vstack((np.arange(1, len(b11) + 1), b11)).T
    np.savetxt(b2, b3, b4 = "Id,Solution", fmt="%d", comments="", b1=",")
b5 = fonk1("train.csv")
b6 = fonk1("trainLabels.csv")
b7 = fonk1("test.csv")
b8 = {'C': 10.**np.arange(-5, 5)}
b9 = LinearSVC()
b10 = GridSearchCV(b9, b8, cv=5, verbose=3)
b10.fit(b5, b6)
for params, mean_score, scores in b10.cv_results_.items():
    print("%0.3f (+/-%0.03f) for %r" % (mean_score.mean(), mean_score.std() * 2, params))
b11 = b10.predict(b7)
fonk2(b11)