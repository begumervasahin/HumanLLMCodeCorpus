import numpy as np
import scipy as sp
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
def load_and_split_data():
    iris_dataset = load_iris()
    X = iris_dataset.data
    y = iris_dataset.target
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test, iris_dataset.target_names
def compute_class_likelihood(y_train):
    n_train = len(y_train)
    class_likelihood = np.zeros(len(np.unique(y_train)), dtype=float)
    for i, label in enumerate(np.unique(y_train)):
        class_likelihood[i] = (y_train == label).sum() / n_train
    return class_likelihood
def compute_mean_and_std(X_train, y_train):
    mu_mat = np.zeros((len(np.unique(y_train)), X_train.shape[1]), dtype=float)
    sig_mat = np.zeros((len(np.unique(y_train)), X_train.shape[1]), dtype=float)
    for i, label in enumerate(np.unique(y_train)):
        mu_mat[i] = X_train[y_train == label].mean(axis=0)
        sig_mat[i] = X_train[y_train == label].std(axis=0)
    return mu_mat, sig_mat
def compute_class_probability(X_test, mu_mat, sig_mat, class_likelihood, epsilon=0.01):
    class_given_data_mat = np.zeros((len(X_test), len(mu_mat)), dtype=float)
    for i in range(len(X_test)):
        for k in range(len(mu_mat)):
            class_given_data = np.log(class_likelihood[k])
            for j in range(X_test.shape[1]):
                class_given_data += np.log(sp.stats.norm.pdf(X_test[i, j], mu_mat[k, j], sig_mat[k, j]) * 2 * epsilon)
            class_given_data_mat[i, k] = class_given_data
    return class_given_data_mat
def main():
    X_train, X_test, y_train, y_test, target_names = load_and_split_data()
    class_likelihood = compute_class_likelihood(y_train)
    mu_mat, sig_mat = compute_mean_and_std(X_train, y_train)
    class_given_data_mat = compute_class_probability(X_test, mu_mat, sig_mat, class_likelihood)
    accuracy = (class_given_data_mat.argmax(axis=1) == y_test).sum() / len(y_test)
    print("Probability that the Model predicts the correct class label:", accuracy)
if __name__ == "__main__":
    main()