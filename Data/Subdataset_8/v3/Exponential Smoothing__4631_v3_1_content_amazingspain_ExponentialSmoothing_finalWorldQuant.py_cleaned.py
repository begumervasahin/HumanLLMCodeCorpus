import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
def perform_linear_regression(x, y):
    x = np.asarray(x).reshape(-1, 1)
    y = np.asarray(y).reshape(-1, 1)
    model = LinearRegression(fit_intercept=True)
    model.fit(x, y)
    plt.scatter(x, y)
    plt.show()
def apply_exponential_smoothing(data, alpha=0.25):
    smoothed_data = [data[0]]
    for i in range(1, len(data)):
        smoothed_value = alpha * data[i] + (1 - alpha) * smoothed_data[i - 1]
        smoothed_data.append(smoothed_value)
    return smoothed_data
def main():
    data = pd.read_csv("/Users/vothiquynhyen/Documents/AMZNdata.csv")
    data = data.iloc[:, 1:]
    plt.plot(data)
    original_values = data.values[0].tolist()
    plt.plot(original_values)
    plt.show()
    user_satisfied = False
    while not user_satisfied:
        alpha = float(input("Enter the alpha value for exponential smoothing: "))
        smoothed_values = apply_exponential_smoothing(original_values, alpha)
        plt.clf()
        plt.plot(smoothed_values, color='red', linewidth=4)
        plt.plot(original_values, color='olive', linewidth=2)
        plt.show()
        user_satisfied = input("Are you happy with the result? (yes/no)").lower() == "yes"
    next_month_prediction = alpha * original_values[7] + (1 - alpha) * smoothed_values[7]
    print("Prediction for next month:", next_month_prediction)
    perform_linear_regression(range(len(original_values)), original_values)
if __name__ == "__main__":
    main()