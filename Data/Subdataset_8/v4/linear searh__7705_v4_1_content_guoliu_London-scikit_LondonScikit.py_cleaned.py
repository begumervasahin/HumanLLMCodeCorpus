import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
x_train = np.loadtxt(open("train.csv", "rb"), delimiter=",", skiprows=0)
y_train = np.loadtxt(open("trainLabels.csv", "rb"), delimiter=",", skiprows=0)
x_test = np.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=0)
tuned_parameters = {'C': 10.**np.arange(-5, 5)}
classifier = LinearSVC()
clf = GridSearchCV(classifier, tuned_parameters, cv=5, verbose=3)
clf.fit(x_train, y_train)
for params, mean_score, scores in clf.grid_scores_:
    print("%0.3f (+/-%0.03f) for %r" % (mean_score, scores.std() * 2, params))
predictions = clf.predict(x_test)
output = np.vstack((np.arange(len(predictions)).astype(int) + 1, predictions.astype(int))).T
np.savetxt("LinearSVMresult.csv", output, header="Id,Solution", fmt="%d", comments="", delimiter=",")