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
def fonk2(b8, b4 = 0.25):
    b5 = [b8[0]]
    for i in range(1, len(b8)):
        b6 = b4 * b8[i] + (1 - b4) * b5[i - 1]
        b5.append(b6)
    return b5
def fonk3():
    b7 = "/Users/vothiquynhyen/Documents/AMZNdata.csv"
    b8 = pd.read_csv(b7)
    b8.describe()
    b8 = b8.iloc[:, 1:]
    plt.plot(b8)
    b9 = b8.iloc[0].tolist()
    plt.plot(b9)
    plt.show()
    b10 = False
    while not b10:
        b4 = float(input("Enter the b4 b6 for calculation: "))
        b5 = fonk2(b9, b4)
        plt.clf()
        plt.plot(b5, b11 = 'red', linewidth=4)
        plt.plot(b9, b11 = 'olive', linewidth=2)
        plt.show()
        b10 = input("Are you happy with the result? (yes/no)").lower() == 'yes'
    b12 = b4 * b9[7] + (1 - b4) * b5[7]
    print("Prediction for next month is:", b12)
    fonk1(range(len(b9)), b9)
    print("Done")
if b13 = = "__main__":
    fonk3()