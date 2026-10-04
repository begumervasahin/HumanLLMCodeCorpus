import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data.drop(['Unnamed: 0'], axis=1, inplace=True)
    data.drop(data.index[[0, 1, 5, 9, 73, 74, 75, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]], inplace=True)
    return data
def split_data(data):
    x = data['Decimal Date'].values
    a = data['Seasonally Adjusted CO2 (ppm)'].values
    x_train, x_test = x[:600], x[601:703]
    a_train, a_actual = a[:600], a[601:703]
    return x_train, a_train, x_test, a_actual
def polynomial_regression(x_train, y_train, degree):
    return np.polyfit(x_train, y_train, degree)
def calculate_mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)
def main():
    data = load_and_preprocess_data('CleanData.csv')
    print(data.info())
    print(data.describe())
    x_train, a_train, x_test, a_actual = split_data(data)
    degree = 2
    start_time = time.time()
    coefficients = polynomial_regression(x_train, a_train, degree)
    print("Polynomial Coefficients:", coefficients.tolist())
    training_curve = np.polyval(coefficients, x_train)
    plt.figure()
    plt.scatter(x_train, a_train, color='red', label='Seasonally Adjusted CO2 (ppm)')
    plt.plot(x_train, training_curve, color='blue', label='Regression Line')
    plt.legend(loc='upper left')
    training_error = calculate_mse(a_train, training_curve)
    print("================== Error During Training ======================")
    print("MSE = ", training_error)
    predicted_list = np.polyval(coefficients, x_test)
    prediction_error = calculate_mse(a_actual, predicted_list)
    end_time = time.time()
    print("========================================================")
    print("Approx execution time: ", end_time - start_time, " seconds")
    print("================== Prediction ===========================")
    for year, prediction in zip(x_test, predicted_list):
        print(f"Predicted value of CO2 (in ppm) for Year {year}: {prediction}")
    print("================== Prediction Error ======================")
    print("MSE for Prediction = ", prediction_error)
    plt.show()
if __name__ == "__main__":
    main()