import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
x_train = np.loadtxt("train.csv", delimiter=",", skiprows=0)
y_train = np.loadtxt("trainLabels.csv", delimiter=",", skiprows=0)
x_test = np.loadtxt("test.csv", delimiter=",", skiprows=0)
tuned_parameters = {'C': 10. ** np.arange(-5, 5)}
x_train_split, x_val, y_train_split, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)
classifier = LinearSVC()
grid_search = GridSearchCV(classifier, tuned_parameters, cv=5, verbose=3)
grid_search.fit(x_train_split, y_train_split)
print("Best parameters found:", grid_search.best_params_)
print("\nGrid scores:")
for params, mean_score, scores in grid_search.cv_results_:
    print(f"{mean_score:.3f} (+/- {scores.std() * 2:.03f}) for {params}")
best_classifier = LinearSVC(C=grid_search.best_params_['C'])
best_classifier.fit(x_train, y_train)
predictions = best_classifier.predict(x_test)
output = np.vstack((np.arange(1, len(predictions) + 1), predictions)).T
np.savetxt("LinearSVMresult.csv", output, header="Id,Solution", fmt="%d", comments="", delimiter=",")