import time
import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential, Model
from huffmax import Huffmax
a1 = 32
a2 = 100
a3 = 100000
a4 = 10000
b1 = {}
b2 = np.random.random((a4, a2))
b3 = np.zeros((a4, a3))
for i in range(a4):
    b3[i, np.random.randint(0, a3)] = 1
b4 = np.random.randint(0, a3, size=(a4, 1))
def fonk1(input_dim, num_classes):
    b5 = Sequential([
        Dense(b6 = num_classes, input_dim=input_dim, activation='softmax')
    ])
    b5.compile(b7 = 'mse', optimizer='sgd')
    return b5
def fonk2(input_dim, num_classes, mode):
    b8 = Input(shape=(input_dim,))
    b9 = Input(shape=(1,))
    b10 = Huffmax(num_classes, verbose=True, mode=mode)([b8, b9])
    b5 = Model(inputs=[b8, b9], outputs=b10)
    b5.compile(b7 = 'mse', optimizer='sgd')
    return b5
def fonk3(b5, b2, Y, model_name):
    b5.predict(b2[:1])
    b11 = time.time()
    b5.fit(b2, Y, b12 = a1)
    b1[model_name] = time.time() - b11
b13 = fonk1(a2, a3)
fonk3(b13, b2, b3, 'Softmax')
for mode in [0, 1]:
    b14 = fonk2(a2, a3, mode)
    fonk3(b14, [b2, b4], np.ones((a4, 1)), f'Huffmax (mode {mode})')
for model_name, exec_time in b1.items():
    print(f'{model_name} : {exec_time:.2f} seconds')