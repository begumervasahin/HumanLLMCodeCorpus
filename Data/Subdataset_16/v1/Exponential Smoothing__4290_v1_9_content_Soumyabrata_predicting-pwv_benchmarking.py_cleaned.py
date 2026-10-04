import numpy as np
import pandas as pd
import random
import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from read_matfile import read_matfile
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
timestamp, b2 = read_matfile(b1)
print('Imported the MATLAB file')
b3 = np.column_stack((timestamp, b2))
b4 = pd.DataFrame(data=b3, columns=['timestamps', 'b2']).set_index('timestamps')
b5 = len(b4)
b6 = np.arange(5, 20, 5)
a1 = 10
a2 = 10000
b7 = int(a2 / 5)
with open("./results/comparison.txt", "w") as text_file:
    text_file.write("b14, our, naive, average\n")
    for lead_time in b6:
        b8 = int(lead_time / 5)
        b9 = []
        b10 = []
        b11 = []
        for _ in range(a1):
            b12 = b5 - (b7 + b8)
            b13 = random.randint(0, b12)
            print(f'From start index of {b13}')
            print(f'Computing for lead b14 = {lead_time} mins with history of {a2} mins')
            b15 = b4[b13:b13 + b7]
            b16 = b4[b13 + b7:b13 + b7 + b8]
            b17 = b16.copy()
            print('Computation started')
            b18 = ExponentialSmoothing(np.asarray(b15['b2']), seasonal_periods=288, trend='add', seasonal='add').fit()
            b17['Holt_Winter'] = b18.forecast(len(b16))
            b19 = b15['b2'].iloc[-1]
            b17['naive'] = b19 * np.ones(len(b16))
            b20 = np.mean(b15['b2'])
            b17['aver'] = b20 * np.ones(len(b16))
            print('Computation completed')
            b21 = np.sqrt(np.mean((b17['Holt_Winter'] - b17['b2']) ** 2))
            b9.append(b21)
            b21 = np.sqrt(np.mean((b17['naive'] - b17['b2']) ** 2))
            b10.append(b21)
            b21 = np.sqrt(np.mean((b17['aver'] - b17['b2']) ** 2))
            b11.append(b21)
        text_file.write(f"{lead_time}, {np.mean(b9)}, {np.mean(b10)}, {np.mean(b11)}\n")