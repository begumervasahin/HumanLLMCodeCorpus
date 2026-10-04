import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
def fonk1():
    b1 = pd.read_csv("kc_house_data.csv")
    b2 = b1["sqft_living"]
    b3 = b1["price"]
    b5, b6, b7, b4 = train_test_split(b2, b3, test_size=0.3, random_state=42)
    b5 = fonk2(b5)
    b6 = fonk2(b6)
    b7 = fonk2(b7)
    b4 = fonk2(b4)
    return b5, b6, b7, b4
def fonk2(series):
    return (series - series.min()) / (series.max() - series.min())
def fonk3(b8, b9):
    b8 = np.array(b8)
    b9 = np.array(b9)
    b10 = sorted(zip(b8, b9))
    b8, b9 = zip(*b10)
    return np.array(b8), np.array(b9)
def fonk4(b14, b13, ridge_factor, b9):
    b11 = np.linalg.inv(np.dot(b14.T, b14) + ridge_factor * b13)
    b12 = np.dot(b14.T, b9)
    return np.dot(b11, b12)
def fonk5(b8, degree):
    b13 = np.identity(degree + 1)
    b14 = np.column_stack([b8**i for i in range(degree + 1)])
    return b14, b13
def fonk6(b5, b7):
    a1 = 6
    b15 = []
    b16 = []
    for complexity in range(1, a1 + 1):
        b14, b13 = fonk5(b5, complexity)
        b17 = fonk4(b14, b13, ridge_factor=0.00001, b9=b7)
        b18 = sum(b17[i] * b5**i for i in range(len(b17)))
        plt.scatter(b5, b7)
        plt.plot(b5, b18)
        plt.show()
        b16.append(fonk7(b7, b18))
        b15.append(b18)
    return b16
def fonk7(y_true, b18):
    return np.sqrt(np.mean((y_true - b18)**2))
def fonk8(b16, b19):
    plt.title("Root Mean Square Error of Train and Test Data")
    plt.xlabel("Complexity")
    plt.ylabel("RMSE Score")
    plt.ylim([0, 1])
    plt.plot(range(1, len(b16) + 1), b16, b19 = b19)
    plt.show()
if b20 = = "__main__":
    b5, b6, b7, b4 = fonk1()
    b5, b7 = fonk3(b5, b7)
    b16 = fonk6(b5, b7)
    print(b16)