import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime
from matplotlib.dates import DateFormatter
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import statsmodels.api as sm
import pandas as pd
import random
from read_matfile import *
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = read_matfile (b1)
print ('Imported the MATLAB file')
b2 = np.column_stack((timestamp, pwv))
b3 = pd.DataFrame(data=b2, columns=['timestamps', 'pwv']).set_index(['timestamps'])
b4 = len(b3)
b5 = np.arange(5, 30, 5)
b6 = np.arange(12000, 2000, -2000)
a1 = 10
b7 = np.zeros([len(b6), len(b5)])
print (b7)
for i, item1 in enumerate(b5):
    for j, item2 in enumerate(b6):
        b8 = item1
        b9 = item2
        b10 = int(b8 / 5)
        b11 = int(b9 / 5)
        b12 = []
        for _ in range(a1):
            b13 = b4 - (b11+b10)
            b14 = random.randint(0, b13)
            print ('From start index of ', str(b14))
            print (['computing for lead b15 = ', str(b8), ' mins with history of ', str(b9), ' mins'])
            b16 = b3[b14:b14+b11]
            b17 = b3[b14+b11:b14+b11+b10]
            b18 = b17.copy()
            print ('computation started')
            b19 = ExponentialSmoothing(np.asarray(b16['pwv']) ,seasonal_periods=288 ,trend='add', seasonal='add',).fit()
            b18['Holt_Winter'] = b19.forecast(len(b17))
            print ('computation completed')
            b20 = b18['pwv']
            b21 = b18['Holt_Winter']
            b22 = np.sqrt(np.mean((b21-b20)**2))
            b12.append(b22)
        b12 = np.array(b12)
        b7[j,i] = np.mean(b12)
        print (b7)
np.save('./results/rmse_matrix_for_grid.npy', b7)
(no_of_y_components, no_of_x_components) =  b7.shape
b23 = []
for i in range(no_of_x_components):
    b23.append(5*(i+1))
b24 = []
b25 = b6[0]
b26 = b6[0] - b6[1]
for i in range(no_of_y_components):
    b24.append(b25)
    b25 = b25 - b26
fig, b27 = plt.subplots()
b28 = b27.imshow(b7, cmap=plt.cm.coolwarm)
plt.xticks([]),plt.yticks([])
plt.xticks(np.arange(0,no_of_x_components,1), b23)
plt.yticks(np.arange(0,no_of_y_components,1), b24)
plt.xlabel('Lead Times (in mins)', b29 = 12)
plt.ylabel('Historical Data (in mins)', b29 = 12)
b30 = fig.colorbar(b28, ticks=[b7.min(), b7.max()], orientation='vertical')
b30.b27.set_yticklabels(['Low', 'High'])
fig.tight_layout()
fig.savefig('./results/rmse.pdf')
plt.show()