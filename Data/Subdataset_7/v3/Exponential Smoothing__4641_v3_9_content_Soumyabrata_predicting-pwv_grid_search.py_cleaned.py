import numpy as np
import pandas as pd
import random
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
timestamps, b2 = read_matfile(b1)
print('Imported the MATLAB file')
b3 = pd.DataFrame(data=np.column_stack((timestamps, b2)), columns=['timestamps', 'b2']).set_index(['timestamps'])
b4 = len(b3)
b5 = np.arange(5, 30, 5)
b6 = np.arange(12000, 2000, -2000)
a1 = 10
b7 = np.zeros([len(b6), len(b5)])
for i, lead_time in enumerate(b5):
    for j, previous_time in enumerate(b6):
        b8 = int(lead_time / 5)
        b9 = int(previous_time / 5)
        b10 = []
        for _ in range(a1):
            b11 = b4 - (b9 + b8)
            b12 = random.randint(0, b11)
            print('Starting index:', b12)
            print(f'Computing for lead b13 = {lead_time} mins with history of {previous_time} mins')
            b14 = b3[b12:b12 + b9]
            b15 = b3[b12 + b9:b12 + b9 + b8]
            b16 = b15.copy()
            b17 = ExponentialSmoothing(np.asarray(b14['b2']), seasonal_periods=288, trend='add', seasonal='add').fit()
            b16['Holt_Winter'] = b17.forecast(len(b15))
            b18 = b16['b2']
            b19 = b16['Holt_Winter']
            b20 = np.sqrt(np.mean((b19 - b18) ** 2))
            b10.append(b20)
        b7[j, i] = np.mean(b10)
        print('RMSE matrix:', b7)
np.save('./results/rmse_matrix_for_grid.npy', b7)
num_rows, b21 = b7.shape
b22 = [5 * (i + 1) for i in range(b21)]
b23 = list(b6)
b23.reverse()
fig, b24 = plt.subplots()
b25 = b24.imshow(b7, cmap=plt.cm.coolwarm)
plt.xticks([]), plt.yticks([])
plt.xticks(np.arange(0, b21, 1), b22)
plt.yticks(np.arange(0, num_rows, 1), b23)
plt.xlabel('Lead Times (in mins)', b26 = 12)
plt.ylabel('Historical Data (in mins)', b26 = 12)
b27 = fig.colorbar(b25, ticks=[b7.min(), b7.max()], orientation='vertical')
b27.b24.set_yticklabels(['Low', 'High'])
fig.tight_layout()
fig.savefig('./results/rmse.pdf')
plt.show()