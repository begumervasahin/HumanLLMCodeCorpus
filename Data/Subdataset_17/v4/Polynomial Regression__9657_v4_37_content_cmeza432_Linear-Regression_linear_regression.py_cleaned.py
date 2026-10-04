import numpy as np
import sys
def get_bigphi(data, rows, cols, degree):
    result = []
    t_values = []
    for i in range(rows):
        row_result = [1]
        for k in range(cols):
            if k == (cols - 1):
                t_values.append(data[i][k])
            else:
                for deg in range(degree):
                    row_result.append(np.power(data[i][k], deg + 1))
        result.append(row_result)
    return np.array(result), np.array(t_values)
def get_weights(big_phi, t_values, lamb):
    phi_t = np.transpose(big_phi)
    identity = np.identity(big_phi.shape[1])
    lamb_m = lamb * identity
    temp = np.matmul(phi_t, big_phi)
    first = np.add(lamb_m, temp)
    inverse = np.linalg.pinv(first)
    second = np.matmul(inverse, phi_t)
    weights = np.matmul(second, t_values)
    return weights
def get_prediction(test_phi, weights):
    return np.dot(test_phi, weights)
def print_weights(weights):
    for i, weight in enumerate(weights):
        print(f"w{i}={weight:.4f}")
def print_test(predictions, targets):
    for i, (prediction, target) in enumerate(zip(predictions, targets)):
        error = (prediction - target) ** 2
        print(f"ID={i+1:5d}, output={prediction:5.4f}, target value={target:5.4f}, squared error={error:.4f}")
def linear_regression(training, degree, lamb, test):
    training_rows, training_cols = training.shape
    test_rows, test_cols = test.shape
    big_phi, t_values = get_bigphi(training, training_rows, training_cols, degree)
    weights = get_weights(big_phi, t_values, lamb)
    print_weights(weights)
    test_phi, target_values = get_bigphi(test, test_rows, test_cols, degree)
    predictions = get_prediction(test_phi, weights)
    print_test(predictions, target_values)
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Error, not enough arguments given!")
    else:
        training_file = sys.argv[1]
        degree = int(sys.argv[2])
        lamb = float(sys.argv[3])
        test_file = sys.argv[4]
        training_data = np.loadtxt(training_file)
        test_data = np.loadtxt(test_file)
        linear_regression(training_data, degree, lamb, test_data)