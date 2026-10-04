import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
def fonk1(b10, b11):
    a1 = 0
    for b5 in range(len(b10)):
        a1 += abs(b11[b5] - b10[b5]) / b10[b5]
    return a1 / len(b10)
def fonk2(b13, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if isinstance(b13, list) else b13.shape[1]
    b3 = pd.DataFrame(b13)
    cols, b4 = [], []
    for b5 in range(b1, 0, -1):
        cols.append(b3.shift(b5))
        b4 += [f'var{j + 1}(t-{b5})' for j in range(b2)]
    for b5 in range(0, n_out):
        cols.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [f'var{j + 1}(t)' for j in range(b2)]
        else:
            b4 += [f'var{j + 1}(t+{b5})' for j in range(b2)]
    b6 = pd.concat(cols, axis=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
if b9 = = "__main__":
    b10 = np.array([100, 200, 300, 400, 500])
    b11 = np.array([110, 190, 310, 420, 480])
    b12 = fonk1(b10, b11)
    print(f"Mean Absolute Percentage Error: {b12:.2%}")
    b13 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    b14 = fonk2(b13, b1=2, n_out=1)
    print(b14)