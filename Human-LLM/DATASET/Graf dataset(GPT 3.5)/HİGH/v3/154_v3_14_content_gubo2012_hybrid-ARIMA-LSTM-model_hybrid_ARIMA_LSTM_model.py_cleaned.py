import pandas as pd
import numpy as np
from scipy.stats import kurtosis
from pmdarima import auto_arima
import pmdarima as pm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.callbacks import EarlyStopping
from talib import abstract
import json
def fonk1(b42, b9):
    b1 = pd.Series(b42)
    b2 = pd.Series(b9)
    return 100 * np.mean(np.abs((b1 - b2)) / b1)
def fonk2(b3, train_len, test_len):
    b3 = b3.tail(test_len + train_len).reset_index(drop=True)
    b4 = b3.head(train_len).values.tolist()
    b5 = b3.tail(test_len).values.tolist()
    b6 = auto_arima(b4, max_p=3, max_q=3, seasonal=False, trace=True,
                       b7 = 'ignore', suppress_warnings=True)
    b6.fit(b4)
    b8 = b6.get_params()['b8']
    print('ARIMA b8:', b8, '\n')
    b9 = []
    for i in range(len(b5)):
        b10 = pm.ARIMA(b8=b8)
        b10.fit(b4)
        print(f'Working on {i+1} of {test_len} -- {int(100 * (i + 1) / test_len)}% complete')
        b9.append(b10.predict()[0])
        b4.append(b5[i])
    b11 = mean_squared_error(b5, b9)
    b12 = b11 ** 0.5
    b13 = fonk1(pd.Series(b5), pd.Series(b9))
    return b9, b11, b12, b13
def fonk3(b3, train_len, test_len, b14 = 4):
    b3 = b3.tail(test_len + train_len).reset_index(drop=True)
    b15 = pd.DataFrame({'the b3': b3.values})
    b16 = b15.values
    b17 = MinMaxScaler(feature_range=(0, 1))
    b18 = b17.fit_transform(b16)
    b20, b21, b19 = [], [], []
    for i in range(b14, train_len):
        b20.append(b18[i - b14:i, 0])
        b21.append(b18[i, 0])
    for i in range(train_len, len(b18)):
        b19.append(b18[i - b14:i, 0])
    b20 = np.array(b20)
    b21 = np.array(b21)
    b20 = np.reshape(b20, (b20.shape[0], b20.shape[1], 1))
    b19 = np.array(b19)
    b19 = np.reshape(b19, (b19.shape[0], b19.shape[1], 1))
    b6 = Sequential()
    b6.add(LSTM(b22 = b14, return_sequences=True, input_shape=(b20.shape[1], 1)))
    b6.add(LSTM(b22 = int(b14/2)))
    b6.add(Dense(1, b23 = 'sigmoid'))
    b6.compile(b24 = 'mean_squared_error', optimizer='adam')
    b25 = EarlyStopping(monitor='b24', mode='min', verbose=1, patience=5)
    b6.fit(b20, b21, b26 = 500, batch_size=1, verbose=2, callbacks=[b25])
    b9 = b6.predict(b19)
    b9 = b17.inverse_transform(b9).tolist()
    b27 = []
    for i in range(len(b9)):
        b27.extend(b9[i])
    b9 = b27
    b11 = mean_squared_error(b3.tail(len(b9)).values, b9)
    b12 = b11 ** 0.5
    b13 = fonk1(b3.tail(len(b9)).reset_index(drop=True), pd.Series(b9))
    return b9, b11, b12, b13
if b28 = = '__main__':
    b3 = pd.read_csv('YOUR-DATA-HERE.csv', index_col=0, header=0).tail(1500).reset_index(drop=True)
    b29 = ['SMA', 'EMA', 'WMA', 'DEMA', 'KAMA', 'MIDPOINT', 'MIDPRICE', 'T3', 'TEMA', 'TRIMA']
    b30 = {ma: abstract.Function(ma) for ma in b29}
    b31 = {'period': []}
    for i in range(4, 100):
        b31['period'].append(i)
        for ma in b29:
            b32 = b30[ma](b3[:-252], i).tail(60)
            b33 = kurtosis(b32, fisher=False)
            if ma not in b31.keys():
                b31[ma] = []
            b31[ma].append(b33)
    b31 = pd.DataFrame(b31)
    b31.to_csv('b31.csv')
    b34 = {}
    for ma in b29:
        b35 = np.abs(b31[ma] - 3)
        b15 = pd.DataFrame({'b35': b35, 'period': b31['period']})
        b15 = b15.sort_values(by=['b35'], ascending=True).reset_index(drop=True)
        if b15.at[0, 'b35'] < 3 * 0.05:
            b34[ma] = b15.at[0, 'period']
        else:
            print(f'{ma} is not viable, best K greater or less than 3 +/-5%')
    print('\nOptimized periods:', b34)
    b36 = {}
    for ma in b34:
        b37 = b30[ma](b3, b34[ma])
        b38 = b3['close'] - b37
        print(f'\nWorking on {ma} predictions')
        try:
            low_vol_prediction, low_vol_mse, low_vol_rmse, b39 = fonk2(b37, 1000, 252)
        except:
            print('ARIMA error, skipping to next MA type')
            continue
        high_vol_prediction, high_vol_mse, high_vol_rmse, b40 = fonk3(b38, 1000, 252)
        b41 = pd.Series(low_vol_prediction) + pd.Series(high_vol_prediction)
        b11 = mean_squared_error(b41.values, b3['close'].tail(252).values)
        b12 = b11 ** 0.5
        b13 = fonk1(b3['close'].tail(252).reset_index(drop=True), b41)
        b42 = b3['close'].tail(252).values
        b43 = [1 if b41[i] > b42[i-1] and b42[i] > b42[i-1] or
                          b41[i] < b42[i-1] and b42[i] < b42[i-1] else 0
                    for i in range(1, len(b41))]
        b44 = [1 if b41[i] > b41[i-1] and b42[i] > b42[i-1] or
                          b41[i] < b41[i-1] and b42[i] < b42[i-1] else 0
                    for i in range(1, len(b41))]
        b45 = np.mean(b43)
        b46 = np.mean(b44)
        b36[ma] = {'b37': {'b9': low_vol_prediction, 'b11': low_vol_mse,
                                      'b12': low_vol_rmse, 'b13': b39},
                          'b38': {'b9': high_vol_prediction, 'b11': high_vol_mse,
                                       'b12': high_vol_rmse},
                          'final': {'b9': b41.values.tolist(), 'b11': b11,
                                    'b12': b12, 'b13': b13},
                          'accuracy': {'b9 vs close': b45, 'b9 vs b9': b46}}
        with open('simulation_data.json', 'w') as fp:
            json.dump(b36, fp)
    for ma in b36.keys():
        print(f'\n{ma}')
        print(f'Prediction vs Close:\t\t{round(100*b36[ma]["accuracy"]["b9 vs close"], 2)}% Accuracy')
        print(f'Prediction vs Prediction:\t{round(100*b36[ma]["accuracy"]["b9 vs b9"], 2)}% Accuracy')
        print(f'MSE:\t{b36[ma]["final"]["b11"]}\nRMSE:\t{b36[ma]["final"]["b12"]}\nMAPE:\t{b36[ma]["final"]["b13"]}')