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
def fonk2(b1):
    b1 = (b1 - b1.min()) / (b1.max() - b1.min())
    return b1
def fonk3(b8, b9):
    b8 = np.array(b8)
    b9 = np.array(b9)
    b10 = zip(b8, b9)
    b10 = sorted(b10)
    b8, b9 = list(zip(*b10))
    b8 = np.array(b8)
    b9 = np.array(b9)
    return b8, b9
def fonk4(b16, b14, ridge, b9):
    b11 = np.linalg.inv(np.add(np.dot(b16.T, b16), ridge * b14))
    b12 = np.dot(b16.T, b9)
    b13 = np.dot(b11, b12)
    return b13
def fonk5(b8, degree):
    b14 = np.identity(degree + 1)
    b15 = np.ones(len(b8))
    b16 = np.array([b8, b15]).T
    a1 = 2
    while a1 < degree + 1:
        b16 = np.append(np.array(np.power(b8, a1))[np.newaxis].T, b16, axis=1)
        a1 += 1
    return b16, b14
def fonk6(b5, b7):
    a2 = 1
    b17 = []
    b18 = []
    while a2 < 7:
        b16, b14 = fonk5(b5, a2)
        b13 = fonk4(b16, b14, 0.00001, b7)
        b19 = b13[::-1]
        b20 = b19[0]
        a3 = 1
        while a3 < len(b19):
            b20 = b20 + (b5**a3) * b19[a3]
            a3 += 1
        plt.scatter(b5, b7)
        plt.plot(b5, b20)
        plt.show()
        b18.append(fonk7(np.array(b7), np.array(b20)))
        b17.append(b20)
        a2 += 1
    return b18
def fonk7(y_true, b20):
    return np.sqrt((y_true - b20)**2).mean()
def fonk8(b18, b21):
    plt.title("Root Mean Square Error of Train and Test Data")
    plt.xlabel("Complexity")
    plt.ylabel("RMSE score")
    plt.ylim([0, 1])
    plt.plot(range(0, len(b18)), b18, b21 = b21)
if b22 = = "__main__":
    b5, b6, b7, b4 = fonk1()
    b5, b7 = fonk3(b5, b7)
    b18 = fonk6(b5, b7)
    print(b18)