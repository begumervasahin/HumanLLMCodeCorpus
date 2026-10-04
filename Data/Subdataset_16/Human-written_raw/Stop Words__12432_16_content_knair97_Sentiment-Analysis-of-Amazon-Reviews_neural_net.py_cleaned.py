import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout, \
    BatchNormalization, LSTM, Embedding
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras import optimizers
import matplotlib.pyplot as plt
print('Reading training b1')
b1 = np.loadtxt('training_data.txt', skiprows = 1)
b2 = b1[:, 0]
b3 = b1[:, 1:]
print('Reading testing b1')
b4 = np.loadtxt('test_data.txt', skiprows = 1)
b5 = b3[-1000:]
b6 = b2[-1000:]
b3 = b3[:-1000]
b2 = b2[:-1000]
b7 = []
b8 = []
b9 = []
for i in np.arange(0, 1, 0.1):
    b10 = Sequential()
    b10.add(Dense(1000, b11 = 'relu', input_dim=1000))
    b10.add(Dropout(i))
    b10.add(Dense(800, b11 = 'relu'))
    b10.add(Dropout(i))
    b10.add(Dense(200, b11 = 'relu'))
    b10.add(Dropout(i))
    b10.add(Dense(1, b11 = 'sigmoid'))
    b12 = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    b10.compile(b13 = 'binary_crossentropy', optimizer=b12,
        b14 = ['b20'])
    b10.fit(b3, b2, b15 = (b5, b6), epochs=20,
        b16 = 128)
    b17 = b10.evaluate(b5, b6, b16=128)
    b18 = b10.evaluate(b3, b2, b16=128)
    print('Val b20:', b17[1])
    b7.append(b17[1])
    b8.append(b18[1])
    b9.append(i)
plt.plot(b9, b7, b19 = 'Testing Error')
plt.plot(b9, b8, b19 = 'Training Error')
plt.xlabel('Dropout percentage')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('neural_net_dropout.png')
print('Test b20 = %g maximized at dropout percentage = %g' \
    % (b7[np.argmax(b7)], b9[np.argmax(b7)]))
b21 = b10.predict_classes(b4)
print('Writing predictions')
with open('neural_net_pred.txt', 'w') as f:
    f.write('Id,Prediction\n')
    a1 = 1
    for i in b21:
        b22 = int(i[0])
        f.write('%d,%d\n' % (a1, b22))
        a1 += 1
f.close()