import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
def fonk1(filename):
    return pd.read_csv(filename)
def fonk2(b7, b8):
    return np.polyfit(b7, b8, 3)
def fonk3(b7, b8, b10, a, b, c, b9):
    plt.scatter(b7, b8)
    plt.plot(b10, a*(b10**3) + b*(b10**2) + c*b10 + b9)
    plt.xlabel('Square Meter')
    plt.ylabel('Price')
    plt.title('House Price Prediction')
    plt.show()
def fonk4(message):
    print(message)
    return float(input())
def fonk5(b11, a, b, c, b9):
    return a*(b11**3) + b*(b11**2) + c*b11 + b9
def fonk6(b15, a, b, c, b9):
    b4, b1 = 0, 1000
    while b4 <= b1:
        b2 = (b4 + b1) / 2
        b3 = a*(b2**3) + b*(b2**2) + c*b2 + b9
        if b3 < b15:
            b4 = b2 + 0.001
        elif b3 > b15:
            b1 = b2 - 0.001
        else:
            return b2
    return None
def fonk7(b5, end_time):
    return end_time - b5
b5 = time.time()
b6 = fonk1("housePriceDataset.csv")
b7 = np.array(b6["squareMeter"])
b8 = np.array(b6["b8"])
a, b, c, b9 = fonk2(b7, b8)
b10 = np.arange(150)
fonk3(b7, b8, b10, a, b, c, b9)
b11 = fonk4("Please, enter square meter (m2): ")
b12 = time.time()
b13 = fonk5(b11, a, b, c, b9)
print("House Price b14 = > $" + str(b13))
b15 = fonk4("Please, enter house b8 ($): ")
b16 = time.time()
b17 = fonk6(b15, a, b, c, b9)
if b17 is not None:
    print("Square Meter (m2) b14 = > " + str(b17) + " m2")
else:
    print("Square meter not found for the given house b8.")
b18 = fonk7(b5, time.time())
print("{} Seconds".format(b18))