import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
def load_data(file_path):
    return np.loadtxt(open(file_path, "rb"), delimiter=",", skiprows=0)
def save_predictions(predictions, file_path="LinearSVMresult.csv"):
    output = np.vstack((np.arange(1, len(predictions) + 1), predictions)).T
    np.savetxt(file_path, output, header="Id,Solution", fmt="%d", comments="", delimiter=",")
x_train = load_data("train.csv")
y_train = load_data("trainLabels.csv")
x_test = load_data("test.csv")
tuned_parameters = {'C': 10.**np.arange(-5, 5)}
classifier = LinearSVC()
clf = GridSearchCV(classifier, tuned_parameters, cv=5, verbose=3)
clf.fit(x_train, y_train)
for params, mean_score, scores in clf.cv_results_.items():
    print("%0.3f (+/-%0.03f) for %r" % (mean_score.mean(), mean_score.std() * 2, params))
predictions = clf.predict(x_test)
save_predictions(predictions)