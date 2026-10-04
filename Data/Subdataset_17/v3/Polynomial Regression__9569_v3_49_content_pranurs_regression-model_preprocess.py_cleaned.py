import numpy as np
from sklearn.model_selection import train_test_split
def normalize(x, type='min_max_normalization'):
    if type == 'standardization':
        return (x - np.mean(x)) / np.std(x)
    return (x - np.min(x)) / (np.max(x) - np.min(x))
def train_test_val_split(x1, x2, Y):
    x1 = x1.reshape(-1, 1)
    x2 = x2.reshape(-1, 1)
    X = np.hstack((x1, x2))
    Y = Y.reshape(-1, 1)
    X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.2, random_state=0)
    X_test, X_val, Y_test, Y_val = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=3)
    x1_train, x2_train = X_train[:, 0], X_train[:, 1]
    x1_test, x2_test = X_test[:, 0], X_test[:, 1]
    x1_val, x2_val = X_val[:, 0], X_val[:, 1]
    return x1_train, x1_test, x1_val, x2_train, x2_test, x2_val, Y_train, Y_test, Y_val
def generate_feature_matrix(x1, x2, degree):
    x1 = x1.reshape(-1, 1)
    x2 = x2.reshape(-1, 1)
    feature_matrix = np.ones((x1.shape[0], 1))
    for d in range(1, degree + 1):
        for i in range(d + 1):
            feature = (x1 ** (d - i)) * (x2 ** i)
            feature_matrix = np.hstack((feature_matrix, feature.reshape(-1, 1)))
    return feature_matrix
if __name__ == "__main__":
    x1 = np.array([1, 2, 3, 4, 5])
    x2 = np.array([2, 3, 4, 5, 6])
    Y = np.array([3, 4, 5, 6, 7])
    x1_normalized = normalize(x1, type='min_max_normalization')
    print("Normalized x1:", x1_normalized)
    x1_train, x1_test, x1_val, x2_train, x2_test, x2_val, Y_train, Y_test, Y_val = train_test_val_split(x1, x2, Y)
    print("x1_train:", x1_train)
    print("x1_test:", x1_test)
    print("x1_val:", x1_val)
    print("x2_train:", x2_train)
    print("x2_test:", x2_test)
    print("x2_val:", x2_val)
    print("Y_train:", Y_train)
    print("Y_test:", Y_test)
    print("Y_val:", Y_val)
    degree = 2
    feature_matrix = generate_feature_matrix(x1, x2, degree)
    print("Feature Matrix:\n", feature_matrix)