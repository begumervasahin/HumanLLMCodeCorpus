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
b3 = np.random.randint(0, a3, size=(a4, 1))
b4 = []
for _ in range(a4):
    b5 = np.zeros(a3)
    b5[np.random.randint(0, a3)] = 1
    b4.append(b5)
b4 = np.array(b4)
b6 = Sequential()
b6.add(Dense(a2 = a2, units=a3, activation='softmax'))
b6.compile(b7 = 'mse', optimizer='sgd')
b6.predict(b2[:1])
b8 = time.time()
b6.fit(b2, b4, a1 = a1)
b9 = time.time()
b1['Softmax'] = b9 - b8
del b6
for mode in [0, 1]:
    b10 = Input((a2,))
    b11 = Input((1,))
    b12 = Huffmax(a3, verbose=True, mode=mode)([b10, b11])
    b13 = Model(inputs=[b10, b11], outputs=b12)
    b13.compile(b7 = 'mse', optimizer='sgd')
    b13.predict([b2[:1], b3[:1]])
    b8 = time.time()
    b13.fit([b2, b3], np.ones((a4, 1)), a1 = a1)
    b9 = time.time()
    b1['Huffmax (mode ' + str(mode) + ')'] = b9 - b8
for key in b1.keys():
    print(key + ' : ' + str(b1[key]))