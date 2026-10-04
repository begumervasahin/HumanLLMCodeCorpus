import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras import optimizers
import matplotlib.pyplot as plt
print('Reading training b1')
b1 = np.loadtxt('training_data.txt', skiprows=1)
b2 = b1[:, 0]
b3 = b1[:, 1:]
print('Reading testing b1')
b4 = np.loadtxt('b4.txt', skiprows=1)
b5 = b3[-1000:]
b6 = b2[-1000:]
b3 = b3[:-1000]
b2 = b2[:-1000]
b7 = []
b8 = []
b9 = []
for i in np.arange(0, 1, 0.1):
    b10 = Sequential()
    b10.add(Dense(1000, b11 = 'relu', input_dim=b3.shape[1]))
    b10.add(Dropout(i))
    b10.add(Dense(800, b11 = 'relu'))
    b10.add(Dropout(i))
    b10.add(Dense(200, b11 = 'relu'))
    b10.add(Dropout(i))
    b10.add(Dense(1, b11 = 'sigmoid'))
    b12 = optimizers.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    b10.compile(b13 = 'binary_crossentropy', optimizer=b12, metrics=['b18'])
    b10.fit(b3, b2, b14 = (b5, b6), epochs=20, batch_size=128)
    b15 = b10.evaluate(b5, b6, batch_size=128)
    b16 = b10.evaluate(b3, b2, batch_size=128)
    print('Val b18:', b15[1])
    b7.append(b15[1])
    b8.append(b16[1])
    b9.append(i)
plt.plot(b9, b7, b17 = 'Testing Error')
plt.plot(b9, b8, b17 = 'Training Error')
plt.xlabel('Dropout percentage')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('neural_net_dropout.png')
print('Test b18 = %g maximized at dropout percentage = %g' % (b7[np.argmax(b7)], b9[np.argmax(b7)]))
b19 = b10.predict_classes(b4)
print('Writing predictions')
with open('neural_net_pred.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for it, pred in enumerate(b19, 1):
        f.write('%d,%d\n' % (it, int(pred[0])))