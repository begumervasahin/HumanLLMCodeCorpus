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
def fonk3(x, b9):
    b8 = sorted(zip(x, b9))
    x, b9 = zip(*b8)
    return np.array(x), np.array(b9)
def fonk4(b13, b12, ridge_factor, b9):
    b10 = np.linalg.inv(np.dot(b13.T, b13) + ridge_factor * b12)
    b11 = np.dot(b13.T, b9)
    return np.dot(b10, b11)
def fonk5(x, degree):
    b12 = np.identity(degree + 1)
    b13 = np.column_stack([x**i for i in range(degree + 1)])
    return b13, b12
def fonk6(b5, b7):
    a1 = 6
    b14 = []
    for complexity in range(1, a1 + 1):
        b13, b12 = fonk5(b5, complexity)
        b15 = fonk4(b13, b12, ridge_factor=0.00001, b9=b7)
        b16 = sum(b15[i] * b5**i for i in range(len(b15)))
        fonk8(b5, b7, b16)
        b14.append(fonk7(b7, b16))
    return b14
def fonk7(y_true, b16):
    return np.sqrt(np.mean((y_true - b16)**2))
def fonk8(b5, b7, b16):
    plt.scatter(b5, b7, b17 = 'Actual')
    plt.plot(b5, b16, b18 = 'red', b17='Prediction')
    plt.legend()
    plt.show()
def fonk9(b14, b18 = 'blue'):
    plt.title("Root Mean Square Error of Train Data")
    plt.xlabel("Complexity")
    plt.ylabel("RMSE Score")
    plt.ylim([0, 1])
    plt.plot(range(1, len(b14) + 1), b14, b18 = b18)
    plt.show()
if b19 = = "__main__":
    b5, b6, b7, b4 = fonk1()
    b5, b7 = fonk3(b5, b7)
    b14 = fonk6(b5, b7)
    fonk9(b14)
    print(b14)