import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
b1 = np.loadtxt("train.csv", delimiter=",", skiprows=0)
b2 = np.loadtxt("trainLabels.csv", delimiter=",", skiprows=0)
b3 = np.loadtxt("test.csv", delimiter=",", skiprows=0)
b4 = {'C': 10. ** np.arange(-5, 5)}
x_train_split, x_val, y_train_split, b5 = train_test_split(b1, b2, test_size=0.2, random_state=42)
b6 = LinearSVC()
b7 = GridSearchCV(b6, b4, cv=5, verbose=3)
b7.fit(x_train_split, y_train_split)
print("Best parameters found:", b7.best_params_)
print("\nGrid scores:")
for params, mean_score, scores in b7.cv_results_:
    print(f"{mean_score:.3f} (+/- {scores.std() * 2:.03f}) for {params}")
b8 = LinearSVC(C=b7.best_params_['C'])
b8.fit(b1, b2)
b9 = b8.predict(b3)
b10 = np.vstack((np.arange(1, len(b9) + 1), b9)).T
np.savetxt("LinearSVMresult.csv", b10, b11 = "Id,Solution", fmt="%d", comments="", delimiter=",")