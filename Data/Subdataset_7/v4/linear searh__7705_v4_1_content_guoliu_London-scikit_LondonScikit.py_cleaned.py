import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
b1 = np.loadtxt(open("train.csv", "rb"), delimiter=",", skiprows=0)
b2 = np.loadtxt(open("trainLabels.csv", "rb"), delimiter=",", skiprows=0)
b3 = np.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=0)
b4 = {'C': 10.**np.arange(-5, 5)}
b5 = LinearSVC()
b6 = GridSearchCV(b5, b4, cv=5, verbose=3)
b6.fit(b1, b2)
for params, mean_score, scores in b6.grid_scores_:
    print("%0.3f (+/-%0.03f) for %r" % (mean_score, scores.std() * 2, params))
b7 = b6.predict(b3)
b8 = np.vstack((np.arange(len(b7)).astype(int) + 1, b7.astype(int))).T
np.savetxt("LinearSVMresult.csv", b8, b9 = "Id,Solution", fmt="%d", comments="", delimiter=",")