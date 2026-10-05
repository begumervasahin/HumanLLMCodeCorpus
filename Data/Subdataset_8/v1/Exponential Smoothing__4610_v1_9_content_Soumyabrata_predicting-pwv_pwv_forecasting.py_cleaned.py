import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
from matplotlib.dates import DateFormatter
matlab_file = './data/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = read_matfile(matlab_file)
datas = np.column_stack((timestamp, pwv))
df = pd.DataFrame(data=datas, columns=['timestamps', 'pwv']).set_index(['timestamps'])
start_index = 73513
train_length = 10000
test_length = 50
train = df[start_index:start_index+train_length]
test = df[start_index+train_length:start_index+train_length+test_length]
y_hat_avg = test.copy()
print('Computation started')
fit1 = ExponentialSmoothing(np.asarray(train['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
y_hat_avg['Holt_Winter'] = fit1.forecast(len(test))
print('Computation completed')
fig = plt.figure(1, figsize=(10, 5))
plt.plot(train['pwv'][-150:], 'b:', label='Train')
plt.plot(test['pwv'], 'r--', label='Test')
plt.plot(y_hat_avg['Holt_Winter'], 'k-', label='Predicted')
plt.legend(loc='best', fontsize=18)
fig.autofmt_xdate()
formatter = DateFormatter('%d-%m-%y %H:%M')
plt.gca().xaxis.set_major_formatter(formatter)
plt.grid(True)
plt.xlabel('Timestamps', fontsize=14)
plt.ylabel('Precipitable Water Vapor (in mm)', fontsize=14)
fig.tight_layout()
save_name = './results/73513-example.pdf'
fig.savefig(save_name)
plt.show()