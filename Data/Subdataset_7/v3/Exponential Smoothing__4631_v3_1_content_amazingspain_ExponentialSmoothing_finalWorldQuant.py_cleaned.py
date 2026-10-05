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
    plt.show()
def fonk2(b7, b4 = 0.25):
    b5 = [b7[0]]
    for i in range(1, len(b7)):
        b6 = b4 * b7[i] + (1 - b4) * b5[i - 1]
        b5.append(b6)
    return b5
def fonk3():
    b7 = pd.read_csv("/Users/vothiquynhyen/Documents/AMZNdata.csv")
    b7 = b7.iloc[:, 1:]
    plt.plot(b7)
    b8 = b7.values[0].tolist()
    plt.plot(b8)
    plt.show()
    b9 = False
    while not b9:
        b4 = float(input("Enter the b4 value for exponential smoothing: "))
        b10 = fonk2(b8, b4)
        plt.clf()
        plt.plot(b10, b11 = 'red', linewidth=4)
        plt.plot(b8, b11 = 'olive', linewidth=2)
        plt.show()
        b9 = input("Are you happy with the result? (yes/no)").lower() == "yes"
    b12 = b4 * b8[7] + (1 - b4) * b10[7]
    print("Prediction for next month:", b12)
    fonk1(range(len(b8)), b8)
if b13 = = "__main__":
    fonk3()