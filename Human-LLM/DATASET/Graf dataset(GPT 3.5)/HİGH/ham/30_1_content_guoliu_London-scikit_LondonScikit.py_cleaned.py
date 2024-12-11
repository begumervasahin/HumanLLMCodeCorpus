import numpy as np
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
b1 = np.loadtxt(open("train.csv","rb"), delimiter=",", skiprows=0)
b2 = np.loadtxt(open("trainLabels.csv","rb"), delimiter=",", skiprows=0)
b3 = np.loadtxt(open("test.csv","rb"), delimiter=",", skiprows=0)
b4 = {'C': 10.**np.arange(-5,5)}
b5 = GridSearchCV(LinearSVC(), b4, cv=5,verbose=3)
b5.fit(b1, b2)
for params, mean_score, scores in b5.grid_scores_:
    print("%0.3f (+/-%0.03f) for %r" % (mean_score, scores.std() * 2, params))
b6 = b5.predict(b3)
b7 = np.vstack((np.arange(len(b6)).astype(int)+1, b6.astype(int))).T
np.savetxt("LinearSVMresult.csv", b7, b8 = "Id,Solution", fmt="%d", comments="", delimiter=",")