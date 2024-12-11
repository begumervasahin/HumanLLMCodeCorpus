
import numpy as np
import pandas as pd
import random
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = read_matfile(b1)
print('Imported the MATLAB file')
b2 = pd.DataFrame(data=np.column_stack((timestamp, pwv)), columns=['timestamps', 'pwv']).set_index(['timestamps'])
b3 = len(b2)
b4 = np.arange(5, 20, 5)
a1 = 10
a2 = 10000
b5 = int(a2 / 5)
with open("./results/comparison.txt", "w") as text_file:
    text_file.write("b12, our, naive, average \n")
    for lead_time in b4:
        b6 = int(lead_time / 5)
        b7 = []
        b8 = []
        b9 = []
        for _ in range(a1):
            b10 = b3 - (b5 + b6)
            b11 = random.randint(0, b10)
            print('From start index of ', str(b11))
            print(['computing for lead b12 = ', str(lead_time), ' mins with history of ', str(a2), ' mins'])
            b13 = b2[b11:b11 + b5]
            b14 = b2[b11 + b5:b11 + b5 + b6]
            b15 = b14.copy()
            print('computation started')
            b16 = ExponentialSmoothing(np.asarray(b13['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
            b15['Holt_Winter'] = b16.forecast(len(b14))
            b17 = b13['pwv'][-1]
            b15['naive'] = b17 * np.ones(len(b14))
            b18 = np.mean(b13['pwv'])
            b15['aver'] = b18 * np.ones(len(b14))
            print('computation completed')
            b19 = b15['pwv']
            b20 = b15['Holt_Winter']
            b21 = np.sqrt(np.mean((b20 - b19) ** 2))
            b7.append(b21)
            b19 = b15['pwv']
            b20 = b15['naive']
            b21 = np.sqrt(np.mean((b20 - b19) ** 2))
            b8.append(b21)
            b19 = b15['pwv']
            b20 = b15['aver']
            b21 = np.sqrt(np.mean((b20 - b19) ** 2))
            b9.append(b21)
        b7 = np.array(b7)
        b8 = np.array(b8)
        b9 = np.array(b9)
        text_file.write("%s, %s, %s, %s \n" % (lead_time, np.mean(b7), np.mean(b8), np.mean(b9)))