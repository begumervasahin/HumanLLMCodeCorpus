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
    plt.show()
def exponential_smoothing(data, alpha=0.25):
    smoothed_data = [data[0]]
    for i in range(1, len(data)):
        value = alpha * data[i] + (1 - alpha) * smoothed_data[i - 1]
        smoothed_data.append(value)
    return smoothed_data
def main():
    file_path = "/Users/vothiquynhyen/Documents/AMZNdata.csv"
    data = pd.read_csv(file_path)
    data.describe()
    data = data.iloc[:, 1:]
    plt.plot(data)
    data_list = data.iloc[0].tolist()
    plt.plot(data_list)
    plt.show()
    is_happy = False
    while not is_happy:
        alpha = float(input("Enter the alpha value for calculation: "))
        smoothed_data = exponential_smoothing(data_list, alpha)
        plt.clf()
        plt.plot(smoothed_data, color='red', linewidth=4)
        plt.plot(data_list, color='olive', linewidth=2)
        plt.show()
        is_happy = input("Are you happy with the result? (yes/no)").lower() == 'yes'
    ninth = alpha * data_list[7] + (1 - alpha) * smoothed_data[7]
    print("Prediction for next month is:", ninth)
    linear_regression(range(len(data_list)), data_list)
    print("Done")
if __name__ == "__main__":
    main()