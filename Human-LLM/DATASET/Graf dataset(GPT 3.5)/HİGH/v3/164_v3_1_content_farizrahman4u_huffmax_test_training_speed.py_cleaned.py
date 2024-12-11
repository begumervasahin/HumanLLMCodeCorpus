import time
import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential, Model
from huffmax import Huffmax
def fonk1(a2, b6, a1):
    b1 = np.random.random((a2, b6))
    b2 = np.random.randint(0, a1, size=(a2, 1))
    b3 = np.zeros((a2, a1))
    for i in range(a2):
        b4 = np.random.randint(0, a1)
        b3[i, b4] = 1
    return b1, b2, b3
def fonk2(b1, b3, b6, a1, b9):
    b5 = Sequential()
    b5.add(Dense(b6 = b6, units=a1, activation='softmax'))
    b5.compile(b7 = 'mse', optimizer='sgd')
    b5.predict(b1[:1])
    b8 = time.time()
    b5.fit(b1, b3, b9 = b9)
    b10 = time.time()
    b11 = b10 - b8
    del b5
    return b11
def fonk3(b1, b2, b6, a1, b9, mode):
    b12 = Input((b6,))
    b13 = Input((1,))
    b14 = Huffmax(a1, verbose=True, mode=mode)([b12, b13])
    b15 = Model(inputs=[b12, b13], outputs=b14)
    b15.compile(b7 = 'mse', optimizer='sgd')
    b15.predict([b1[:1], b2[:1]])
    b8 = time.time()
    b15.fit([b1, b2], np.ones((len(b1), 1)), b9 = b9)
    b10 = time.time()
    b11 = b10 - b8
    return b11
def fonk4():
    b9 = 32
    b6 = 100
    a1 = 100000
    a2 = 10000
    b16 = {}
    b1, b2, b3 = fonk1(a2, b6, a1)
    b17 = fonk2(b1, b3, b6, a1, b9)
    b16['Softmax'] = b17
    for mode in [0, 1]:
        b18 = fonk3(b1, b2, b6, a1, b9, mode)
        b16[f'Huffmax (mode {mode})'] = b18
    for key, value in b16.items():
        print(f'{key}: {value}')
if b19 = = "__main__":
    fonk4()