import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
def fonk1(file_path):
    b1 = ['x', 'y']
    return pd.read_csv(file_path, b2 = b1, header=None)
def fonk2(b13, b12):
    fig, b3 = plt.subplots(1, len(b13), figsize=(16, 8), sharey=True)
    for i, data in enumerate(b13):
        data.plot(b4 = 'scatter', x='x', y='y', ax=b3[i])
        b3[i].set_title(b12[i])
        b3[i].set_xlabel("x")
        b3[i].set_ylabel("y")
    plt.show()
def fonk3(data, degree):
    b5 = np.polyfit(data['x'], data['y'], degree)
    b6 = np.polyval(b5, data['x'])
    b7 = data['y'] - b6
    b8 = np.sum(np.power(b7, 2))
    b9 = len(data['y']) * np.var(data['y'])
    b10 = 1 - b8 / b9
    return b5, b10
def fonk4(b14, degree, b5, b15, r_value, p_value):
    print(f"Dataset {b14}.csv:")
    print(f"Polynomial degree {degree} b5:", b5)
    print("R-squared value (from polynomial fitting):", b15)
    print("R-squared value (scipy method):", r_value ** 2)
    print("P-value:", p_value)
    print("--------------------------------------------------")
b11 = ['/home/idies/workspace/AS.171.205/data/bfit.csv',
              '/home/idies/workspace/AS.171.205/data/cfit.csv',
              '/home/idies/workspace/AS.171.205/data/dfit.csv',
              '/home/idies/workspace/AS.171.205/data/efit.csv']
b12 = ["bfit.csv Scatter", "cfit.csv Scatter", "dfit.csv Scatter", "efit.csv Scatter"]
b13 = [fonk1(path) for path in b11]
fonk2(b13, b12)
for i, data in enumerate(b13):
    b14 = chr(ord('a') + i)
    for degree in range(1, 4):
        b5, b15 = fonk3(data, degree)
        slope, intercept, r_value, p_value, b16 = linregress(data['x'], data['y'])
        fonk4(b14, degree, b5, b15, r_value, p_value)