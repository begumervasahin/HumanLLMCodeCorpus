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
def fonk1(b41, prediction):
    b1 = pd.Series(b41)
    b2 = pd.Series(prediction)
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
        b6 = pm.ARIMA(b8=b8)
        b6.fit(b4)
        print('working on', i+1, 'of', test_len, '-- ' + str(int(100 * (i + 1) / test_len)) + '% complete')
        b9.append(b6.predict()[0])
        b4.append(b5[i])
    b10 = mean_squared_error(b5, b9)
    b11 = b10 ** 0.5
    b12 = fonk1(pd.Series(b5), pd.Series(b9))
    return b9, b10, b11, b12
def fonk3(b3, train_len, test_len, b13 = 4):
    b3 = b3.tail(test_len + train_len).reset_index(drop=True)
    b14 = pd.DataFrame({'the b3': b3.values})
    b15 = b14.values
    b16 = MinMaxScaler(feature_range=(0, 1))
    b17 = b16.fit_transform(b15)
    b18 = []
    b19 = []
    b20 = []
    for i in range(b13, train_len):
        b18.append(b17[i - b13:i, 0])
        b19.append(b17[i, 0])
    for i in range(train_len, len(b17)):
        b20.append(b17[i - b13:i, 0])
    b18 = np.array(b18)
    b19 = np.array(b19)
    b18 = np.reshape(b18, (b18.shape[0], b18.shape[1], 1))
    b20 = np.array(b20)
    b20 = np.reshape(b20, (b20.shape[0], b20.shape[1], 1))
    b6 = Sequential()
    b6.add(LSTM(b21 = b13, return_sequences=True, input_shape=(b18.shape[1], 1)))
    b6.add(LSTM(b21 = int(b13/2)))
    b6.add(Dense(1, b22 = 'sigmoid'))
    b6.compile(b23 = 'mean_squared_error', optimizer='adam')
    b24 = EarlyStopping(monitor='b23', mode='min', verbose=1, patience=5)
    b6.fit(b18, b19, b25 = 500, batch_size=1, verbose=2, callbacks=[b24])
    b9 = b6.predict(b20)
    b9 = b16.inverse_transform(b9).tolist()
    b26 = []
    for i in range(len(b9)):
        b26.extend(b9[i])
    b9 = b26
    b10 = mean_squared_error(b3.tail(len(b9)).values, b9)
    b11 = b10 ** 0.5
    b12 = fonk1(b3.tail(len(b9)).reset_index(drop=True), pd.Series(b9))
    return b9, b10, b11, b12
if b27 = = '__main__':
    b3 = pd.read_csv('YOUR-DATA-HERE.csv', index_col=0, header=0).tail(1500).reset_index(drop=True)
    b28 = ['SMA', 'EMA', 'WMA', 'DEMA', 'KAMA', 'MIDPOINT', 'MIDPRICE', 'T3', 'TEMA', 'TRIMA']
    b29 = {ma: abstract.Function(ma) for ma in b28}
    b30 = {'period': []}
    for i in range(4, 100):
        b30['period'].append(i)
        for ma in b28:
            b31 = b29[ma](b3[:-252], i).tail(60)
            b32 = kurtosis(b31, fisher=False)
            b30.setdefault(ma, []).append(b32)
    b30 = pd.DataFrame(b30)
    b30.to_csv('b30.csv')
    b33 = {}
    for ma in b28:
        b34 = np.abs(b30[ma] - 3)
        b14 = pd.DataFrame({'b34': b34, 'period': b30['period']})
        b14 = b14.sort_values(by=['b34'], ascending=True).reset_index(drop=True)
        if b14.at[0, 'b34'] < 3 * 0.05:
            b33[ma] = b14.at[0, 'period']
        else:
            print(ma + ' is not viable, best K greater or less than 3 +/-5%')
    print('\nOptimized periods:', b33)
    b35 = {}
    for ma in b33:
        b36 = b29[ma](b3, b33[ma])
        b37 = b3['close'] - b36
        print('\nWorking on ' + ma + ' b9')
        try:
            low_vol_prediction, low_vol_mse, low_vol_rmse, b38 = fonk2(b36, 1000, 252)
        except:
            print('ARIMA error, skipping to next MA type')
            continue
        high_vol_prediction, high_vol_mse, high_vol_rmse, b39 = fonk3(b37, 1000, 252)
        b40 = pd.Series(low_vol_prediction) + pd.Series(high_vol_prediction)
        b10 = mean_squared_error(b40.values, b3['close'].tail(252).values)
        b11 = b10 ** 0.5
        b12 = fonk1(b3['close'].tail(252).reset_index(drop=True), b40)
        b41 = b3['close'].tail(252).values
        b42 = []
        b43 = []
        for i in range(1, len(b40)):
            if b40[i] > b41[i-1] and b41[i] > b41[i-1]:
                b42.append(1)
            elif b40[i] < b41[i-1] and b41[i] < b41[i-1]:
                b42.append(1)
            else:
                b42.append(0)
            if b40[i] > b40[i-1] and b41[i] > b41[i-1]:
                b43.append(1)
            elif b40[i] < b40[i-1] and b41[i] < b41[i-1]:
                b43.append(1)
            else:
                b43.append(0)
        b44 = np.mean(b42)
        b45 = np.mean(b43)
        b35[ma] = {'b36': {'prediction': low_vol_prediction, 'b10': low_vol_mse,
                                      'b11': low_vol_rmse, 'b12': b38},
                          'b37': {'prediction': high_vol_prediction, 'b10': high_vol_mse,
                                       'b11': high_vol_rmse},
                          'final': {'prediction': b40.values.tolist(), 'b10': b10,
                                    'b11': b11, 'b12': b12},
                          'accuracy': {'prediction vs close': b44, 'prediction vs prediction': b45}}
        with open('simulation_data.json', 'w') as fp:
            json.dump(b35, fp)
    for ma in b35.keys():
        print('\n' + ma)
        print('Prediction vs Close:\t\t' + str(round(100*b35[ma]['accuracy']['prediction vs close'], 2))
              + '% Accuracy')
        print('Prediction vs Prediction:\t' + str(round(100*b35[ma]['accuracy']['prediction vs prediction'], 2))
              + '% Accuracy')
        print('MSE:\t', b35[ma]['final']['b10'],
              '\nRMSE:\t', b35[ma]['final']['b11'],
              '\nMAPE:\t', b35[ma]['final']['b12'])