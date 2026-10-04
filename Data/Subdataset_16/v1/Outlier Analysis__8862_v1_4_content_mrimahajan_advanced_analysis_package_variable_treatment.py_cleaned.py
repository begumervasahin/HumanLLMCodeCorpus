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
def fonk1(data, s, b1 = 0.5, b6=True, low=True):
    p1, p5, p95, b2 = data[s].quantile([0.01, 0.05, 0.95, 0.99])
    if not 0 < b1 < 1:
        raise ValueError('b1 should be between 0 and 1')
    data.sort_values(s, b3 = True, inplace=True)
    if b6:
        b4 = fonk2(list(np.array(data.loc[(data[s] >= p95) & (data[s] <= b2) & (data[s].notnull()), s])), b1)
        for i in data[(data[s] > b2) & (data[s].notnull())].index.tolist():
            data.loc[i, s] = b1 * data.loc[i, s] + (1 - b1) * b4
            b4 = data.loc[i, s]
    if low:
        b4 = fonk3(list(np.array(data.loc[(data[s] >= p1) & (data[s] <= p5) & (data[s].notnull()), s])), b1)
        for i in data[(data[s] < p1) & (data[s].notnull())].index.tolist()[::-1]:
            data.loc[i, s] = b1 * data[s].loc[i, s] + (1 - b1) * b4
            b4 = data.loc[i, s]
def fonk2(array, b1):
    b5 = array[0]
    for i in range(1, len(array)):
        b5 = b1 * array[i] + (1 - b1) * b5
    return b5
def fonk3(array, b1):
    b5 = array[-1]
    for i in range(len(array) - 2, -1, -1):
        b5 = b1 * array[i + 1] + (1 - b1) * b5
    return b5
def fonk4(data, s, a, b, b6 = True, low=True):
    if b6:
        data.loc[(data[s] > a) & (data[s].notnull()), s] = a
    if low:
        data.loc[(data[s] < b) & (data[s].notnull()), s] = b
def fonk5(data, s):
    b7 = []
    b8 = pd.DataFrame()
    b8['counts'] = data[s].value_counts(b9 = False)
    b8.sort_values(b10 = 'counts', b3=False, inplace=True)
    for category in b8.index.tolist()[:-1]:
        b7.append(category)
        data[s + '_dum_' + str(category)] = 0
        data.loc[data[s] == category, s + '_dum_' + str(category)] = 1
    return b7
def fonk6(data, s):
    b8 = pd.DataFrame()
    b8['counts'] = data[s].value_counts(b9 = False)
    b11 = b8.index.tolist()
    b12 = len(b11)
    b13 = len(str(int(bin(b12)[2:], 10)))
    b14 = [int(bin(i)[2:], 10) for i in range(b12)]
    b15 = [(cat, b14[i]) for i, cat in enumerate(b11)]
    for j in range(b13):
        data[s + '_dum_' + str(j)] = 0
        for i, cat in enumerate(b11):
            data.loc[data[s] == cat, s + '_dum_' + str(j)] = b14[i] % 10
            b14[i] = b14[i]
    return b15