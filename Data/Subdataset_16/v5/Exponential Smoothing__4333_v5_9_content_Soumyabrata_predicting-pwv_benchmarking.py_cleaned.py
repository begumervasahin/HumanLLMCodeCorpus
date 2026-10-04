import numpy as np
import pandas as pd
import random
from statsmodels.tsa.api import ExponentialSmoothing
from read_matfile import read_matfile
def fonk1(b18):
    timestamp, b1 = read_matfile(b18)
    print('Imported the MATLAB file')
    b2 = np.column_stack((timestamp, b1))
    return pd.DataFrame(b2, b3 = ['timestamps', 'b1']).set_index('timestamps')
def fonk2(y_true, y_pred):
    return np.sqrt(np.mean((y_pred - y_true) ** 2))
def fonk3(b19, b20, a1, b21, text_file):
    b4 = len(b19)
    for lead_time in b20:
        b5 = int(lead_time / 5)
        rmse_list, naive_list, b6 = [], [], []
        for _ in range(a1):
            b7 = b4 - (b21 + b5)
            b8 = random.randint(0, b7)
            print(f'Start index: {b8}')
            print(f'Lead time: {lead_time} mins with history of {b21 * 5} mins')
            b9 = b19[b8:b8 + b21]
            b10 = b19[b8 + b21:b8 + b21 + b5]
            b11 = b10.copy()
            print('Computation started')
            b12 = ExponentialSmoothing(
                np.asarray(b9['b1']),
                b13 = 288,
                b14 = 'add',
                b15 = 'add'
            ).b12()
            b11['Holt_Winter'] = b12.forecast(len(b10))
            b16 = b9['b1'].iloc[-1]
            b11['naive'] = b16 * np.ones(len(b10))
            b17 = np.mean(b9['b1'])
            b11['average'] = b17 * np.ones(len(b10))
            print('Computation completed')
            rmse_list.append(fonk2(b11['b1'], b11['Holt_Winter']))
            naive_list.append(fonk2(b11['b1'], b11['naive']))
            b6.append(fonk2(b11['b1'], b11['average']))
        text_file.write(f"{lead_time}, {np.mean(rmse_list)}, {np.mean(naive_list)}, {np.mean(b6)}\n")
def fonk4():
    b18 = './b2/PWV_2010from_WS_2_withGradient.mat'
    b19 = fonk1(b18)
    b20 = np.arange(5, 20, 5)
    a1 = 10
    a2 = 10000
    b21 = int(a2 / 5)
    with open("./results/comparison.txt", "w") as text_file:
        text_file.write("time, our, naive, average\n")
        fonk3(b19, b20, a1, b21, text_file)
if b22 = = '__main__':
    fonk4()