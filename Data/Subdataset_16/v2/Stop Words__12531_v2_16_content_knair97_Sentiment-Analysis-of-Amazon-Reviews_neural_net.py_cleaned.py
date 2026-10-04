import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import matplotlib.pyplot as plt
def fonk1(b15, b16):
    print('Reading training data')
    b1 = np.loadtxt(b15, skiprows=1)
    b2 = b1[:, 0]
    b3 = b1[:, 1:]
    print('Reading testing data')
    b4 = np.loadtxt(b16, skiprows=1)
    b5 = b3[-1000:]
    b6 = b2[-1000:]
    b3 = b3[:-1000]
    b2 = b2[:-1000]
    return b3, b2, b5, b6, b4
def fonk2(input_dim, dropout_rate):
    b7 = Sequential()
    b7.add(Dense(1000, b8 = 'relu', input_dim=input_dim))
    b7.add(Dropout(dropout_rate))
    b7.add(Dense(800, b8 = 'relu'))
    b7.add(Dropout(dropout_rate))
    b7.add(Dense(200, b8 = 'relu'))
    b7.add(Dropout(dropout_rate))
    b7.add(Dense(1, b8 = 'sigmoid'))
    return b7
def fonk3(b7, b3, b2, x_val, y_val, dropout_rate):
    b9 = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    b7.compile(b10 = 'binary_crossentropy', optimizer=b9, metrics=['b24'])
    b7.fit(b3, b2, b11 = (x_val, y_val), epochs=20, batch_size=128)
    return b7
def fonk4(b7, b3, b2, x_val, y_val):
    b12 = b7.evaluate(b3, b2, batch_size=128)
    b13 = b7.evaluate(x_val, y_val, batch_size=128)
    return b12[1], b13[1]
def fonk5(b20, b19, b18):
    plt.plot(b20, b18, b14 = 'Validation Accuracy')
    plt.plot(b20, b19, b14 = 'Training Accuracy')
    plt.xlabel('Dropout Rate')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('neural_net_dropout.png')
def fonk6(predictions, b17):
    print('Writing predictions')
    with open(b17, 'w') as f:
        f.write('Id,Prediction\n')
        for idx, pred in enumerate(predictions, 1):
            f.write(f'{idx},{int(pred[0])}\n')
def fonk7():
    b15 = 'training_data.txt'
    b16 = 'b4.txt'
    b17 = 'neural_net_pred.txt'
    b3, b2, b5, b6, b4 = fonk1(b15, b16)
    b18 = []
    b19 = []
    b20 = np.arange(0, 1, 0.1)
    for dropout_rate in b20:
        b7 = fonk2(input_dim=b3.shape[1], dropout_rate=dropout_rate)
        b7 = fonk3(b7, b3, b2, b5, b6, dropout_rate)
        train_acc, b21 = fonk4(b7, b3, b2, b5, b6)
        b18.append(b21)
        b19.append(train_acc)
        print(f'Validation b24: {b21}')
    fonk5(b20, b19, b18)
    b22 = b20[np.argmax(b18)]
    b23 = b18[np.argmax(b18)]
    print(f'Test b24 = {b23} maximized at dropout percentage = {b22}')
    b25 = b7.predict_classes(b4)
    fonk6(b25, b17)
if b26 = = '__main__':
    fonk7()