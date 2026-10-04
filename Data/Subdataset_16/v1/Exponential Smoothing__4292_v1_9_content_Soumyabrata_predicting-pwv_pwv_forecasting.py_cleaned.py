import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from statsmodels.tsa.api import ExponentialSmoothing
from read_matfile import read_matfile
def fonk1(b13):
    timestamp, b1 = read_matfile(b13)
    b2 = np.column_stack((timestamp, b1))
    return pd.DataFrame(b2, b3 = ['timestamps', 'b1']).set_index('timestamps')
def fonk2(train_data, b4 = 288):
    b5 = ExponentialSmoothing(
        np.asarray(train_data),
        b4 = b4,
        b6 = 'add',
        b7 = 'add'
    ).fit()
    return b5
def fonk3(b15, b16, b17, save_path):
    b8 = plt.figure(figsize=(10, 5))
    plt.plot(b15[-150:], 'b:', b9 = 'Train')
    plt.plot(b16, 'r--', b9 = 'Test')
    plt.plot(b17, 'k-', b9 = 'Predicted')
    plt.legend(b10 = 'best', b12=18)
    b8.autofmt_xdate()
    b11 = DateFormatter('%d-%m-%y %H:%M')
    plt.gcf().axes[0].xaxis.set_major_formatter(b11)
    plt.grid(True)
    plt.xlabel('Timestamps', b12 = 14)
    plt.ylabel('Precipitable Water Vapor (in mm)', b12 = 14)
    b8.tight_layout()
    b8.savefig(save_path)
    plt.show()
def fonk4():
    b13 = './b2/PWV_2010from_WS_2_withGradient.mat'
    b14 = fonk1(b13)
    a1 = 73513
    b15 = b14[a1:a1 + 10000]
    b16 = b14[a1 + 10000:a1 + 10000 + 50]
    print('Computation started')
    b5 = fonk2(b15['b1'])
    b17 = b5.forecast(len(b16))
    print('Computation completed')
    b18 = b16.copy()
    b18['Holt_Winter'] = b17
    fonk3(b15['b1'], b16['b1'], b18['Holt_Winter'], './results/73513-example.pdf')
if b19 = = '__main__':
    fonk4()