import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
def fonk1(y_true, y_pred):
    return np.mean(np.abs((y_pred - y_true) / y_true)) * 100
def fonk2(data, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if isinstance(data, list) else data.shape[1]
    b3 = pd.DataFrame(data)
    b7, b4 = [], []
    for b5 in range(b1, 0, -1):
        b7.append(b3.shift(b5))
        b4 += [('var%d(t-%d)' % (j+1, b5)) for j in range(b2)]
    for b5 in range(0, n_out):
        b7.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [('var%d(t)' % (j+1)) for j in range(b2)]
        else:
            b4 += [('var%d(t+%d)' % (j+1, b5)) for j in range(b2)]
    b6 = pd.concat(b7, b11=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
b9 = pd.read_csv('your_dataset.csv')
a1 = 1
a2 = 1
b10 = fonk2(b9, a1, 1)
b10.drop(b10.b7[-a2:], b11 = 1, b8=True)
b12 = b10.b12
b13 = int(len(b12) * 0.7)
train, b14 = b12[:b13, :], b12[b13:, :]
b17, b15 = train[:, :-1], train[:, -1]
b18, b16 = b14[:, :-1], b14[:, -1]
b17 = b17.reshape((b17.shape[0], 1, b17.shape[1]))
b18 = b18.reshape((b18.shape[0], 1, b18.shape[1]))
b19 = Sequential()
b19.add(LSTM(50, b20 = (b17.shape[1], b17.shape[2])))
b19.add(Dense(1))
b19.compile(b21 = 'mae', optimizer='adam')
b22 = b19.fit(b17, b15, epochs=50, batch_size=72, validation_data=(b18, b16), verbose=2, shuffle=False)
b23 = b19.predict(b18)
b24 = fonk1(b16, b23)
print('Test MAPE: %.3f' % b24)
plt.plot(b22.b22['b21'], b25 = 'Train')
plt.plot(b22.b22['val_loss'], b25 = 'Test')
plt.title('Model b21')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
plt.show()