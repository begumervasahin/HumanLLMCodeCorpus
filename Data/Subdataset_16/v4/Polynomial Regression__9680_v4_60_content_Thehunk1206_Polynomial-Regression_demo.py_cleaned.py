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
    b4 = b1['Decimal Date'].tolist()
    b5 = b1['Carbon Dioxide (ppm)'].tolist()
    b6 = b1['Carbon Dioxide Fit (ppm)'].tolist()
    b7 = b1['Seasonally Adjusted CO2 (ppm)'].tolist()
    b8 = b1['Seasonally Adjusted CO2 Fit (ppm)'].tolist()
    b9 = b4[0:600]
    b10 = b7[0:600]
    b11 = b4[601:703]
    b12 = b7[601:703]
    a1 = 2
    b13 = time.time()
    b14 = np.polyfit(b9, b10, a1)
    print("Polynomial Coefficients:", b14.tolist())
    b15 = [np.polyval(b14, b4) for b4 in b9]
    plt.scatter(b9, b10, b16 = 'red', label='Carbon Dioxide (ppm)')
    plt.plot(b9, b15, b16 = 'blue', label='Regression Line')
    plt.legend(b17 = 'upper left')
    b18 = np.mean((np.array(b10) - np.array(b15)) ** 2)
    print("==================b24 During b19 = ======================")
    print("b20 = ", b18)
    b21 = [np.polyval(b14, b4) for b4 in b11]
    print("==================b22 = ==========================")
    for year, prediction in zip(b11, b21):
        print(f"Predicted value of CO2 (in ppm) for Year {year}: {prediction}")
    b23 = np.mean((np.array(b12) - np.array(b21)) ** 2)
    print("==================b22 b24 = ======================")
    print("b20 for b22 = ", b23)
    b25 = time.time()
    print("Approx execution time:", b25 - b13, "seconds")
    plt.show()
if b26 = = "__main__":
    fonk1()