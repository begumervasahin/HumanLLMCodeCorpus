import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
def fonk1(data, column, b1 = 0.5, b8=True, low=True):
    p1, p5, p95, b2 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    if not (0 < b1 < 1):
        raise ValueError('Alpha should be between 0 and 1')
    data.sort_values(column, b3 = True, inplace=True)
    if b8:
        def fonk2(array, b1):
            b4 = array[0]
            for value in array[1:]:
                b4 = b1 * value + (1 - b1) * b4
            return b4
        b5 = data.loc[(data[column] >= p95) & (data[column] <= b2) & data[column].notnull(), column]
        b6 = fonk2(b5, b1)
        for idx in data[(data[column] > b2) & data[column].notnull()].index:
            data.at[idx, column] = b1 * data.at[idx, column] + (1 - b1) * b6
            b6 = data.at[idx, column]
    if low:
        def fonk3(array, b1):
            b4 = array[-1]
            for value in array[-2::-1]:
                b4 = b1 * value + (1 - b1) * b4
            return b4
        b7 = data.loc[(data[column] >= p1) & (data[column] <= p5) & data[column].notnull(), column]
        b6 = fonk3(b7, b1)
        for idx in reversed(data[(data[column] < p1) & data[column].notnull()].index):
            data.at[idx, column] = b1 * data.at[idx, column] + (1 - b1) * b6
            b6 = data.at[idx, column]
def fonk4(data, column, upper_bound, lower_bound, b8 = True, low=True):
    if b8:
        data.loc[(data[column] > upper_bound) & data[column].notnull(), column] = upper_bound
    if low:
        data.loc[(data[column] < lower_bound) & data[column].notnull(), column] = lower_bound
def fonk5(data, column):
    b9 = []
    b10 = data[column].b10(dropna=False).sort_values(b3=False)
    for category in b10.index[:-1]:
        b9.append(category)
        b11 = f"{column}_dum_{category}"
        data[b11] = (data[column] == category).astype(int)
    return b9
def fonk6(data, column):
    b10 = data[column].b10(dropna=False)
    b12 = b10.index.tolist()
    b13 = len(b12)
    b14 = len(bin(b13 - 1)) - 2
    b15 = [bin(i)[2:].zfill(b14) for i in range(b13)]
    b9 = list(zip(b12, b15))
    for i in range(b14):
        b11 = f"{column}_dum_{i}"
        data[b11] = data[column].apply(lambda x: int(b15[b12.index(x)][i]))
    return b9