import PolynomialModel
import DataUtils
import pandas as pd
import numpy as np
from time import time
import matplotlib.pyplot as plt
def main():
    dataset = load_and_preprocess_data("dataset.csv")
    degree = 1
    method = "L2GD"
    dataset = transform_and_normalize_data(dataset, degree)
    x_train, y_train, x_test, y_test = split_data(dataset)
    evaluate_model(x_train, y_train, x_test, y_test, degree, method)
def load_and_preprocess_data(file_path):
    dataset = pd.read_csv(file_path)
    dataset = dataset.drop(columns="OSM_ID")
    return dataset
def transform_and_normalize_data(dataset, degree):
    dataset = PolynomialModel.transform_dataset(dataset, degree)
    dataset = DataUtils.normalize(dataset, type="min-max")
    return dataset
def split_data(dataset):
    train, test = DataUtils.data_split(dataset, split_at=0.80)
    x_train, y_train = DataUtils.xy_split(train)
    x_test, y_test = DataUtils.xy_split(test)
    x_train.insert(0, "Const", np.ones(x_train.shape[0]))
    x_test.insert(0, "Const", np.ones(x_test.shape[0]))
    return x_train, y_train, x_test, y_test
def evaluate_model(x_train, y_train, x_test, y_test, degree, method):
    start_time = time()
    print(f"Using polynomial of degree: {degree}")
    w_list, lambdas, val_errs, train_errs = PolynomialModel.reg_fit(
        pd.concat([x_train, y_train], axis=1), alpha=7e-7, epsilion=1e-3, method=method, degree=degree
    )
    test_errs = [PolynomialModel.test(w, x_test, y_test) for w in w_list]
    plot_errors(lambdas, val_errs, degree, method)
    best_lambda, best_weights = select_best_model(lambdas, val_errs, w_list)
    print(f"\nSelected Regularization Parameter: {best_lambda}")
    print(f"\nExecution Time: {time() - start_time} seconds")
    print("Weights:\n", best_weights)
    print_errors(best_weights, x_train, y_train, x_test, y_test)
def plot_errors(lambdas, val_errs, degree, method):
    plt.title(f'Error w.r.t lambda - degree: {degree}, method: {method}')
    plt.ylabel('Error')
    plt.xlabel('Lambda')
    plt.plot(lambdas, val_errs, label="Validation Error")
    plt.legend()
    plt.grid(True)
    plt.show()
def select_best_model(lambdas, val_errs, w_list):
    min_index = np.argmin(val_errs)
    best_lambda = lambdas[min_index]
    best_weights = w_list[min_index]
    return best_lambda, best_weights
def print_errors(best_weights, x_train, y_train, x_test, y_test):
    train_mse = PolynomialModel.error(best_weights, x_train.values, y_train.values)
    test_mse = PolynomialModel.test(best_weights, x_test, y_test)
    print('Train Error (MSE):\t', train_mse)
    print('Test Error (MSE):\t', test_mse)
    print('Train Error (RMSE):\t', np.sqrt(train_mse))
    print('Test Error (RMSE):\t', np.sqrt(test_mse))
    print('Train Error (R2):\t', PolynomialModel.r2_error(best_weights, x_train, y_train))
    print('Test Error (R2):\t', PolynomialModel.r2_error(best_weights, x_test, y_test))
if __name__ == "__main__":
    main()