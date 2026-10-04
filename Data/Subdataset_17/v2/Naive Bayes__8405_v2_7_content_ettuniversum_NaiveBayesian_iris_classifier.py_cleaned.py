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
    print("\nClass Labels:")
    print(iris_dataset.target_names)
    Cn = len(iris_dataset.target_names)
    print(f"Number of class labels: {Cn}")
    n, d_features = X.shape
    print(f"\nNumber of samples: {n}")
    print(f"Number of features per sample: {d_features}")
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    n_train = len(X_train)
    n_test = len(X_test)
    print(f"\nNumber of training samples: {n_train}")
    print(f"Number of testing samples: {n_test}")
    mu_mat = np.zeros((Cn, d_features))
    sig_mat = np.zeros((Cn, d_features))
    for i in range(Cn):
        mu_mat[i] = X_train[y_train == i].mean(axis=0)
        sig_mat[i] = X_train[y_train == i].std(axis=0)
    epsilon = 0.01
    class_likelihood = np.zeros(Cn)
    for i in range(Cn):
        class_likelihood[i] = (y_train == i).sum() / n_train
    class_given_data_mat = np.zeros((n_test, Cn))
    for i in range(n_test):
        for k in range(Cn):
            log_prob = np.log(class_likelihood[k])
            for j in range(d_features):
                log_prob += np.log(stats.norm.pdf(X_test[i, j], mu_mat[k, j], sig_mat[k, j]) + epsilon)
            class_given_data_mat[i, k] = log_prob
    predicted_classes = class_given_data_mat.argmax(axis=1)
    accuracy = (predicted_classes == y_test).sum() / n_test
    print("\nModel Accuracy:")
    print(f"{accuracy:.2f}")
if __name__ == '__main__':
    main()