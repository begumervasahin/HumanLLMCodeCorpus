import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
b1 = ['/home/idies/workspace/AS.171.205/data/bfit.csv',
              '/home/idies/workspace/AS.171.205/data/cfit.csv',
              '/home/idies/workspace/AS.171.205/data/dfit.csv',
              '/home/idies/workspace/AS.171.205/data/efit.csv']
b2 = [pd.read_csv(file, names=['x', 'y'], header=None) for file in b1]
for i, dataset in enumerate(b2):
    plt.figure(b3 = (12, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(dataset['x'], dataset['y'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{b1[i]} Scatter')
    plt.subplot(1, 2, 2)
    plt.scatter(dataset['x'], dataset['y'])
    b4 = np.polyfit(dataset['x'], dataset['y'], 1)
    plt.plot(dataset['x'], np.polyval(b4, dataset['x']), 'r-', b5 = 'Linear Fit')
    b6 = np.polyfit(dataset['x'], dataset['y'], 2)
    plt.plot(dataset['x'], np.polyval(b6, dataset['x']), 'b--', b5 = 'Quadratic Fit')
    b7 = np.polyfit(dataset['x'], dataset['y'], 3)
    plt.plot(dataset['x'], np.polyval(b7, dataset['x']), 'm:', b5 = 'Cubic Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{b1[i]} Polynomial Fits')
    plt.legend()
    b8 = np.polyval(b4, dataset['x'])
    b9 = dataset['y'] - b8
    b10 = sum(pow(b9, 2))
    b11 = len(dataset['y']) * np.var(dataset['y'])
    b12 = 1 - b10 / b11
    print(f'R-squared (using numpy) for {b1[i]}: {b12}')
    slope, intercept, r_value, p_value, b13 = linregress(dataset['x'], dataset['y'])
    print(f'R-squared (using scipy) for {b1[i]}: {r_value**2}')
    print(f'p-value for {b1[i]}: {p_value}')
    plt.show()