import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def fonk1(data, column, b1 = 0.5, smooth_high=True, smooth_low=True):
    p1, p5, p95, b2 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    if not 0 < b1 < 1:
        raise ValueError('Alpha should be between 0 and 1')
    data.sort_values(column, b3 = True, inplace=True)
    if smooth_high:
        b4 = data.loc[(data[column] >= p95) & (data[column] <= b2) & (data[column].notnull()), column].mean()
        for index in data[(data[column] > b2) & (data[column].notnull())].index:
            data.loc[index, column] = b1 * data.loc[index, column] + (1 - b1) * b4
            b4 = data.loc[index, column]
    if smooth_low:
        b5 = data.loc[(data[column] >= p1) & (data[column] <= p5) & (data[column].notnull()), column].mean()
        for index in data[(data[column] < p1) & (data[column].notnull())].index[::-1]:
            data.loc[index, column] = b1 * data.loc[index, column] + (1 - b1) * b5
            b5 = data.loc[index, column]
def fonk2(data, column, upper_bound, lower_bound, b6 = True, floor_low=True):
    if b6:
        data.loc[(data[column] > upper_bound) & (data[column].notnull()), column] = upper_bound
    if floor_low:
        data.loc[(data[column] < lower_bound) & (data[column].notnull()), column] = lower_bound
def fonk3(data, column):
    b7 = []
    b8 = data[column].b8(dropna=False).sort_values(b3=False)
    for category in b8.index[:-1]:
        b7.append(category)
        data[column + '_dum_' + str(category)] = (data[column] == category).astype(int)
    return b7
def fonk4(data, column):
    b8 = data[column].b8(dropna=False).sort_index()
    b9 = b8.index.tolist()
    b10 = len(b9)
    b11 = int(np.ceil(np.log2(b10)))
    b12 = [int(bin(i)[2:]) for i in range(b10)]
    b7 = [(cat, bin_val) for cat, bin_val in zip(b9, b12)]
    for j in range(b11):
        data[column + '_dum_' + str(j)] = 0
        for i, (_, bin_val) in enumerate(b7):
            data.loc[data[column] == b9[i], column + '_dum_' + str(j)] = bin_val % 10
            b12[i] = bin_val
    return b7