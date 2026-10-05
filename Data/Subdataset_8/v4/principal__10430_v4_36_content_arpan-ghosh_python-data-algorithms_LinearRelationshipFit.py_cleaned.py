import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from scipy.stats import linregress
colnames = ['x', 'y']
bfit = pd.read_csv('/home/idies/workspace/AS.171.205/data/bfit.csv', names=colnames, header=None)
cfit = pd.read_csv('/home/idies/workspace/AS.171.205/data/cfit.csv', names=colnames, header=None)
dfit = pd.read_csv('/home/idies/workspace/AS.171.205/data/dfit.csv', names=colnames, header=None)
efit = pd.read_csv('/home/idies/workspace/AS.171.205/data/efit.csv', names=colnames, header=None)
plt.figure(figsize=(12, 8))
fig, axs = plt.subplots(1, 4, sharey=True)
datasets = [bfit, cfit, dfit, efit]
titles = ["bfit.csv Scatter", "cfit.csv Scatter", "dfit.csv Scatter", "efit.csv Scatter"]
for i, data in enumerate(datasets):
    data.plot(kind='scatter', x='x', y='y', ax=axs[i], figsize=(16, 8))
    axs[i].set_title(titles[i])
    axs[i].set_xlabel("x")
    axs[i].set_ylabel("y")
plt.show()
def fit_polynomial(data, degree):
    coefficients = np.polyfit(data['x'], data['y'], degree)
    return coefficients
def calculate_r_squared(data, coefficients):
    yfit = np.polyval(coefficients, data['x'])
    yresid = data['y'] - yfit
    SSresid = np.sum(np.power(yresid, 2))
    SStotal = len(data['y']) * np.var(data['y'])
    rsq = 1 - SSresid / SStotal
    return rsq
datasets = [bfit, cfit, dfit, efit]
for i, data in enumerate(datasets):
    print(f"Dataset {chr(ord('a') + i)}.csv:")
    for degree in range(1, 4):
        coefficients = fit_polynomial(data, degree)
        rsquared = calculate_r_squared(data, coefficients)
        print(f"Polynomial degree {degree} coefficients:", coefficients)
        print("R-squared value:", rsquared)
        slope, intercept, r_value, p_value, std_err = linregress(data['x'], data['y'])
        print("R-squared value (scipy method):", r_value ** 2)
        print("P-value:", p_value)
        print()
    print("--------------------------------------------------")