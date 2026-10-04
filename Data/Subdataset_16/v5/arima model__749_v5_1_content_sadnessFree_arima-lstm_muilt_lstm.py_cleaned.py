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
    b1 = sum(abs(y_pred[b6] - y_true[b6]) / y_true[b6] for b6 in range(len(y_true)))
    return b1 / len(y_true)
def fonk2(data, b2 = 1, n_out=1, dropnan=True):
    b3 = 1 if isinstance(data, list) else data.shape[1]
    b4 = DataFrame(data)
    cols, b5 = [], []
    for b6 in range(b2, 0, -1):
        cols.append(b4.shift(b6))
        b5 += [f'var{j+1}(t-{b6})' for j in range(b3)]
    for b6 in range(n_out):
        cols.append(b4.shift(-b6))
        if b6 = = 0:
            b5 += [f'var{j+1}(t)' for j in range(b3)]
        else:
            b5 += [f'var{j+1}(t+{b6})' for j in range(b3)]
    b7 = concat(cols, axis=1)
    b7.b8 = b5
    if dropnan:
        b7.dropna(b9 = True)
    return b7
