import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def fonk1(data, s, b1 = 0.5, b6=True, low=True):
    p1, p5, p95, b2 = data[s].quantile([0.01, 0.05, 0.95, 0.99])
    if not 0 < b1 < 1:
        raise ValueError('b1 should be between 0 and 1')
    data.sort_values(s, b3 = True, inplace=True)
    if b6:
        b4 = data.loc[(data[s] >= p95) & (data[s] <= b2) & (data[s].notnull()), s].mean()
        for i in data[(data[s] > b2) & (data[s].notnull())].index:
            data.loc[i, s] = b1 * data.loc[i, s] + (1 - b1) * b4
            b4 = data.loc[i, s]
    if low:
        b5 = data.loc[(data[s] >= p1) & (data[s] <= p5) & (data[s].notnull()), s].mean()
        for i in data[(data[s] < p1) & (data[s].notnull())].index[::-1]:
            data.loc[i, s] = b1 * data.loc[i, s] + (1 - b1) * b5
            b5 = data.loc[i, s]
def fonk2(data, s, a, b, b6 = True, low=True):
    if b6:
        data.loc[(data[s] > a) & (data[s].notnull()), s] = a
    if low:
        data.loc[(data[s] < b) & (data[s].notnull()), s] = b
def fonk3(data, s):
    b7 = []
    b8 = data[s].value_counts(dropna=False).sort_values(b3=False)
    for category in b8.index[:-1]:
        b7.append(category)
        data[s + '_dum_' + str(category)] = (data[s] == category).astype(int)
    return b7
def fonk4(data, s):
    b8 = data[s].value_counts(dropna=False).sort_index()
    b9 = b8.index.tolist()
    b10 = len(b9)
    b11 = int(np.ceil(np.log2(b10)))
    b12 = [int(bin(i)[2:]) for i in range(b10)]
    b13 = [(cat, bin_val) for cat, bin_val in zip(b9, b12)]
    for j in range(b11):
        data[s + '_dum_' + str(j)] = 0
        for i, (_, bin_val) in enumerate(b13):
            data.loc[data[s] == b9[i], s + '_dum_' + str(j)] = bin_val % 10
            b12[i] = bin_val
    return b13
