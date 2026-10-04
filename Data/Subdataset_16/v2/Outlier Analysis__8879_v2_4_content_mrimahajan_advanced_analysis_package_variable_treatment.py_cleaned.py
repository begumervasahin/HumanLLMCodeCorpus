import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import chisquare
from matplotlib import pyplot as plt
import os
import pickle
from sklearn.linear_model import LinearRegression
def fonk1(data, column, b1 = 0.5, b6=True, low=True):
    if not 0 < b1 < 1:
        raise ValueError('b1 should be between 0 and 1')
    p1, p5, p95, b2 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    data.sort_values(column, b3 = True, inplace=True)
    if b6:
        b4 = fonk2(data.loc[(data[column] >= p95) & (data[column] <= b2) & (data[column].notnull()), column], b1)
        for i in data[(data[column] > b2) & (data[column].notnull())].index:
            data.at[i, column] = b1 * data.at[i, column] + (1 - b1) * b4
            b4 = data.at[i, column]
    if low:
        b4 = fonk3(data.loc[(data[column] >= p1) & (data[column] <= p5) & (data[column].notnull()), column], b1)
        for i in data[(data[column] < p1) & (data[column].notnull())].index[::-1]:
            data.at[i, column] = b1 * data.at[i, column] + (1 - b1) * b4
            b4 = data.at[i, column]
def fonk2(array, b1):
    b5 = array[0]
    for value in array[1:]:
        b5 = b1 * value + (1 - b1) * b5
    return b5
def fonk3(array, b1):
    b5 = array[-1]
    for value in array[-2::-1]:
        b5 = b1 * value + (1 - b1) * b5
    return b5
def fonk4(data, column, upper, lower, b6 = True, low=True):
    if b6:
        data.loc[(data[column] > upper) & (data[column].notnull()), column] = upper
    if low:
        data.loc[(data[column] < lower) & (data[column].notnull()), column] = lower
def fonk5(data, column):
    b7 = data[column].value_counts(dropna=False).to_frame(name='counts').sort_values(by='counts', b3=False)
    b8 = b7.index[:-1].tolist()
    for category in b8:
        b9 = f"{column}_dum_{category}"
        data[b9] = (data[column] == category).astype(int)
    return b8
def fonk6(data, column):
    b7 = data[column].value_counts(dropna=False).to_frame(name='counts')
    b10 = b7.index.tolist()
    b11 = len(b10)
    b12 = len(bin(b11)[2:])
    b13 = [int(bin(i)[2:]) for i in range(b11)]
    b14 = list(zip(b10, b13))
    for j in range(b12):
        b9 = f"{column}_dum_{j}"
        data[b9] = 0
        for i, category in enumerate(b10):
            data.loc[data[column] == category, b9] = b13[i] % 10
            b13[i]
    return b14