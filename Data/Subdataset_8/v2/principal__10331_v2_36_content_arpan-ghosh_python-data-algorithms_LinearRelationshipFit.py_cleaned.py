import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
data_files = [
    '/home/idies/workspace/AS.171.205/data/bfit.csv',
    '/home/idies/workspace/AS.171.205/data/cfit.csv',
    '/home/idies/workspace/AS.171.205/data/dfit.csv',
    '/home/idies/workspace/AS.171.205/data/efit.csv'
]
datasets = [pd.read_csv(file, names=['x', 'y'], header=None) for file in data_files]
for i, dataset in enumerate(datasets):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(dataset['x'], dataset['y'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Scatter Plot of {data_files[i]}')
    plt.subplot(1, 2, 2)
    plt.scatter(dataset['x'], dataset['y'])
    p1 = np.polyfit(dataset['x'], dataset['y'], 1)
    plt.plot(dataset['x'], np.polyval(p1, dataset['x']), 'r-', label='Linear Fit')
    p2 = np.polyfit(dataset['x'], dataset['y'], 2)
    plt.plot(dataset['x'], np.polyval(p2, dataset['x']), 'b--', label='Quadratic Fit')
    p3 = np.polyfit(dataset['x'], dataset['y'], 3)
    plt.plot(dataset['x'], np.polyval(p3, dataset['x']), 'm:', label='Cubic Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Polynomial Fits of {data_files[i]}')
    plt.legend()
    yfit = np.polyval(p1, dataset['x'])
    yresid = dataset['y'] - yfit
    SSresid = sum(pow(yresid, 2))
    SStotal = len(dataset['y']) * np.var(dataset['y'])
    rsq = 1 - SSresid / SStotal
    print(f'R-squared (computed with numpy) for {data_files[i]}: {rsq}')
    slope, intercept, r_value, p_value, std_err = linregress(dataset['x'], dataset['y'])
    print(f'R-squared (computed with scipy) for {data_files[i]}: {r_value**2}')
    print(f'p-value for {data_files[i]}: {p_value}')
    plt.show()