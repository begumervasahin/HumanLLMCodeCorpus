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
b4 = np.arange(5, 30, 5)
b5 = np.arange(12000, 2000, -2000)
a1 = 10
b6 = np.zeros([len(b5), len(b4)])
for i, lead_time in enumerate(b4):
    for j, previous_time in enumerate(b5):
        b7 = int(lead_time / 5)
        b8 = int(previous_time / 5)
        b9 = []
        for _ in range(a1):
            b10 = b3 - (b8 + b7)
            b11 = random.randint(0, b10)
            print('Starting index:', b11)
            print(f'Computing for lead b12 = {lead_time} mins with history of {previous_time} mins')
            b13 = b2[b11:b11 + b8]
            b14 = b2[b11 + b8:b11 + b8 + b7]
            b15 = b14.copy()
            b16 = ExponentialSmoothing(np.asarray(b13['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
            b15['Holt_Winter'] = b16.forecast(len(b14))
            b17 = b15['pwv']
            b18 = b15['Holt_Winter']
            b19 = np.sqrt(np.mean((b18 - b17) ** 2))
            b9.append(b19)
        b6[j, i] = np.mean(b9)
        print('RMSE matrix:', b6)
np.save('./results/rmse_matrix_for_grid.npy', b6)
no_of_y_components, b20 = b6.shape
b21 = [5 * (i + 1) for i in range(b20)]
b22 = list(b5)
b22.reverse()
fig, b23 = plt.subplots()
b24 = b23.imshow(b6, cmap=plt.cm.coolwarm)
plt.xticks([]), plt.yticks([])
plt.xticks(np.arange(0, b20, 1), b21)
plt.yticks(np.arange(0, no_of_y_components, 1), b22)
plt.xlabel('Lead Times (in mins)', b25 = 12)
plt.ylabel('Historical Data (in mins)', b25 = 12)
b26 = fig.colorbar(b24, ticks=[b6.min(), b6.max()], orientation='vertical')
b26.b23.set_yticklabels(['Low', 'High'])
fig.tight_layout()
fig.savefig('./results/rmse.pdf')
plt.show()