import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
def fonk1(filename):
    b1 = pd.read_csv(filename)
    return b1["squareMeter"].values, b1["b9"].values
def fonk2(x, y, b2 = 3):
    b3 = np.polyfit(x, y, b2)
    b4 = np.arange(150)
    b5 = np.poly1d(b3)
    plt.scatter(x, y, b6 = "Original Data")
    plt.plot(b4, b5(b4), b7 = 'red', b6="Polynomial Curve")
    plt.xlabel("Square Meter")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
def fonk3(square_meter, b3):
    return np.polyval(b3, square_meter)
def fonk4(b13, b3):
    for i in np.arange(0, 1000, 0.001):
        if np.polyval(b3, i) >= b13:
            return i
def fonk5():
    b8 = time.time()
    square_meter, b9 = fonk1("housePriceDataset.csv")
    fonk2(square_meter, b9)
    b10 = float(input("Please, enter square meter (m2): "))
    b11 = fonk3(b10, np.polyfit(square_meter, b9, 3))
    print("House Price b12 = > ${:.2f}".format(b11))
    b13 = float(input("Please, enter house b9 ($): "))
    b14 = fonk4(b13, np.polyfit(square_meter, b9, 3))
    print("Square Meter (m2) b12 = > {:.2f}m2".format(b14))
    print("Total Execution Time: {:.4f} Seconds".format(time.time() - b8))
if b15 = = "__main__":
    fonk5()