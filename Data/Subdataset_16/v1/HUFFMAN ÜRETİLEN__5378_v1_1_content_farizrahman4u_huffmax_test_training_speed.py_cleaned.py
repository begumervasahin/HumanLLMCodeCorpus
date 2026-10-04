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
b5 = Sequential()
b5.add(Dense(b6 = a3, input_dim=a2, activation='softmax'))
b5.compile(b7 = 'mse', optimizer='sgd')
b5.predict(b2[:1])
b8 = time.time()
b5.fit(b2, b3, b9 = a1)
b10 = time.time()
b1['Softmax'] = b10 - b8
del b5
for mode in [0, 1]:
    b11 = Input(shape=(a2,))
    b12 = Input(shape=(1,))
    b13 = Huffmax(a3, verbose=True, mode=mode)([b11, b12])
    b14 = Model(inputs=[b11, b12], outputs=b13)
    b14.compile(b7 = 'mse', optimizer='sgd')
    b14.predict([b2[:1], b4[:1]])
    b8 = time.time()
    b14.fit([b2, b4], np.ones((a4, 1)), b9 = a1)
    b10 = time.time()
    b1[f'Huffmax (mode {mode})'] = b10 - b8
for key, value in b1.items():
    print(f'{key} : {value:.2f} seconds')