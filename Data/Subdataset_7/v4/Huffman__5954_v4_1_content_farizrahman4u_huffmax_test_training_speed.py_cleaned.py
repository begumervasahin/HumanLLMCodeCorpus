import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential, Model
from huffmax import Huffmax
import time
a1 = 32
a2 = 100
a3 = 100000
a4 = 10000
b1 = {}
b2 = np.random.random((a4, a2))
b3 = np.random.randint(0, a3, size=(a4, 1))
b4 = np.array([np.eye(a3)[np.random.randint(0, a3)] for _ in range(a4)])
b5 = Sequential()
b5.add(Dense(a2 = a2, units=a3, activation='softmax'))
b5.compile(b6 = 'mse', optimizer='sgd')
b5.predict(b2[:1])
b7 = time.time()
b5.fit(b2, b4, a1 = a1)
b8 = time.time()
b1['Softmax'] = b8 - b7
del b5
for mode in [0, 1]:
    b9 = Input((a2,))
    b10 = Input((1,))
    b11 = Huffmax(a3, verbose=True, mode=mode)([b9, b10])
    b12 = Model(inputs=[b9, b10], outputs=b11)
    b12.compile(b6 = 'mse', optimizer='sgd')
    b12.predict([b2[:1], b3[:1]])
    b7 = time.time()
    b12.fit([b2, b3], np.ones((a4, 1)), a1 = a1)
    b8 = time.time()
    b1['Huffmax (mode ' + str(mode) + ')'] = b8 - b7
for key in b1.keys():
    print(key + ' : ' + str(b1[key]))