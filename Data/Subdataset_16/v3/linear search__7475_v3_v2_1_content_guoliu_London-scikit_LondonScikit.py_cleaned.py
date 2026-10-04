import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
def fonk1(train_file, train_labels_file, test_file):
    b1 = np.loadtxt(open(train_file, "rb"), delimiter=",", skiprows=0)
    b2 = np.loadtxt(open(train_labels_file, "rb"), delimiter=",", skiprows=0)
    b3 = np.loadtxt(open(test_file, "rb"), delimiter=",", skiprows=0)
    return b1, b2, b3
def fonk2(x_train_split, y_train_split):
    b4 = {'C': 10. ** np.arange(-5, 5)}
    b5 = LinearSVC()
    b6 = GridSearchCV(b5, b4, cv=5, verbose=3)
    b6.fit(x_train_split, y_train_split)
    return b6
def fonk3(b6):
    print("Best parameters found:")
    print(b6.best_params_)
def fonk4(b6):
    print("\nGrid scores:")
    for mean_score, params in zip(b6.cv_results_['mean_test_score'], b6.cv_results_['params']):
        print(f"{mean_score:.3f} (+/-{b6.cv_results_['std_test_score'][0] * 2:.03f}) for {params}")
def fonk5(b1, b2, best_params):
    b7 = LinearSVC(C=best_params['C'])
    b7.fit(b1, b2)
    return b7
def fonk6(b11, output_file):
    b8 = np.vstack((np.arange(len(b11)).astype(int) + 1, b11.astype(int))).T
    np.savetxt(output_file, b8, b9 = "Id,Solution", fmt="%d", comments="", delimiter=",")
def fonk7():
    b1, b2, b3 = fonk1("train.csv", "trainLabels.csv", "test.csv")
    x_train_split, x_val, y_train_split, b10 = train_test_split(b1, b2, test_size=0.2, random_state=42)
    b6 = fonk2(x_train_split, y_train_split)
    fonk3(b6)
    fonk4(b6)
    b7 = fonk5(b1, b2, b6.best_params_)
    b11 = b7.predict(b3)
    fonk6(b11, "LinearSVMresult.csv")
if b12 = = "__main__":
    fonk7()