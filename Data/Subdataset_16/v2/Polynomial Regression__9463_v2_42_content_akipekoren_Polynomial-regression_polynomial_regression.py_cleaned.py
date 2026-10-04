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
def fonk3(x, y):
    b8 = sorted(zip(x, y))
    sorted_x, b9 = zip(*b8)
    return np.array(sorted_x), np.array(b9)
def fonk4(b16, b14, ridge, y):
    b10 = np.dot(b16.T, b16)
    b11 = ridge * b14
    b12 = np.linalg.inv(b10 + b11)
    b13 = np.dot(b16.T, y)
    return np.dot(b12, b13)
def fonk5(x, degree):
    b14 = np.identity(degree + 1)
    b15 = np.ones(len(x))
    b16 = np.column_stack([np.power(x, i) for i in range(degree + 1)])
    return b16, b14
def fonk6(b5, b7):
    a1 = 7
    b17 = []
    b18 = []
    for complexity in range(1, a1):
        b16, b14 = fonk5(b5, complexity)
        b19 = fonk4(b16, b14, ridge=0.00001, y=b7)
        b20 = np.polyval(b19[::-1], b5)
        plt.scatter(b5, b7)
        plt.plot(b5, b20, b21 = 'red')
        plt.show()
        b18.append(fonk7(b7, b20))
        b17.append(b20)
    return b18
def fonk7(y_true, b20):
    return np.sqrt(np.mean((y_true - b20) ** 2))
def fonk8(b18, b21):
    plt.title("Root Mean Square Error of Train and Test Data")
    plt.xlabel("Complexity")
    plt.ylabel("RMSE score")
    plt.ylim([0, 1])
    plt.plot(range(len(b18)), b18, b21 = b21)
    plt.show()
if b22 = = "__main__":
    b5, b6, b7, b4 = fonk1()
    b5, b7 = fonk3(b5, b7)
    b18 = fonk6(b5, b7)
    print(b18)