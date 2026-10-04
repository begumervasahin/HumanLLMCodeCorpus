import numpy as np
import scipy.stats as stats
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
def main():
    iris_dataset = load_iris()
    print("\nIris Dataset Keys:")
    print(iris_dataset.keys())
    X = iris_dataset.data
    y = iris_dataset.target
    print("\nClass Labels are:")
    print(iris_dataset.target_names)
    Cn = len(iris_dataset.target_names)
    print(f"{Cn} class labels")
    n, d_features = X.shape
    print(f"\nWe have {n} samples")
    print(f"With {d_features} features each")
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    n_train = len(X_train)
    n_test = len(X_test)
    print(f"\n{n_train} samples in the training set")
    print(f"{n_test} samples in the test set")
    mu_mat = np.zeros((Cn, d_features), dtype=float)
    sig_mat = np.zeros((Cn, d_features), dtype=float)
    for i in range(Cn):
        mu_mat[i] = X_train[y_train == i].mean(axis=0)
        sig_mat[i] = X_train[y_train == i].std(axis=0)
    epsilon = 0.01
    class_likelihood = np.zeros(Cn, dtype=float)
    for i in range(Cn):
        class_likelihood[i] = (y_train == i).sum() / n_train
    class_given_data_mat = np.zeros((n_test, Cn), dtype=float)
    for i in range(n_test):
        for k in range(Cn):
            class_given_data = np.log(class_likelihood[k])
            for j in range(d_features):
                class_given_data += np.log(stats.norm.pdf(X_test[i, j], mu_mat[k, j], sig_mat[k, j]) * 2 * epsilon)
            class_given_data_mat[i, k] = class_given_data
    accuracy = (class_given_data_mat.argmax(axis=1) == y_test).sum() / n_test
    print("\nProbability that the Model predicts the correct class label:")
    print(accuracy)
if __name__ == '__main__':
    main()