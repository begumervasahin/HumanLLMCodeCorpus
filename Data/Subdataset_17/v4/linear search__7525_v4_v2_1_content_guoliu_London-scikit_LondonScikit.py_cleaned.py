import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
x_train = np.loadtxt("train.csv", delimiter=",", skiprows=0)
y_train = np.loadtxt("trainLabels.csv", delimiter=",", skiprows=0)
x_test = np.loadtxt("test.csv", delimiter=",", skiprows=0)
param_grid = {'C': 10.0 ** np.arange(-5, 5)}
x_train_split, x_val, y_train_split, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)
linear_svc = LinearSVC()
grid_search = GridSearchCV(estimator=linear_svc, param_grid=param_grid, cv=5, verbose=3)
grid_search.fit(x_train_split, y_train_split)
print("Best parameters found:")
print(grid_search.best_params_)
print("\nGrid scores:")
for mean_score, params in zip(grid_search.cv_results_['mean_test_score'], grid_search.cv_results_['params']):
    print(f"{mean_score:.3f} for {params}")
best_svc = LinearSVC(C=grid_search.best_params_['C'])
best_svc.fit(x_train, y_train)
test_predictions = best_svc.predict(x_test)
output = np.vstack((np.arange(len(test_predictions)).astype(int) + 1, test_predictions.astype(int))).T
np.savetxt("LinearSVMresult.csv", output, header="Id,Solution", fmt="%d", comments="", delimiter=",")
print("Predictions saved to 'LinearSVMresult.csv'.")