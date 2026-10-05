import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from statsmodels.tsa.api import ExponentialSmoothing
def fonk1(b1):
    pass
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = fonk1(b1)
print('Imported the MATLAB file')
b2 = np.column_stack((timestamp, pwv))
b3 = pd.DataFrame(data=b2, columns=['timestamps', 'pwv']).set_index(['timestamps'])
b4 = len(b3)
b5 = np.arange(5, 20, 5)
a1 = 10
a2 = 10000
b6 = int(a2 / 5)
b7 = open("./results/comparison.txt", "w")
b7.write("b15, our, naive, average \n")
for item1 in b5:
    b8 = item1
    b9 = int(b8 / 5)
    b10 = []
    b11 = []
    b12 = []
    for _ in range(a1):
        b13 = b4 - (b6 + b9)
        b14 = random.randint(0, b13)
        print('From start index of ', str(b14))
        print(['computing for lead b15 = ', str(b8), ' mins with history of ', str(a2), ' mins'])
        b16 = b3[b14:b14 + b6]
        b17 = b3[b14 + b6:b14 + b6 + b9]
        b18 = b17.copy()
        b19 = ExponentialSmoothing(np.asarray(b16['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
        b18['Holt_Winter'] = b19.forecast(len(b17))
        b20 = b16['pwv'][-1]
        b18['naive'] = b20 * np.ones(len(b17))
        b21 = np.mean(b16['pwv'])
        b18['aver'] = b21 * np.ones(len(b17))
        b22 = np.sqrt(np.mean((b18['Holt_Winter'] - b18['pwv']) ** 2))
        b10.append(b22)
        b22 = np.sqrt(np.mean((b18['naive'] - b18['pwv']) ** 2))
        b11.append(b22)
        b22 = np.sqrt(np.mean((b18['aver'] - b18['pwv']) ** 2))
        b12.append(b22)
    b7.write("%s, %s, %s, %s \n" % (b8, np.mean(b10), np.mean(b11), np.mean(b12)))
b7.close()