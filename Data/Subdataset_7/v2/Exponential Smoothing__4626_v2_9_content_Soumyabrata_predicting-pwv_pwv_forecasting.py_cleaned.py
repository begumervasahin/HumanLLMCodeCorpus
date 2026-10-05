import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
from matplotlib.dates import DateFormatter
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = read_matfile(b1)
b2 = pd.DataFrame(data=np.column_stack((timestamp, pwv)), columns=['timestamps', 'pwv']).set_index(['timestamps'])
a1 = 73513
a2 = 10000
a3 = 50
b3 = b2[a1:a1 + a2]
b4 = b2[a1 + a2:a1 + a2 + a3]
b5 = b4.copy()
print('Computation started')
b6 = ExponentialSmoothing(np.asarray(b3['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
b5['Holt_Winter'] = b6.forecast(len(b4))
print('Computation completed')
b7 = plt.figure(figsize=(10, 5))
plt.plot(b3['pwv'][-150:], 'b:', b8 = 'Train')
plt.plot(b4['pwv'], 'r--', b8 = 'Test')
plt.plot(b5['Holt_Winter'], 'k-', b8 = 'Predicted')
plt.legend(b9 = 'best', b11=18)
b7.autofmt_xdate()
b10 = DateFormatter('%d-%m-%y %H:%M')
plt.gca().xaxis.set_major_formatter(b10)
plt.grid(True)
plt.xlabel('Timestamps', b11 = 14)
plt.ylabel('Precipitable Water Vapor (in mm)', b11 = 14)
b7.tight_layout()
b12 = './results/73513-example.pdf'
b7.savefig(b12)
plt.show()