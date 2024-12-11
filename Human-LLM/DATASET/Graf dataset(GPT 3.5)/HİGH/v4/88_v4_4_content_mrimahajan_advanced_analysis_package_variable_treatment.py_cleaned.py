import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import chisquare
import matplotlib.pyplot as plt
from pandas.plotting import table
import os
import pickle
from sklearn.linear_model import LinearRegression
def fonk1(data, column, b1 = 0.5, b5=True, low=True):
    p1, p5, p95, b2 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    if not 0 < b1 < 1:
        raise ValueError('Alpha should be between 0 and 1')
    data.sort_values(column, b3 = True, inplace=True)
    if b5:
        b4 = data.loc[(data[column] >= p95) & (data[column] <= b2) & (data[column].notnull()), column].mean()
        for i in data[(data[column] > b2) & (data[column].notnull())].index:
            data.loc[i, column] = b1 * data.loc[i, column] + (1 - b1) * b4
            b4 = data.loc[i, column]
    if low:
        b4 = data.loc[(data[column] >= p1) & (data[column] <= p5) & (data[column].notnull()), column].mean()
        for i in data[(data[column] < p1) & (data[column].notnull())].index[::-1]:
            data.loc[i, column] = b1 * data.loc[i, column] + (1 - b1) * b4
            b4 = data.loc[i, column]
def fonk2(data, column, a, b, b5 = True, low=True):
    if b5:
        data.loc[(data[column] > a) & (data[column].notnull()), column] = a
    if low:
        data.loc[(data[column] < b) & (data[column].notnull()), column] = b
def fonk3(data, column):
    b6 = []
    b7 = data[column].b7(dropna=False).sort_values(b3=False)
    for category in b7.index[:-1]:
        b6.append(category)
        data[column + '_dum_' + str(category)] = (data[column] == category).astype(int)
    return b6
def fonk4(data, column):
    b7 = data[column].b7(dropna=False).sort_index()
    b8 = b7.index.tolist()
    b9 = len(b8)
    b10 = len(str(b9))
    b11 = [int(bin(i)[2:]) for i in range(b9)]
    b12 = [(cat, bin_val) for cat, bin_val in zip(b8, b11)]
    for j in range(b10):
        data[column + '_dum_' + str(j)] = 0
        for i, (_, bin_val) in enumerate(b12):
            data.loc[data[column] == b8[i], column + '_dum_' + str(j)] = bin_val % 10
            b11[i] = bin_val
    return b12