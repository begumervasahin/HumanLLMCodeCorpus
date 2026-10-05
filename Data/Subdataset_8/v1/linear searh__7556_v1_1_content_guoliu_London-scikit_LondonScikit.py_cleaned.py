import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
x_train = np.loadtxt(open("train.csv", "rb"), delimiter=",", skiprows=0)
y_train = np.loadtxt(open("trainLabels.csv", "rb"), delimiter=",", skiprows=0)
x_test = np.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=0)
tuned_parameters = {'C': 10.**np.arange(-5, 5)}
x_train_split, x_val, y_train_split, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)
clf = LinearSVC()
grid_search = GridSearchCV(clf, tuned_parameters, cv=5, verbose=3)
grid_search.fit(x_train_split, y_train_split)
print("Best parameters found:")
print(grid_search.best_params_)
print("\nGrid scores:")
for params, mean_score, scores in grid_search.grid_scores_:
    print("%0.3f (+/-%0.03f) for %r" % (mean_score, scores.std() * 2, params))
best_clf = LinearSVC(C=grid_search.best_params_['C'])
best_clf.fit(x_train, y_train)
predictions = best_clf.predict(x_test)
out = np.vstack((np.arange(len(predictions)).astype(int) + 1, predictions.astype(int))).T
np.savetxt("LinearSVMresult.csv", out, header="Id,Solution", fmt="%d", comments="", delimiter=",")