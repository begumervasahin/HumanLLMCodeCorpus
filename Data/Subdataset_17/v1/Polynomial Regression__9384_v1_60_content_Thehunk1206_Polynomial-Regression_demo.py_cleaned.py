import numpy as np
from numpy.polynomial.polynomial import Polynomial
import pandas as pd
import matplotlib.pyplot as plt
import time
def main():
    data = pd.read_csv('CleanData.csv')
    data.drop(['Unnamed: 0'], axis=1, inplace=True)
    data.drop(data.index[[0, 1, 5, 9, 73, 74, 75, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]], inplace=True)
    print(data.info())
    print(data.describe())
    fig = plt.figure()
    graph1 = fig.add_subplot(1, 1, 1)
    x = data['Decimal Date'].tolist()
    a = data['Seasonally Adjusted CO2 (ppm)'].tolist()
    x_train = x[0:600]
    a_train = a[0:600]
    x_test = x[601:703]
    a_actual = a[601:703]
    degree = 2
    startTime = time.time()
    coef = np.polyfit(x_train, a_train, degree)
    coefList = coef.tolist()
    print(coefList)
    training_curve = np.polyval(coef, x_train)
    graph1.scatter(x_train, a_train, color='red', label='Seasonally Adjusted CO2 (ppm)')
    graph1.plot(x_train, training_curve, color='blue', label='Regression Line')
    graph1.legend(loc='upper left')
    training_error = np.mean((a_train - training_curve) ** 2)
    print("==================Error During training=======================")
    print("MSE = ", training_error)
    predicted_list = np.polyval(coef, x_test)
    prediction_error = np.mean((a_actual - predicted_list) ** 2)
    endTime = time.time()
    print("========================================================")
    print("Approx execution time: ", endTime - startTime, "Seconds")
    print("==================Prediction===========================")
    for i in range(len(x_test)):
        print(f"Predicted value of CO2 (in ppm) for Year: {x_test[i]} is {predicted_list[i]}")
    print("==================Prediction Error=======================")
    print("MSE FOR Prediction = ", prediction_error)
    plt.show()
if __name__ == "__main__":
    main()