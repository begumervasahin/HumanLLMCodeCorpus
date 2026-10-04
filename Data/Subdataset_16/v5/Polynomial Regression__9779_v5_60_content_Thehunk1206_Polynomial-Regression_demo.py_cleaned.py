import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b1.drop(['Unnamed: 0'], b2 = 1, b4=True)
    b3 = [0, 1, 5, 9, 73, 74, 75, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]
    b1.drop(b1.index[b3], b4 = True)
    return b1
def fonk2(b5, b6, a1):
    return np.polyfit(b5, b6, a1)
def fonk3(actual, predicted):
    return np.mean((np.array(actual) - np.array(predicted)) ** 2)
def fonk4():
    b1 = fonk1('CleanData.csv')
    print(b1.info())
    print(b1.describe())
    b5 = b1['Decimal Date'].tolist()
    b6 = b1['Carbon Dioxide (ppm)'].tolist()
    b7 = b1['Seasonally Adjusted CO2 (ppm)'].tolist()
    b8 = b5[:600]
    b9 = b7[:600]
    b10 = b5[601:703]
    b11 = b7[601:703]
    a1 = 2
    b12 = time.time()
    b13 = fonk2(b8, b9, a1)
    print("Polynomial Coefficients:", b13.tolist())
    b14 = [np.polyval(b13, xi) for xi in b8]
    plt.scatter(b8, b9, b15 = 'red', label='Seasonally Adjusted CO2 (ppm)')
    plt.plot(b8, b14, b15 = 'blue', label='Regression Line')
    plt.legend(b16 = 'upper left')
    b17 = fonk3(b9, b14)
    print("==================b23 During b18 = ======================")
    print("b19 = ", b17)
    b20 = [np.polyval(b13, xi) for xi in b10]
    print("==================b21 = ==========================")
    for year, prediction in zip(b10, b20):
        print(f"Predicted value of CO2 (in ppm) for Year {year}: {prediction}")
    b22 = fonk3(b11, b20)
    print("==================b21 b23 = ======================")
    print("b19 for b21 = ", b22)
    b24 = time.time()
    print("Approx execution time:", b24 - b12, "seconds")
    plt.show()
if b25 = = "__main__":
    fonk4()