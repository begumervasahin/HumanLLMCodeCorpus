import numpy as np
import scipy as sp
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_dataset = load_iris()
print("Iris Dataset Keys:")
print(iris_dataset.keys())
X = iris_dataset.data
y = iris_dataset.target
print("\nClass Labels are:")
print(iris_dataset.target_names)
num_classes = len(iris_dataset.target_names)
print("{} class labels".format(num_classes))
num_samples, num_features = X.shape
print("\nWe have {} samples".format(num_samples))
print("With {} features each".format(num_features))
X_train, X_test, y_train, y_test = train_test_split(X, y)
num_train_samples = len(X_train)
num_test_samples = len(X_test)
print("\n{} samples in the training set".format(num_train_samples))
print("{} samples in the test set".format(num_test_samples))
mean_matrix = np.zeros((num_classes, num_features), dtype=float)
std_matrix = np.zeros((num_classes, num_features), dtype=float)
for i in range(0, num_classes):
    mean_matrix[i] = X_train[y_train == i].mean(axis=0)
    std_matrix[i] = X_train[y_train == i].std(axis=0)
epsilon = 0.01
class_likelihood = np.zeros(num_classes, dtype=float)
for i in range(0, num_classes):
    class_likelihood[i] = (y_train == i).sum() / num_train_samples
class_given_data_matrix = np.zeros((num_test_samples, num_classes), dtype=float)
for i in range(0, num_test_samples):
    for k in range(0, num_classes):
        class_given_data = np.log(class_likelihood[k])
        for j in range(0, num_features):
            class_given_data += np.log(sp.stats.norm.pdf(X_test[i, j], mean_matrix[k, j], std_matrix[k, j]) * 2 * epsilon)
        class_given_data_matrix[i, k] = class_given_data
print("\nProbability that the Model predicts the correct class label:")
print((class_given_data_matrix.argmax(axis=1) == y_test).sum() / num_test_samples)