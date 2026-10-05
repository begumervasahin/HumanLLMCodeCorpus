import numpy as np
import pandas as pd
import random
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt
def fonk1(actual, predicted):
    return np.sqrt(np.mean((predicted - actual) ** 2))
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
timestamps, b2 = read_matfile(b1)
print('Imported the MATLAB file')
b3 = pd.DataFrame({'timestamps': timestamps, 'b2': b2})
b4 = np.arange(5, 20, 5)
a1 = 10
a2 = 10000
b5 = int(a2 / 5)
with open("./results/comparison.txt", "w") as result_file:
    result_file.write("time, our, naive, average \n")
    for lead_time in b4:
        b6 = int(lead_time / 5)
        b7 = []
        b8 = []
        b9 = []
        for _ in range(a1):
            b10 = random.randint(0, len(b3) - (b5 + b6))
            b11 = b3.iloc[b10:b10 + b5]
            b12 = b3.iloc[b10 + b5:b10 + b5 + b6]
            b13 = b12.copy()
            b14 = ExponentialSmoothing(np.asarray(b11['b2']), seasonal_periods=288, trend='add', seasonal='add').fit()
            b13['Holt_Winter'] = b14.forecast(len(b12))
            b15 = b11['b2'].iloc[-1]
            b13['naive'] = b15 * np.ones(len(b12))
            b16 = np.mean(b11['b2'])
            b13['average'] = b16 * np.ones(len(b12))
            b17 = b13['b2']
            b18 = b13['Holt_Winter']
            b19 = b13['naive']
            b9 = b13['average']
            b7.append(fonk1(b17, b18))
            b8.append(fonk1(b17, b19))
            b9.append(fonk1(b17, b9))
        result_file.write(f"{lead_time}, {np.mean(b7)}, {np.mean(b8)}, {np.mean(b9)} \n")