import numpy as np
from numpy.polynomial.polynomial import Polynomial
import pandas as pd
import matplotlib.pyplot as plt
import time
def fonk1():
    b1 = pd.read_csv('CleanData.csv')
    b1.drop(['Unnamed: 0'], b2 = 1, b3=True)
    b1.drop(b1.index[[0, 1, 5, 9, 73, 74, 75, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]], b3 = True)
    print(b1.info())
    print(b1.describe())
    b4 = plt.figure()
    b5 = b4.add_subplot(1, 1, 1)
    b6 = b1['Decimal Date'].tolist()
    b7 = b1['Seasonally Adjusted CO2 (ppm)'].tolist()
    b8 = b6[0:600]
    b9 = b7[0:600]
    b10 = b6[601:703]
    b11 = b7[601:703]
    a1 = 2
    b12 = time.time()
    b13 = np.polyfit(b8, b9, a1)
    b14 = b13.tolist()
    print(b14)
    b15 = np.polyval(b13, b8)
    b5.scatter(b8, b9, b16 = 'red', label='Seasonally Adjusted CO2 (ppm)')
    b5.plot(b8, b15, b16 = 'blue', label='Regression Line')
    b5.legend(b17 = 'upper left')
    b18 = np.mean((b9 - b15) ** 2)
    print("==================b25 During b19 = ======================")
    print("b20 = ", b18)
    b21 = np.polyval(b13, b10)
    b22 = np.mean((b11 - b21) ** 2)
    b23 = time.time()
    print("========================================================")
    print("Approx execution time: ", b23 - b12, "Seconds")
    print("==================b24 = ==========================")
    for i in range(len(b10)):
        print(f"Predicted value of CO2 (in ppm) for Year: {b10[i]} is {b21[i]}")
    print("==================b24 b25 = ======================")
    print("b20 FOR b24 = ", b22)
    plt.show()
if b26 = = "__main__":
    fonk1()