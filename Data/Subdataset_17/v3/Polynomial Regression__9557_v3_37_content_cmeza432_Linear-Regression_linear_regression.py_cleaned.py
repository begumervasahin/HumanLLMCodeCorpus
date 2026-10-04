import numpy as np
import sys
def construct_design_matrix(data, rows, cols, degree):
    design_matrix = []
    target_values = []
    for i in range(rows):
        row = [1]
        for k in range(cols):
            if k == cols - 1:
                target_values.append(data[i][k])
            else:
                for deg in range(degree):
                    row.append(data[i][k] ** (deg + 1))
        design_matrix.append(row)
    return np.array(design_matrix), np.array(target_values)
def compute_weights(design_matrix, target_values, regularization_param):
    phi_transpose = np.transpose(design_matrix)
    identity_matrix = np.identity(design_matrix.shape[1])
    regularization_matrix = regularization_param * identity_matrix
    to_invert = np.add(np.matmul(phi_transpose, design_matrix), regularization_matrix)
    inverted_matrix = np.linalg.pinv(to_invert)
    weights = np.matmul(np.matmul(inverted_matrix, phi_transpose), target_values)
    return weights
def predict(test_design_matrix, weights):
    return np.dot(test_design_matrix, weights)
def display_weights(weights):
    for i, weight in enumerate(weights):
        print(f"w{i} = {weight:.4f}")
def display_test_results(predictions, target_values):
    for i, (prediction, target) in enumerate(zip(predictions, target_values)):
        squared_error = (prediction - target) ** 2
        print(f"ID={i+1:5d}, output={prediction:.4f}, target value={target:.4f}, squared error={squared_error:.4f}")
def linear_regression(training_data, degree, regularization_param, test_data):
    training_rows, training_cols = training_data.shape
    test_rows, test_cols = test_data.shape
    training_design_matrix, training_targets = construct_design_matrix(training_data, training_rows, training_cols, degree)
    weights = compute_weights(training_design_matrix, training_targets, regularization_param)
    display_weights(weights)
    test_design_matrix, test_targets = construct_design_matrix(test_data, test_rows, test_cols, degree)
    predictions = predict(test_design_matrix, weights)
    display_test_results(predictions, test_targets)
if len(sys.argv) != 5:
    print("Error, not enough arguments given!")
else:
    training_file = sys.argv[1]
    degree = int(sys.argv[2])
    regularization_param = float(sys.argv[3])
    test_file = sys.argv[4]
    with open(training_file) as file:
        training_data = np.array([list(map(float, line.split())) for line in file])
    with open(test_file) as file:
        test_data = np.array([list(map(float, line.split())) for line in file])
    linear_regression(training_data, degree, regularization_param, test_data)