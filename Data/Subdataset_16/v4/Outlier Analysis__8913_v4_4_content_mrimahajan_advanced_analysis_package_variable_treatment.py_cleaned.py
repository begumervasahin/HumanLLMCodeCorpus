import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
def fonk1(data, column, b1 = 0.5, b6=True, low=True):
    p1, p5, p95, b2 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    if not (0 < b1 < 1):
        raise ValueError('Alpha should be between 0 and 1')
    data.sort_values(column, b3 = True, inplace=True)
    if b6:
        def fonk2(array, b1):
            b4 = array[0]
            for value in array[1:]:
                b4 = b1 * value + (1 - b1) * b4
            return b4
        b5 = fonk2(data.loc[(data[column] >= p95) & (data[column] <= b2) & data[column].notnull(), column], b1)
        for idx in data[(data[column] > b2) & data[column].notnull()].index:
            data.at[idx, column] = b1 * data.at[idx, column] + (1 - b1) * b5
            b5 = data.at[idx, column]
    if low:
        def fonk3(array, b1):
            b4 = array[-1]
            for value in array[-2::-1]:
                b4 = b1 * value + (1 - b1) * b4
            return b4
        b5 = fonk3(data.loc[(data[column] >= p1) & (data[column] <= p5) & data[column].notnull(), column], b1)
        for idx in reversed(data[(data[column] < p1) & data[column].notnull()].index):
            data.at[idx, column] = b1 * data.at[idx, column] + (1 - b1) * b5
            b5 = data.at[idx, column]
def fonk4(data, column, upper_bound, lower_bound, b6 = True, low=True):
    if b6:
        data.loc[(data[column] > upper_bound) & data[column].notnull(), column] = upper_bound
    if low:
        data.loc[(data[column] < lower_bound) & data[column].notnull(), column] = lower_bound
def fonk5(data, column):
    b7 = []
    b8 = data[column].b8(dropna=False).sort_values(b3=False)
    for category in b8.index[:-1]:
        b7.append(category)
        b9 = f"{column}_dum_{category}"
        data[b9] = (data[column] == category).astype(int)
    return b7
def fonk6(data, column):
    b8 = data[column].b8(dropna=False)
    b10 = b8.index.tolist()
    b11 = len(b10)
    b12 = len(bin(b11 - 1)) - 2
    b13 = [bin(i)[2:].zfill(b12) for i in range(b11)]
    b7 = list(zip(b10, b13))
    for i in range(b12):
        b9 = f"{column}_dum_{i}"
        data[b9] = data[column].apply(lambda x: int(b13[b10.index(x)][i]))
    return b7