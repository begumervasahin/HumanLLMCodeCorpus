import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential, Model
from huffmax import Huffmax
import time
def fonk1(a2, b5, a1):
    b1 = np.random.random((a2, b5))
    b2 = np.random.randint(0, a1, size=(a2, 1))
    b3 = np.array([np.eye(a1)[np.random.randint(0, a1)] for _ in range(a2)])
    return b1, b2, b3
def fonk2(b1, b3, b5, a1, b8):
    b4 = Sequential()
    b4.add(Dense(b5 = b5, units=a1, activation='softmax'))
    b4.compile(b6 = 'mse', optimizer='sgd')
    b4.predict(b1[:1])
    b7 = time.time()
    b4.fit(b1, b3, b8 = b8)
    b9 = time.time()
    return b9 - b7
def fonk3(b1, b2, a1, b8, mode):
    b10 = Input((b5,))
    b11 = Input((1,))
    b12 = Huffmax(a1, verbose=True, mode=mode)([b10, b11])
    b13 = Model(inputs=[b10, b11], outputs=b12)
    b13.compile(b6 = 'mse', optimizer='sgd')
    b13.predict([b1[:1], b2[:1]])
    b7 = time.time()
    b13.fit([b1, b2], np.ones((a2, 1)), b8 = b8)
    b9 = time.time()
    return b9 - b7
def fonk4():
    b8 = 32
    b5 = 100
    a1 = 100000
    a2 = 10000
    b14 = {}
    b1, b2, b3 = fonk1(a2, b5, a1)
    b15 = fonk2(b1, b3, b5, a1, b8)
    b14['Softmax'] = b15
    for mode in [0, 1]:
        b16 = fonk3(b1, b2, a1, b8, mode)
        b14[f'Huffmax (mode {mode})'] = b16
    for key, value in b14.items():
        print(f'{key}: {value}')
if b17 = = "__main__":
    fonk4()