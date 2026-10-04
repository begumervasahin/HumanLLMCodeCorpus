import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from statsmodels.tsa.api import ExponentialSmoothing
from read_matfile import read_matfile
def fonk1(b14):
    timestamp, b1 = read_matfile(b14)
    b2 = np.column_stack((timestamp, b1))
    b3 = pd.DataFrame(b2, columns=['timestamps', 'b1'])
    b3.set_index('timestamps', b4 = True)
    return b3
def fonk2(train_data, b5 = 288):
    b6 = ExponentialSmoothing(
        train_data,
        b5 = b5,
        b7 = 'add',
        b8 = 'add'
    ).fit()
    return b6
def fonk3(b15, b16, b17, save_path):
    fig, b9 = plt.subplots(figsize=(10, 5))
    b9.plot(b15[-150:], 'b:', b10 = 'Train')
    b9.plot(b16, 'r--', b10 = 'Test')
    b9.plot(b17, 'k-', b10 = 'Predicted')
    b9.legend(b11 = 'best', b13=18)
    fig.autofmt_xdate()
    b12 = DateFormatter('%d-%m-%y %H:%M')
    b9.xaxis.set_major_formatter(b12)
    b9.grid(True)
    b9.set_xlabel('Timestamps', b13 = 14)
    b9.set_ylabel('Precipitable Water Vapor (in mm)', b13 = 14)
    fig.tight_layout()
    fig.savefig(save_path)
    plt.show()
def fonk4():
    b14 = './b2/PWV_2010from_WS_2_withGradient.mat'
    b3 = fonk1(b14)
    a1 = 73513
    b15 = b3.iloc[a1:a1 + 10000]
    b16 = b3.iloc[a1 + 10000:a1 + 10000 + 50]
    print('Computation started')
    b6 = fonk2(b15['b1'])
    b17 = b6.forecast(len(b16))
    print('Computation completed')
    fonk3(b15['b1'], b16['b1'], b17, './results/73513-example.pdf')
if b18 = = '__main__':
    fonk4()