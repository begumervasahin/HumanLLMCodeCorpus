import numpy as np
from sklearn.model_selection import train_test_split
def fonk1(x, b1 = 'min_max_normalization'):
    '''
    Performs normalization on the given vector according to the specified b1.
    The b1 of normalization may be 'standardization' or 'min_max_normalization'.
    Defaults to 'min_max_normalization'.
    Arguments:
    x : numpy array
        The vector to be normalized
    b1 : str, optional
        The b1 of normalization to be performed (default is 'min_max_normalization')
    Returns:
    numpy array
        The normalized vector
    '''
    if b1 = = 'standardization':
        return (x - np.mean(x)) / np.std(x)
    else:
        return (x - np.min(x)) / (np.max(x) - np.min(x))
def fonk2(b2, b3, b5):
    '''
    Splits the data into train, test, and validation sets in the ratio 0.8 : 0.1 : 0.1.
    Arguments:
    b2 : numpy array
        Vector representing latitudes in the data
    b3 : numpy array
        Vector representing longitudes in the data
    b5 : numpy array
        Vector representing the target variable in the data
    Returns:
    tuple
        Tuple containing the train, test, and validation sets for b2, b3, and b5
    '''
    b2 = np.reshape(b2, (b2.shape[0], 1))
    b3 = np.reshape(b3, (b3.shape[0], 1))
    b4 = np.concatenate((b2, b3), axis=1)
    b5 = np.reshape(b5, (b5.shape[0], 1))
    X_train, X_temp, Y_train, b6 = train_test_split(b4, b5, test_size=0.2, random_state=0)
    X_test, X_val, Y_test, b7 = train_test_split(X_temp, b6, test_size=0.5, random_state=3)
    b8 = X_train[:, 0].reshape(-1, 1)
    b9 = X_test[:, 0].reshape(-1, 1)
    b10 = X_val[:, 0].reshape(-1, 1)
    b11 = X_train[:, 1].reshape(-1, 1)
    b12 = X_test[:, 1].reshape(-1, 1)
    b13 = X_val[:, 1].reshape(-1, 1)
    return b8, b9, b10, b11, b12, b13, Y_train, Y_test, b7
def fonk3(b2, b3, a1):
    '''
    Generates a b15 matrix for polynomial regression of a specified a1 with two variables.
    Arguments:
    b2 : numpy array
        Vector representing the first variable (e.g., latitudes)
    b3 : numpy array
        Vector representing the second variable (e.g., longitudes)
    a1 : int
        The desired a1 of the polynomial to fit to the data
    Returns:
    numpy array
        The b15 matrix for the specified polynomial a1
    '''
    b2 = np.reshape(b2, (b2.shape[0], 1))
    b3 = np.reshape(b3, (b3.shape[0], 1))
    b14 = np.ones((b2.shape[0], 1))
    for d in range(1, a1 + 1):
        for i in range(d + 1):
            b15 = np.multiply(b2 ** (d - i), b3 ** i)
            b15 = np.reshape(b15, (b15.shape[0], 1))
            b14 = np.concatenate((b14, b15), axis=1)
    return np.asarray(b14)
if b16 = = "__main__":
    b2 = np.array([1, 2, 3, 4, 5])
    b3 = np.array([2, 3, 4, 5, 6])
    b5 = np.array([3, 4, 5, 6, 7])
    b17 = fonk1(b2, b1='min_max_normalization')
    print("Normalized b2:", b17)
    b8, b9, b10, b11, b12, b13, Y_train, Y_test, b7 = fonk2(b2, b3, b5)
    print("b8:", b8)
    print("b9:", b9)
    print("b10:", b10)
    print("b11:", b11)
    print("b12:", b12)
    print("b13:", b13)
    print("Y_train:", Y_train)
    print("Y_test:", Y_test)
    print("b7:", b7)
    a1 = 2
    b14 = fonk3(b2, b3, a1)
    print("Feature Matrix:\n", b14)