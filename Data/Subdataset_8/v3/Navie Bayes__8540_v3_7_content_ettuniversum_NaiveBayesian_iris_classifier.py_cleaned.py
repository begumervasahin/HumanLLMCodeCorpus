import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.stats import norm
def load_and_split_data():
    iris_dataset = load_iris()
    X = iris_dataset.data
    y = iris_dataset.target
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test, iris_dataset.target_names
def calculate_statistics(X_train, y_train):
    num_classes = len(np.unique(y_train))
    num_features = X_train.shape[1]
    mean_matrix = np.array([X_train[y_train == i].mean(axis=0) for i in range(num_classes)])
    std_matrix = np.array([X_train[y_train == i].std(axis=0) for i in range(num_classes)])
    return mean_matrix, std_matrix
def calculate_class_likelihood(y_train):
    class_likelihood = np.array([(y_train == i).sum() / len(y_train) for i in range(len(np.unique(y_train)))])
    return class_likelihood
def calculate_class_given_data(X_test, mean_matrix, std_matrix, class_likelihood):
    epsilon = 0.01
    num_classes = len(class_likelihood)
    num_test_samples, num_features = X_test.shape
    class_given_data_matrix = np.zeros((num_test_samples, num_classes))
    for i in range(num_test_samples):
        for k in range(num_classes):
            class_given_data = np.log(class_likelihood[k])
            for j in range(num_features):
                class_given_data += np.log(norm.pdf(X_test[i, j], mean_matrix[k, j], std_matrix[k, j]) * 2 * epsilon)
            class_given_data_matrix[i, k] = class_given_data
    return class_given_data_matrix
def main():
    X_train, X_test, y_train, y_test, target_names = load_and_split_data()
    mean_matrix, std_matrix = calculate_statistics(X_train, y_train)
    class_likelihood = calculate_class_likelihood(y_train)
    class_given_data_matrix = calculate_class_given_data(X_test, mean_matrix, std_matrix, class_likelihood)
    accuracy = (class_given_data_matrix.argmax(axis=1) == y_test).sum() / len(y_test)
    print("\nProbability that the Model predicts the correct class label:")
    print(accuracy)
if __name__ == "__main__":
    main()