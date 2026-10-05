import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def fonk1(data, column, b1 = 0.5, smooth_high=True, smooth_low=True):
    b2 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    p1, p5, p95, b3 = b2[0.01], b2[0.05], b2[0.95], b2[0.99]
    if not 0 < b1 < 1:
        raise ValueError('Alpha should be between 0 and 1')
    data.sort_values(column, b4 = True, inplace=True)
    if smooth_high:
        b5 = data.loc[(p95 >= data[column]) & (data[column] <= b3) & (data[column].notnull()), column].mean()
        for i in data[(b3 < data[column]) & (data[column].notnull())].index:
            data.loc[i, column] = b1 * data.loc[i, column] + (1 - b1) * b5
            b5 = data.loc[i, column]
    if smooth_low:
        b5 = data.loc[(p1 <= data[column]) & (data[column] <= p5) & (data[column].notnull()), column].mean()
        for i in data[(p1 > data[column]) & (data[column].notnull())].index[::-1]:
            data.loc[i, column] = b1 * data.loc[i, column] + (1 - b1) * b5
            b5 = data.loc[i, column]
def fonk2(data, column, upper_bound, lower_bound, b6 = True, floor_low=True):
    if b6:
        data.loc[(data[column] > upper_bound) & (data[column].notnull()), column] = upper_bound
    if floor_low:
        data.loc[(data[column] < lower_bound) & (data[column].notnull()), column] = lower_bound
def fonk3(data, column):
    b7 = []
    b8 = data[column].b8(dropna=False).sort_values(b4=False)
    for category in b8.index[:-1]:
        b7.append(category)
        data[column + '_dum_' + str(category)] = (data[column] == category).astype(int)
    return b7
def fonk4(data, column):
    b8 = data[column].b8(dropna=False).sort_index()
    b9 = b8.index.tolist()
    b10 = len(b9)
    b11 = len(str(b10))
    b12 = [int(bin(i)[2:]) for i in range(b10)]
    b13 = [(cat, bin_val) for cat, bin_val in zip(b9, b12)]
    for j in range(b11):
        data[column + '_dum_' + str(j)] = 0
        for i, (_, bin_val) in enumerate(b13):
            data.loc[data[column] == b9[i], column + '_dum_' + str(j)] = bin_val % 10
            b12[i] = bin_val
    return b13