import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from scipy.stats import linregress
b1 = ['x', 'y']
b2 = pd.read_csv('/home/idies/workspace/AS.171.205/data/b2.csv', names=b1, header=None)
b3 = pd.read_csv('/home/idies/workspace/AS.171.205/data/b3.csv', names=b1, header=None)
b4 = pd.read_csv('/home/idies/workspace/AS.171.205/data/b4.csv', names=b1, header=None)
b5 = pd.read_csv('/home/idies/workspace/AS.171.205/data/b5.csv', names=b1, header=None)
plt.figure(b6 = (12, 8))
fig, b7 = plt.subplots(1, 4, sharey=True)
b8 = [b2, b3, b4, b5]
b9 = ["b2.csv Scatter", "b3.csv Scatter", "b4.csv Scatter", "b5.csv Scatter"]
for i, data in enumerate(b8):
    data.plot(b10 = 'scatter', x='x', y='y', ax=b7[i], b6=(16, 8))
    b7[i].set_title(b9[i])
    b7[i].set_xlabel("x")
    b7[i].set_ylabel("y")
plt.show()
def fonk1(data, degree):
    b11 = np.polyfit(data['x'], data['y'], degree)
    return b11
def fonk2(data, b11):
    b12 = np.polyval(b11, data['x'])
    b13 = data['y'] - b12
    b14 = np.sum(np.power(b13, 2))
    b15 = len(data['y']) * np.var(data['y'])
    b16 = 1 - b14 / b15
    return b16
b8 = [b2, b3, b4, b5]
for i, data in enumerate(b8):
    print(f"Dataset {chr(ord('a') + i)}.csv:")
    for degree in range(1, 4):
        b11 = fonk1(data, degree)
        b17 = fonk2(data, b11)
        print(f"Polynomial degree {degree} b11:", b11)
        print("R-squared value:", b17)
        slope, intercept, r_value, p_value, b18 = linregress(data['x'], data['y'])
        print("R-squared value (scipy method):", r_value ** 2)
        print("P-value:", p_value)
        print()
    print("--------------------------------------------------")