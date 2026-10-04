import math
from math import sqrt
import numpy as np
from numpy import concatenate
from pandas import read_csv, DataFrame, concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
def fonk1(y_true, y_pred):
    a1 = 0
    for b5 in range(len(y_true)):
        a1 += abs(y_pred[b5] - y_true[b5]) / y_true[b5]
    return a1 / len(y_true)
def fonk2(data, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if isinstance(data, list) else data.shape[1]
    b3 = DataFrame(data)
    cols, b4 = [], []
    for b5 in range(b1, 0, -1):
        cols.append(b3.shift(b5))
        b4 += [f'var{j+1}(t-{b5})' for j in range(b2)]
    for b5 in range(n_out):
        cols.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [f'var{j+1}(t)' for j in range(b2)]
        else:
            b4 += [f'var{j+1}(t+{b5})' for j in range(b2)]
    b6 = concat(cols, axis=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
