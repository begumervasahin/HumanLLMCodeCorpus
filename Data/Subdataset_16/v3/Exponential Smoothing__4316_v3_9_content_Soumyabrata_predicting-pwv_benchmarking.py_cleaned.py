import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
from statsmodels.tsa.api import ExponentialSmoothing
from read_matfile import read_matfile
def fonk1(b19):
    timestamp, b1 = read_matfile(b19)
    print('Imported the MATLAB file')
    b2 = np.column_stack((timestamp, b1))
    b3 = pd.DataFrame(b2=b2, columns=['timestamps', 'b1']).set_index('timestamps')
    return b3
def fonk2(y_true, y_pred):
    return np.sqrt(np.mean((y_pred - y_true) ** 2))
def fonk3(b3, b20, a1, b21, text_file):
    b4 = len(b3)
    for lead_time in b20:
        b5 = int(lead_time / 5)
        rmse_array, persist_array, b6 = [], [], []
        for _ in range(a1):
            b7 = b4 - (b21 + b5)
            b8 = random.randint(0, b7)
            print(f'From start index of {b8}')
            print(f'Computing for lead b9 = {lead_time} mins with history of {a2} mins')
            b10 = b3[b8:b8 + b21]
            b11 = b3[b8 + b21:b8 + b21 + b5]
            b12 = b11.copy()
            print('Computation started')
            b13 = ExponentialSmoothing(
                np.asarray(b10['b1']),
                b14 = 288,
                b15 = 'add',
                b16 = 'add'
            ).b13()
            b12['Holt_Winter'] = b13.forecast(len(b11))
            b17 = b10['b1'].iloc[-1]
            b12['naive'] = b17 * np.ones(len(b11))
            b18 = np.mean(b10['b1'])
            b12['aver'] = b18 * np.ones(len(b11))
            print('Computation completed')
            rmse_array.append(fonk2(b12['b1'], b12['Holt_Winter']))
            persist_array.append(fonk2(b12['b1'], b12['naive']))
            b6.append(fonk2(b12['b1'], b12['aver']))
        text_file.write(f"{lead_time}, {np.mean(rmse_array)}, {np.mean(persist_array)}, {np.mean(b6)}\n")
def fonk4():
    b19 = './b2/PWV_2010from_WS_2_withGradient.mat'
    b3 = fonk1(b19)
    b20 = np.arange(5, 20, 5)
    a1 = 10
    a2 = 10000
    b21 = int(a2 / 5)
    with open("./results/comparison.txt", "w") as text_file:
        text_file.write("b9, our, naive, average\n")
        fonk3(b3, b20, a1, b21, text_file)
if b22 = = '__main__':
    fonk4()