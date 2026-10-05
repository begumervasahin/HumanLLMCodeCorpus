import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
from matplotlib.dates import DateFormatter
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
timestamps, b2 = read_matfile(b1)
b3 = pd.DataFrame({'timestamps': timestamps, 'b2': b2}).set_index('timestamps')
a1 = 73513
a2 = 10000
a3 = 50
b4 = b3.iloc[a1:a1 + a2]
b5 = b3.iloc[a1 + a2:a1 + a2 + a3]
b6 = b5.copy()
print('Computation started')
b7 = ExponentialSmoothing(np.asarray(b4['b2']),
                             b8 = 288,
                             b9 = 'add',
                             b10 = 'add').fit()
b6['Holt_Winter'] = b7.forecast(len(b5))
print('Computation completed')
plt.figure(b11 = (10, 5))
plt.plot(b4['b2'][-150:], 'b:', b12 = 'Train')
plt.plot(b5['b2'], 'r--', b12 = 'Test')
plt.plot(b6['Holt_Winter'], 'k-', b12 = 'Predicted')
plt.legend(b13 = 'best', b15=18)
plt.gcf().autofmt_xdate()
b14 = DateFormatter('%d-%m-%y %H:%M')
plt.gca().xaxis.set_major_formatter(b14)
plt.grid(True)
plt.xlabel('Timestamps', b15 = 14)
plt.ylabel('Precipitable Water Vapor (in mm)', b15 = 14)
plt.tight_layout()
b16 = './results/73513-example.pdf'
plt.savefig(b16)
plt.show()