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
def fonk1(b1, b2):
    b1 = pd.Series(b1)
    b2 = pd.Series(b2)
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
    b2 = []
    for i in range(len(b5)):
        b6 = pm.ARIMA(b8=b8)
        b6.fit(b4)
        print('working on', i+1, 'of', test_len, '-- ' + str(int(100 * (i + 1) / test_len)) + '% complete')
        b2.append(b6.predict()[0])
        b4.append(b5[i])
    b9 = mean_squared_error(b5, b2)
    b10 = b9 ** 0.5
    b11 = fonk1(pd.Series(b5), pd.Series(b2))
    return b2, b9, b10, b11
def fonk3(b3, train_len, test_len, b12 = 4):
    b3 = b3.tail(test_len + train_len).reset_index(drop=True)
    b13 = pd.DataFrame({'the b3': b3.values})
    b14 = b13.values
    b15 = MinMaxScaler(feature_range=(0, 1))
    b16 = b15.fit_transform(b14)
    b17 = []
    b18 = []
    b19 = []
    for i in range(b12, train_len):
        b17.append(b16[i - b12:i, 0])
        b18.append(b16[i, 0])
    for i in range(train_len, len(b16)):
        b19.append(b16[i - b12:i, 0])
    b17 = np.array(b17)
    b18 = np.array(b18)
    b17 = np.reshape(b17, (b17.shape[0], b17.shape[1], 1))
    b19 = np.array(b19)
    b19 = np.reshape(b19, (b19.shape[0], b19.shape[1], 1))
    b6 = Sequential()
    b6.add(LSTM(b20 = b12, return_sequences=True, input_shape=(b17.shape[1], 1)))
    b6.add(LSTM(b20 = int(b12/2)))
    b6.add(Dense(1, b21 = 'sigmoid'))
    b6.compile(b22 = 'mean_squared_error', optimizer='adam')
    b23 = EarlyStopping(monitor='b22', mode='min', verbose=1, patience=5)
    b6.fit(b17, b18, b24 = 500, batch_size=1, verbose=2, callbacks=[b23])
    b2 = b6.predict(b19)
    b2 = b15.inverse_transform(b2).tolist()
    b25 = []
    for i in range(len(b2)):
        b25.extend(b2[i])
    b2 = b25
    b9 = mean_squared_error(b3.tail(len(b2)).values, b2)
    b10 = b9 ** 0.5
    b11 = fonk1(b3.tail(len(b2)).reset_index(drop=True), pd.Series(b2))
    return b2, b9, b10, b11
if b26 = = '__main__':
    b3 = pd.read_csv('YOUR-DATA-HERE.csv', index_col=0, header=0).tail(1500).reset_index(drop=True)
    b27 = ['SMA', 'EMA', 'WMA', 'DEMA', 'KAMA', 'MIDPOINT', 'MIDPRICE', 'T3', 'TEMA', 'TRIMA']
    b28 = {}
    for ma in b27:
        b28[ma] = abstract.Function(ma)
    b29 = {'period': []}
    for i in range(4, 100):
        b29['period'].append(i)
        for ma in b27:
            b30 = b28[ma](b3[:-252], i).tail(60)
            b31 = kurtosis(b30, fisher=False)
            if ma not in b29.keys():
                b29[ma] = []
            b29[ma].append(b31)
    b29 = pd.DataFrame(b29)
    b29.to_csv('b29.csv')
    b32 = {}
    for ma in b27:
        b33 = np.abs(b29[ma] - 3)
        b13 = pd.DataFrame({'b33': b33, 'period': b29['period']})
        b13 = b13.sort_values(by=['b33'], ascending=True).reset_index(drop=True)
        if b13.at[0, 'b33'] < 3 * 0.05:
            b32[ma] = b13.at[0, 'period']
        else:
            print(ma + ' is not viable, best K greater or less than 3 +/-5%')
    print('\nOptimized periods:', b32)
    b34 = {}
    for ma in b32:
        b35 = b28[ma](b3, b32[ma])
        b36 = b3['close'] - b35
        print('\nWorking on ' + ma + ' predictions')
        try:
            low_vol_prediction, low_vol_mse, low_vol_rmse, b37 = fonk2(b35, 1000, 252)
        except:
            print('ARIMA error, skipping to next MA type')
            continue
        high_vol_prediction, high_vol_mse, high_vol_rmse, b38 = fonk3(b36, 1000, 252)
        b39 = pd.Series(low_vol_prediction) + pd.Series(high_vol_prediction)
        b9 = mean_squared_error(b39.values, b3['close'].tail(252).values)
        b10 = b9 ** 0.5
        b11 = fonk1(b3['close'].tail(252).reset_index(drop=True), b39)
        b1 = b3['close'].tail(252).values
        b40 = []
        b41 = []
        for i in range(1, len(b39)):
            if b39[i] > b1[i-1] and b1[i] > b1[i-1]:
                b40.append(1)
            elif b39[i] < b1[i-1] and b1[i] < b1[i-1]:
                b40.append(1)
            else:
                b40.append(0)
            if b39[i] > b39[i-1] and b1[i] > b1[i-1]:
                b41.append(1)
            elif b39[i] < b39[i-1] and b1[i] < b1[i-1]:
                b41.append(1)
            else:
                b41.append(0)
        b42 = np.mean(b40)
        b43 = np.mean(b41)
        b34[ma] = {'b35': {'b2': low_vol_prediction, 'b9': low_vol_mse,
                                      'b10': low_vol_rmse, 'b11': b37},
                          'b36': {'b2': high_vol_prediction, 'b9': high_vol_mse,
                                       'b10': high_vol_rmse},
                          'final': {'b2': b39.values.tolist(), 'b9': b9,
                                    'b10': b10, 'b11': b11},
                          'accuracy': {'b2 vs close': b42, 'b2 vs b2': b43}}
        with open('simulation_data.json', 'w') as fp:
            json.dump(b34, fp)
    for ma in b34.keys():
        print('\n' + ma)
        print('Prediction vs Close:\t\t' + str(round(100*b34[ma]['accuracy']['b2 vs close'], 2))
              + '% Accuracy')
        print('Prediction vs Prediction:\t' + str(round(100*b34[ma]['accuracy']['b2 vs b2'], 2))
              + '% Accuracy')
        print('MSE:\t', b34[ma]['final']['b9'],
              '\nRMSE:\t', b34[ma]['final']['b10'],
              '\nMAPE:\t', b34[ma]['final']['b11'])