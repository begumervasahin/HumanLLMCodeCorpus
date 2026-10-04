import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
def main():
    data = pd.read_csv('CleanData.csv')
    data.drop(['Unnamed: 0'], axis=1, inplace=True)
    data.drop(data.index[[0, 1, 5, 9, 73, 74, 75, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]], inplace=True)
    print(data.info())
    print(data.describe())
    x = data['Decimal Date'].values
    a = data['Seasonally Adjusted CO2 (ppm)'].values
    x_train, x_test = x[:600], x[601:703]
    a_train, a_actual = a[:600], a[601:703]
    degree = 2
    start_time = time.time()
    coef = np.polyfit(x_train, a_train, degree)
    print("Polynomial Coefficients:", coef.tolist())
    training_curve = np.polyval(coef, x_train)
    plt.figure()
    plt.scatter(x_train, a_train, color='red', label='Seasonally Adjusted CO2 (ppm)')
    plt.plot(x_train, training_curve, color='blue', label='Regression Line')
    plt.legend(loc='upper left')
    training_error = np.mean((a_train - training_curve) ** 2)
    print("================== Error During Training ======================")
    print("MSE = ", training_error)
    predicted_list = np.polyval(coef, x_test)
    prediction_error = np.mean((a_actual - predicted_list) ** 2)
    end_time = time.time()
    print("========================================================")
    print("Approx execution time: ", end_time - start_time, " seconds")
    print("================== Prediction ===========================")
    for year, pred in zip(x_test, predicted_list):
        print(f"Predicted value of CO2 (in ppm) for Year {year}: {pred}")
    print("================== Prediction Error ======================")
    print("MSE for Prediction = ", prediction_error)
    plt.show()
if __name__ == "__main__":
    main()