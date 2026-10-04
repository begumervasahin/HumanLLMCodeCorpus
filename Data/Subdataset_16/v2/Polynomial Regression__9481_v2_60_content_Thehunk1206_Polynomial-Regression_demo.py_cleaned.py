import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
def fonk1():
    b1 = pd.read_csv('CleanData.csv')
    b1.drop(['Unnamed: 0'], b2 = 1, b3=True)
    b1.drop(b1.index[[0, 1, 5, 9, 73, 74, 75, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]], b3 = True)
    print(b1.info())
    print(b1.describe())
    b4 = b1['Decimal Date'].values
    b5 = b1['Seasonally Adjusted CO2 (ppm)'].values
    x_train, b6 = b4[:600], b4[601:703]
    a_train, b7 = b5[:600], b5[601:703]
    a1 = 2
    b8 = time.time()
    b9 = np.polyfit(x_train, a_train, a1)
    print("Polynomial Coefficients:", b9.tolist())
    b10 = np.polyval(b9, x_train)
    plt.figure()
    plt.scatter(x_train, a_train, b11 = 'red', label='Seasonally Adjusted CO2 (ppm)')
    plt.plot(x_train, b10, b11 = 'blue', label='Regression Line')
    plt.legend(b12 = 'upper left')
    b13 = np.mean((a_train - b10) ** 2)
    print("================== b20 During b14 = =====================")
    print("b15 = ", b13)
    b16 = np.polyval(b9, b6)
    b17 = np.mean((b7 - b16) ** 2)
    b18 = time.time()
    print("========================================================")
    print("Approx execution time: ", b18 - b8, " seconds")
    print("================== b19 = ==========================")
    for year, pred in zip(b6, b16):
        print(f"Predicted value of CO2 (in ppm) for Year {year}: {pred}")
    print("================== b19 b20 = =====================")
    print("b15 for b19 = ", b17)
    plt.show()
if b21 = = "__main__":
    fonk1()