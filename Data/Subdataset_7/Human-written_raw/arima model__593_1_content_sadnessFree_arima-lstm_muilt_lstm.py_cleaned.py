from math import sqrt
import math
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
import matplotlib
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import numpy
def fonk1(y_true, y_pred):
    a1 = 0
    for b5 in range(len(y_true)):
        a1 += math.fabs(y_pred[b5] - y_true[b5]) / y_true[b5]
    return a1 / len(y_true)
def fonk2(data, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if type(data) is list else data.shape[1]
    b3 = DataFrame(data)
    cols, b4 = list(), list()
    for b5 in range(b1, 0, -1):
        cols.append(b3.shift(b5))
        b4 += [('var%d(t-%d)' % (j + 1, b5)) for j in range(b2)]
    for b5 in range(0, n_out):
        cols.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [('var%d(t)' % (j + 1)) for j in range(b2)]
        else:
            b4 += [('var%d(t+%d)' % (j + 1, b5)) for j in range(b2)]
    b6 = concat(cols, axis=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6