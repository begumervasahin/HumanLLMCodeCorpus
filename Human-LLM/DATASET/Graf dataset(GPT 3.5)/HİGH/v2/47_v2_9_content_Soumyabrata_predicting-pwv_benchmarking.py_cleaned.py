import numpy as np
import pandas as pd
import random
from statsmodels.tsa.api import ExponentialSmoothing
def fonk1(b1):
    pass
b1 = './b2/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = fonk1(b1)
print('MATLAB file imported successfully')
b2 = np.column_stack((timestamp, pwv))
b3 = pd.DataFrame(b2=b2, columns=['timestamps', 'pwv']).set_index(['timestamps'])
b4 = len(b3)
b5 = np.arange(5, 20, 5)
a1 = 10
a2 = 10000
b6 = int(a2 / 5)
b7 = open("./results/comparison.txt", "w")
b7.write("lead_time, our_model, naive_model, average_model\n")
for lead_time in b5:
    b8 = int(lead_time / 5)
    b9 = []
    b10 = []
    b11 = []
    for _ in range(a1):
        b12 = random.randint(0, b4 - (b6 + b8))
        b13 = b3[b12:b12 + b6]
        b14 = b3[b12 + b6:b12 + b6 + b8]
        b15 = b14.copy()
        b16 = ExponentialSmoothing(np.asarray(b13['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
        b15['Holt_Winter'] = b16.forecast(len(b14))
        b17 = b13['pwv'][-1]
        b15['naive'] = b17 * np.ones(len(b14))
        b18 = np.mean(b13['pwv'])
        b15['average'] = b18 * np.ones(len(b14))
        b19 = np.sqrt(np.mean((b15['Holt_Winter'] - b15['pwv']) ** 2))
        b9.append(b19)
        b19 = np.sqrt(np.mean((b15['naive'] - b15['pwv']) ** 2))
        b10.append(b19)
        b19 = np.sqrt(np.mean((b15['average'] - b15['pwv']) ** 2))
        b11.append(b19)
    b7.write("%s, %s, %s, %s\n" % (lead_time, np.mean(b9), np.mean(b10), np.mean(b11)))
b7.close()