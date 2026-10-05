import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
def linear_regression():
    x = np.asarray(data_list).reshape(-1, 1)
    y = np.asarray(smoothed_data).reshape(-1, 1)
    model = LinearRegression(fit_intercept=True)
    model.fit(x, y)
    plt.scatter(x, y)
    plt.show()
def exponential_smoothing(data, alpha=0.25):
    out = [data[0]]
    for i in range(1, len(data)):
        value = alpha * data[i] + (1 - alpha) * out[i - 1]
        out.append(value)
    return out
def main():
    data1 = pd.read_csv("/Users/vothiquynhyen/Documents/AMZNdata.csv")
    data1.describe()
    data1 = data1.iloc[:, 1:]
    plt.plot(data1)
    arr = data1.values
    data_list = arr[0].tolist()
    plt.plot(data_list)
    plt.show()
    ok = "no"
    while ok != "yes":
        alpha = float(input("Enter the alpha value for calculation: "))
        smoothed_data = exponential_smoothing(data_list, alpha)
        plt.clf()
        plt.plot(smoothed_data, color='red', linewidth=4)
        plt.plot(data_list, color='olive', linewidth=2)
        plt.show()
        ok = input("Are you happy with the result? (yes/no)")
    ninth = alpha * data_list[7] + (1 - alpha) * smoothed_data[7]
    print("Prediction for next month is:", ninth)
    linear_regression()
    print("Done")
if __name__ == "__main__":
    main()