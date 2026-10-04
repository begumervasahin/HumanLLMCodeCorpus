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
def fonk1(data, column, b1 = 0.5, b7=True, low=True):
    if not 0 < b1 < 1:
        raise ValueError('b1 should be between 0 and 1')
    b2 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    p1, p5, p95, b3 = b2[0.01], b2[0.05], b2[0.95], b2[0.99]
    data.sort_values(column, b4 = True, inplace=True)
    if b7:
        b5 = fonk2(data.loc[(data[column] >= p95) & (data[column] <= b3) & (data[column].notnull()), column], b1)
        for i in data[(data[column] > b3) & (data[column].notnull())].index:
            data.at[i, column] = b1 * data.at[i, column] + (1 - b1) * b5
            b5 = data.at[i, column]
    if low:
        b5 = fonk3(data.loc[(data[column] >= p1) & (data[column] <= p5) & (data[column].notnull()), column], b1)
        for i in data[(data[column] < p1) & (data[column].notnull())].index[::-1]:
            data.at[i, column] = b1 * data.at[i, column] + (1 - b1) * b5
            b5 = data.at[i, column]
def fonk2(array, b1):
    b6 = array[0]
    for value in array[1:]:
        b6 = b1 * value + (1 - b1) * b6
    return b6
def fonk3(array, b1):
    b6 = array[-1]
    for value in array[-2::-1]:
        b6 = b1 * value + (1 - b1) * b6
    return b6
def fonk4(data, column, upper, lower, b7 = True, low=True):
    if b7:
        data.loc[(data[column] > upper) & (data[column].notnull()), column] = upper
    if low:
        data.loc[(data[column] < lower) & (data[column].notnull()), column] = lower
def fonk5(data, column):
    b8 = data[column].value_counts(dropna=False).to_frame(name='counts').sort_values(by='counts', b4=False)
    b9 = b8.index[:-1].tolist()
    for category in b9:
        b10 = f"{column}_dum_{category}"
        data[b10] = (data[column] == category).astype(int)
    return b9
def fonk6(data, column):
    b8 = data[column].value_counts(dropna=False).to_frame(name='counts')
    b11 = b8.index.tolist()
    b12 = len(b11)
    b13 = len(bin(b12)[2:])
    b14 = [int(bin(i)[2:]) for i in range(b12)]
    b15 = list(zip(b11, b14))
    for j in range(b13):
        b10 = f"{column}_dum_{j}"
        data[b10] = 0
        for i, category in enumerate(b11):
            data.loc[data[column] == category, b10] = b14[i] % 10
            b14[i]
    return b15