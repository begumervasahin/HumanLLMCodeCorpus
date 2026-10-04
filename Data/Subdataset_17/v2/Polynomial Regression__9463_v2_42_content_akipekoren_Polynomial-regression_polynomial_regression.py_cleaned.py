import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
def main():
    df = pd.read_csv("kc_house_data.csv")
    data_x = df["sqft_living"]
    data_y = df["price"]
    train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.3, random_state=42)
    train_x = normalize(train_x)
    test_x = normalize(test_x)
    train_y = normalize(train_y)
    test_y = normalize(test_y)
    return train_x, test_x, train_y, test_y
def normalize(series):
    return (series - series.min()) / (series.max() - series.min())
def sort_inputs(x, y):
    sorted_pairs = sorted(zip(x, y))
    sorted_x, sorted_y = zip(*sorted_pairs)
    return np.array(sorted_x), np.array(sorted_y)
def compute_weights(x_matrix, identity_matrix, ridge, y):
    x_transpose_x = np.dot(x_matrix.T, x_matrix)
    regularization = ridge * identity_matrix
    inverse_term = np.linalg.inv(x_transpose_x + regularization)
    x_transpose_y = np.dot(x_matrix.T, y)
    return np.dot(inverse_term, x_transpose_y)
def create_identity_and_input_matrix(x, degree):
    identity_matrix = np.identity(degree + 1)
    ones_column = np.ones(len(x))
    x_matrix = np.column_stack([np.power(x, i) for i in range(degree + 1)])
    return x_matrix, identity_matrix
def polynomial_regression(train_x, train_y):
    max_complexity = 7
    prediction_list = []
    error_list = []
    for complexity in range(1, max_complexity):
        x_matrix, identity_matrix = create_identity_and_input_matrix(train_x, complexity)
        weights = compute_weights(x_matrix, identity_matrix, ridge=0.00001, y=train_y)
        y_pred = np.polyval(weights[::-1], train_x)
        plt.scatter(train_x, train_y)
        plt.plot(train_x, y_pred, color='red')
        plt.show()
        error_list.append(calculate_mse(train_y, y_pred))
        prediction_list.append(y_pred)
    return error_list
def calculate_mse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))
def plot_rmse(error_list, color):
    plt.title("Root Mean Square Error of Train and Test Data")
    plt.xlabel("Complexity")
    plt.ylabel("RMSE score")
    plt.ylim([0, 1])
    plt.plot(range(len(error_list)), error_list, color=color)
    plt.show()
if __name__ == "__main__":
    train_x, test_x, train_y, test_y = main()
    train_x, train_y = sort_inputs(train_x, train_y)
    error_list = polynomial_regression(train_x, train_y)
    print(error_list)