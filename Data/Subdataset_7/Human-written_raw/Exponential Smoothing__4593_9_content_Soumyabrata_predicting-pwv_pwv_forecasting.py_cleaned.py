import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime
from matplotlib.dates import DateFormatter
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import statsmodels.api as sm
import pandas as pd
from read_matfile import *
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = read_matfile (b1)
b2 = np.column_stack((timestamp, pwv))
b3 = pd.DataFrame(data=b2, columns=['timestamps', 'pwv']).set_index(['timestamps'])
a1 = 73513
b4 = b3[a1:a1+10000]
b5 = b3[a1+10000:a1+10000+50]
b6 = b5.copy()
print ('computation started')
b7 = ExponentialSmoothing(np.asarray(b4['pwv']) ,seasonal_periods=288 ,trend='add', seasonal='add',).fit()
b6['Holt_Winter'] = b7.forecast(len(b5))
print ('computation completed')
b8 = plt.figure(1, figsize=(10,5))
plt.plot(b4['pwv'][-150:], 'b:', b9 = 'Train')
plt.plot(b5['pwv'], 'r--', b9 = 'Test')
plt.plot(b6['Holt_Winter'], 'k-', b9 = 'Predicted')
plt.legend(b10 = 'best', b12=18)
b8.autofmt_xdate()
b11 = DateFormatter('%d-%m-%y %H:%M')
plt.gcf().axes[0].xaxis.set_major_formatter(b11)
plt.grid(True)
plt.xlabel('Timestamps', b12 = 14)
plt.ylabel('Precipitible Water Vapor (in mm)', b12 = 14)
b8.tight_layout()
b13 = './results/73513-example.pdf'
b8.savefig(b13)
plt.show()