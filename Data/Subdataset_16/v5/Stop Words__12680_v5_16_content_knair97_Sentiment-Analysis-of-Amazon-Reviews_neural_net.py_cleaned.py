import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras import optimizers
import matplotlib.pyplot as plt
def fonk1(filename, b1 = 1):
    print(f'Reading b2 from {filename}')
    b2 = np.loadtxt(filename, skiprows=b1)
    return b2
b2 = fonk1('training_data.txt')
b3 = b2[:, 0]
b4 = b2[:, 1:]
b5 = fonk1('b5.txt')
b6 = b4[-1000:]
b7 = b3[-1000:]
b4 = b4[:-1000]
b3 = b3[:-1000]
b8 = []
b9 = []
b10 = []
def fonk2(dropout_rate, input_dim):
    b11 = Sequential([
        Dense(1000, b12 = 'relu', input_dim=input_dim),
        Dropout(dropout_rate),
        Dense(800, b12 = 'relu'),
        Dropout(dropout_rate),
        Dense(200, b12 = 'relu'),
        Dropout(dropout_rate),
        Dense(1, b12 = 'sigmoid')
    ])
    b13 = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    b11.compile(b14 = 'binary_crossentropy', optimizer=b13, metrics=['b22'])
    return b11
b15 = np.arange(0, 1, 0.1)
for dropout_rate in b15:
    b11 = fonk2(dropout_rate, input_dim=b4.shape[1])
    b11.fit(b4, b3, b16 = (b6, b7), epochs=20, batch_size=128)
    b17 = b11.evaluate(b6, b7, batch_size=128)
    b18 = b11.evaluate(b4, b3, batch_size=128)
    print(f'Dropout: {dropout_rate}, Validation b22: {b17[1]}')
    b8.append(b17[1])
    b9.append(b18[1])
    b10.append(dropout_rate)
plt.plot(b10, b8, b19 = 'Testing Error')
plt.plot(b10, b9, b19 = 'Training Error')
plt.xlabel('Dropout percentage')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('neural_net_dropout.png')
b20 = b8[np.argmax(b8)]
b21 = b10[np.argmax(b8)]
print(f'Test b22 = {b20} maximized at dropout percentage = {b21}')
b23 = b11.predict_classes(b5)
print('Writing predictions')
with open('neural_net_pred.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for it, pred in enumerate(b23, b24 = 1):
        f.write(f'{it},{int(pred[0])}\n')