
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
def linear_regression(x, y):
    x = np.asarray(x).reshape(-1, 1)
    y = np.asarray(y).reshape(-1, 1)
    model = LinearRegression(fit_intercept=True)
    model.fit(x, y)
    plt.scatter(x, y)
    plt.plot(x, model.predict(x), color='red')
    plt.title("Linear Regression")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
def exponential_smoothing(data, alpha=0.25):
    out = [data[0]]
    for i in range(1, len(data)):
        value = alpha * data[i] + (1 - alpha) * out[i - 1]
        out.append(value)
    return out
def main():
    data1 = pd.read_csv("/Users/vothiquynhyen/Documents/AMZNdata.csv")
    data1 = data1.iloc[:, 1:]
    data_values = data1.values.flatten().tolist()
    plt.plot(data_values)
    plt.title("Original Data")
    plt.show()
    ok = "no"
    while ok.lower() != "yes":
        try:
            alpha = float(input("Enter your alpha for calculation: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        smoothed_values = exponential_smoothing(data_values, alpha)
        plt.clf()
        plt.plot(smoothed_values, color='red', linewidth=4, label='Smoothed')
        plt.plot(data_values, color='olive', linewidth=2, label='Original')
        plt.title("Exponential Smoothing")
        plt.legend()
        plt.show()
        ok = input("Are you happy with the result? (yes/no): ")
    next_prediction = alpha * data_values[-1] + (1 - alpha) * smoothed_values[-1]
    print(f"Prediction for next month is: {next_prediction}")
    linear_regression(range(len(data_values)), data_values)
if __name__ == "__main__":
    main()