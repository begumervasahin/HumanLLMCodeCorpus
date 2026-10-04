
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
def fonk1(b1, b2):
    b1 = np.asarray(b1).reshape(-1, 1)
    b2 = np.asarray(b2).reshape(-1, 1)
    b3 = LinearRegression(fit_intercept=True)
    b3.fit(b1, b2)
    plt.scatter(b1, b2)
    plt.plot(b1, b3.predict(b1), b4 = 'red')
    plt.title("Linear Regression")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
def fonk2(data, b5 = 0.25):
    b6 = [data[0]]
    for i in range(1, len(data)):
        b7 = b5 * data[i] + (1 - b5) * b6[i - 1]
        b6.append(b7)
    return b6
def fonk3():
    b8 = pd.read_csv("/Users/vothiquynhyen/Documents/AMZNdata.csv")
    b8 = b8.iloc[:, 1:]
    b9 = b8.values.flatten().tolist()
    plt.plot(b9)
    plt.title("Original Data")
    plt.show()
    b10 = "no"
    while b10.lower() != "yes":
        try:
            b5 = float(input("Enter your b5 for calculation: "))
        except ValueError:
            print("Invalid input. Please enter a numeric b7.")
            continue
        b11 = fonk2(b9, b5)
        plt.clf()
        plt.plot(b11, b4 = 'red', linewidth=4, label='Smoothed')
        plt.plot(b9, b4 = 'olive', linewidth=2, label='Original')
        plt.title("Exponential Smoothing")
        plt.legend()
        plt.show()
        b10 = input("Are you happy with the result? (yes/no): ")
    b12 = b5 * b9[-1] + (1 - b5) * b11[-1]
    print(f"Prediction for next month is: {b12}")
    fonk1(range(len(b9)), b9)
if b13 = = "__main__":
    fonk3()