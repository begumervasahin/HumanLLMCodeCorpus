import numpy as np
from sklearn.model_selection import train_test_split
def normalize(x, type='min_max_normalization'):
    '''
    Performs normalization on the given vector according to the specified type.
    The type of normalization may be 'standardization' or 'min_max_normalization'.
    Defaults to 'min_max_normalization'.
    Arguments:
    x : numpy array
        The vector to be normalized
    type : str, optional
        The type of normalization to be performed (default is 'min_max_normalization')
    Returns:
    numpy array
        The normalized vector
    '''
    if type == 'standardization':
        return (x - np.mean(x)) / np.std(x)
    else:
        return (x - np.min(x)) / (np.max(x) - np.min(x))
def train_test_val_split(x1, x2, Y):
    '''
    Splits the data into train, test, and validation sets in the ratio 0.8 : 0.1 : 0.1.
    Arguments:
    x1 : numpy array
        Vector representing latitudes in the data
    x2 : numpy array
        Vector representing longitudes in the data
    Y : numpy array
        Vector representing the target variable in the data
    Returns:
    tuple
        Tuple containing the train, test, and validation sets for x1, x2, and Y
    '''
    x1 = np.reshape(x1, (x1.shape[0], 1))
    x2 = np.reshape(x2, (x2.shape[0], 1))
    X = np.concatenate((x1, x2), axis=1)
    Y = np.reshape(Y, (Y.shape[0], 1))
    X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.2, random_state=0)
    X_test, X_val, Y_test, Y_val = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=3)
    x1_train = X_train[:, 0].reshape(-1, 1)
    x1_test = X_test[:, 0].reshape(-1, 1)
    x1_val = X_val[:, 0].reshape(-1, 1)
    x2_train = X_train[:, 1].reshape(-1, 1)
    x2_test = X_test[:, 1].reshape(-1, 1)
    x2_val = X_val[:, 1].reshape(-1, 1)
    return x1_train, x1_test, x1_val, x2_train, x2_test, x2_val, Y_train, Y_test, Y_val
def generate_feature_matrix(x1, x2, degree):
    '''
    Generates a feature matrix for polynomial regression of a specified degree with two variables.
    Arguments:
    x1 : numpy array
        Vector representing the first variable (e.g., latitudes)
    x2 : numpy array
        Vector representing the second variable (e.g., longitudes)
    degree : int
        The desired degree of the polynomial to fit to the data
    Returns:
    numpy array
        The feature matrix for the specified polynomial degree
    '''
    x1 = np.reshape(x1, (x1.shape[0], 1))
    x2 = np.reshape(x2, (x2.shape[0], 1))
    feature_matrix = np.ones((x1.shape[0], 1))
    for d in range(1, degree + 1):
        for i in range(d + 1):
            feature = np.multiply(x1 ** (d - i), x2 ** i)
            feature = np.reshape(feature, (feature.shape[0], 1))
            feature_matrix = np.concatenate((feature_matrix, feature), axis=1)
    return np.asarray(feature_matrix)
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