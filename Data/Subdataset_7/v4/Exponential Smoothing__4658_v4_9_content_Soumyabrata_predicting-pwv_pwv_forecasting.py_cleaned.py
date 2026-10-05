import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
from matplotlib.dates import DateFormatter
b1 = './data/PWV_2010from_WS_2_withGradient.mat'
timestamps, b2 = read_matfile(b1)
b3 = pd.DataFrame(data=np.column_stack((timestamps, b2)), columns=['timestamps', 'b2']).set_index('timestamps')
a1 = 73513
a2 = 10000
a3 = 50
b4 = b3[a1:a1 + a2]
b5 = b3[a1 + a2:a1 + a2 + a3]
b6 = b5.copy()
print('Computation started')
b7 = ExponentialSmoothing(np.asarray(b4['b2']), seasonal_periods=288, trend='add', seasonal='add').fit()
b6['Holt_Winter'] = b7.forecast(len(b5))
print('Computation completed')
plt.figure(b8 = (10, 5))
plt.plot(b4['b2'][-150:], 'b:', b9 = 'Train')
plt.plot(b5['b2'], 'r--', b9 = 'Test')
plt.plot(b6['Holt_Winter'], 'k-', b9 = 'Predicted')
plt.legend(b10 = 'best', b12=18)
plt.gcf().autofmt_xdate()
b11 = DateFormatter('%d-%m-%y %H:%M')
plt.gca().xaxis.set_major_formatter(b11)
plt.grid(True)
plt.xlabel('Timestamps', b12 = 14)
plt.ylabel('Precipitable Water Vapor (in mm)', b12 = 14)
plt.tight_layout()
b13 = './results/73513-example.pdf'
plt.savefig(b13)
plt.show()