import numpy as np
import scipy.stats as stats
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_dataset = load_iris()
print("\nIris Dataset Keys:")
print(iris_dataset.keys())
X = iris_dataset.data
y = iris_dataset.target
print("\nClass Labels are:")
print(iris_dataset.target_names)
num_classes = len(iris_dataset.target_names)
print(f"{num_classes} class labels")
num_samples, num_features = X.shape
print(f"\nWe have {num_samples} samples")
print(f"With {num_features} features each")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
num_train_samples = len(X_train)
num_test_samples = len(X_test)
print(f"\n{num_train_samples} samples in the training set")
print(f"{num_test_samples} samples in the test set")
mu_matrix = np.zeros((num_classes, num_features), dtype=float)
sigma_matrix = np.zeros((num_classes, num_features), dtype=float)
for class_index in range(num_classes):
    mu_matrix[class_index] = X_train[y_train == class_index].mean(axis=0)
    sigma_matrix[class_index] = X_train[y_train == class_index].std(axis=0)
epsilon = 0.01
class_likelihoods = np.zeros(num_classes, dtype=float)
for class_index in range(num_classes):
    class_likelihoods[class_index] = (y_train == class_index).sum() / num_train_samples
class_given_data_matrix = np.zeros((num_test_samples, num_classes), dtype=float)
for i in range(num_test_samples):
    for class_index in range(num_classes):
        log_prob = np.log(class_likelihoods[class_index])
        for feature_index in range(num_features):
            log_prob += np.log(stats.norm.pdf(X_test[i, feature_index], mu_matrix[class_index, feature_index], sigma_matrix[class_index, feature_index]) + epsilon)
        class_given_data_matrix[i, class_index] = log_prob
accuracy = (class_given_data_matrix.argmax(axis=1) == y_test).sum() / num_test_samples
print("\nProbability that the model predicts the correct class label:")
print(accuracy)
print()