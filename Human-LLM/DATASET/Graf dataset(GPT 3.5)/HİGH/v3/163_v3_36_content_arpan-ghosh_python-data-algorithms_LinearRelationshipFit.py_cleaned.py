import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
def fonk1(file_paths):
    b1 = []
    for file_path in file_paths:
        b2 = pd.read_csv(file_path, names=['x', 'y'], header=None)
        b1.append(b2)
    return b1
def fonk2(b2, filename):
    fig, b3 = plt.subplots(1, 2, figsize=(12, 4))
    b3[0].scatter(b2['x'], b2['y'])
    b3[0].set_xlabel('x')
    b3[0].set_ylabel('y')
    b3[0].set_title(f'Scatter Plot of {filename}')
    b3[1].scatter(b2['x'], b2['y'])
    for degree, style in zip([1, 2, 3], ['r-', 'b--', 'm:']):
        b4 = np.polyfit(b2['x'], b2['y'], degree)
        b5 = np.polyval(b4, b2['x'])
        b3[1].plot(b2['x'], b5, style, b6 = f'Degree {degree} Fit')
    b3[1].set_xlabel('x')
    b3[1].set_ylabel('y')
    b3[1].set_title(f'Polynomial Fits of {filename}')
    b3[1].legend()
    b7 = b2['y'] - np.polyval(b4, b2['x'])
    b8 = sum(b7 ** 2)
    b9 = len(b2['y']) * np.var(b2['y'])
    b10 = 1 - b8 / b9
    print(f'R-squared (computed with numpy) for {filename}: {b10}')
    slope, intercept, r_value, p_value, b11 = linregress(b2['x'], b2['y'])
    print(f'R-squared (computed with scipy) for {filename}: {r_value ** 2}')
    print(f'p-value for {filename}: {p_value}')
    plt.show()
b12 = [
    '/home/idies/workspace/AS.171.205/data/bfit.csv',
    '/home/idies/workspace/AS.171.205/data/cfit.csv',
    '/home/idies/workspace/AS.171.205/data/dfit.csv',
    '/home/idies/workspace/AS.171.205/data/efit.csv'
]
b1 = fonk1(b12)
for b2, filename in zip(b1, b12):
    fonk2(b2, filename)