import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from read_matfile import read_matfile
def fonk1(b28):
    timestamp, b1 = read_matfile(b28)
    print('Imported the MATLAB file')
    b2 = np.column_stack((timestamp, b1))
    return pd.DataFrame(b2, b3 = ['timestamps', 'b1']).set_index('timestamps')
def fonk2(y_true, y_pred):
    return np.sqrt(np.mean((y_pred - y_true) ** 2))
def fonk3(b29, b30, b31, a1):
    b4 = len(b29)
    b5 = np.zeros((len(b31), len(b30)))
    for i, lead_time in enumerate(b30):
        for j, previous_time in enumerate(b31):
            b6 = int(lead_time / 5)
            b7 = int(previous_time / 5)
            b8 = []
            for _ in range(a1):
                b9 = b4 - (b7 + b6)
                b10 = random.randint(0, b9)
                print(f'From start index of {b10}')
                print(f'Computing for lead b11 = {lead_time} mins with history of {previous_time} mins')
                b12 = b29[b10:b10 + b7]
                b13 = b29[b10 + b7:b10 + b7 + b6]
                b14 = b13.copy()
                print('Computation started')
                b15 = ExponentialSmoothing(
                    np.asarray(b12['b1']),
                    b16 = 288,
                    b17 = 'add',
                    b18 = 'add'
                ).b15()
                b14['Holt_Winter'] = b15.forecast(len(b13))
                print('Computation completed')
                b19 = fonk2(b14['b1'], b14['Holt_Winter'])
                b8.append(b19)
            b5[j, i] = np.mean(b8)
            print(b5)
    return b5
def fonk4(b5, b20 = './results/rmse_matrix_for_grid.npy'):
    np.save(b20, b5)
def fonk5(b5, b30, b31):
    no_of_y_components, b21 = b5.shape
    b22 = b30
    b23 = b31
    fig, b24 = plt.subplots()
    b25 = b24.imshow(b5, cmap=plt.cm.coolwarm)
    b24.set_xticks(np.arange(b21))
    b24.set_xticklabels(b22)
    b24.set_yticks(np.arange(no_of_y_components))
    b24.set_yticklabels(b23)
    plt.xlabel('Lead Times (in mins)', b26 = 12)
    plt.ylabel('Historical Data (in mins)', b26 = 12)
    b27 = fig.colorbar(b25, ticks=[b5.min(), b5.max()], orientation='vertical')
    b27.b24.set_yticklabels(['Low', 'High'])
    fig.tight_layout()
    fig.savefig('./results/rmse.pdf')
    plt.show()
def fonk6():
    b28 = './b2/PWV_2010from_WS_2_withGradient.mat'
    b29 = fonk1(b28)
    b30 = np.arange(5, 30, 5)
    b31 = np.arange(12000, 2000, -2000)
    a1 = 10
    b5 = fonk3(b29, b30, b31, a1)
    fonk4(b5)
    fonk5(b5, b30, b31)
if b32 = = '__main__':
    fonk6()