import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
def fonk1(b8, b9, b10):
    b1 = np.loadtxt(b8, delimiter=",", skiprows=0)
    b2 = np.loadtxt(b9, delimiter=",", skiprows=0)
    b3 = np.loadtxt(b10, delimiter=",", skiprows=0)
    return b1, b2, b3
def fonk2(b1, b2, b12):
    b4 = LinearSVC()
    b5 = GridSearchCV(estimator=b4, b12=b12, cv=5, verbose=3)
    b5.fit(b1, b2)
    return b5
def fonk3(b5):
    print("Best parameters found:")
    print(b5.best_params_)
    print("\nGrid scores:")
    for mean_score, params in zip(b5.cv_results_['mean_test_score'], b5.cv_results_['params']):
        print(f"{mean_score:.3f} for {params}")
def fonk4(predictions, b11):
    b6 = np.vstack((np.arange(len(predictions)).astype(int) + 1, predictions.astype(int))).T
    np.savetxt(b11, b6, b7 = "Id,Solution", fmt="%d", comments="", delimiter=",")
    print(f"Predictions saved to '{b11}'.")
def fonk5():
    b8 = "train.csv"
    b9 = "trainLabels.csv"
    b10 = "test.csv"
    b11 = "LinearSVMresult.csv"
    b1, b2, b3 = fonk1(b8, b9, b10)
    b12 = {'C': 10.0 ** np.arange(-5, 5)}
    x_train_split, x_val, y_train_split, b13 = train_test_split(b1, b2, test_size=0.2, random_state=42)
    b5 = fonk2(x_train_split, y_train_split, b12)
    fonk3(b5)
    b14 = LinearSVC(C=b5.best_params_['C'])
    b14.fit(b1, b2)
    b15 = b14.predict(b3)
    fonk4(b15, b11)
if b16 = = "__main__":
    fonk5()