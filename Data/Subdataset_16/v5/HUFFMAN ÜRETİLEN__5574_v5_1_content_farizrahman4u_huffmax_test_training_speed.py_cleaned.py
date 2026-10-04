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
b4 = np.zeros((a4, a3))
b4[np.arange(a4), np.random.randint(0, a3, a4)] = 1
def fonk1():
    b5 = Sequential([
        Dense(b6 = a3, input_dim=a2, activation='softmax')
    ])
    b5.compile(b7 = 'mse', optimizer='sgd')
    b5.predict(b2[:1])
    b8 = time.time()
    b5.fit(b2, b4, b9 = a1)
    b1['Softmax'] = time.time() - b8
    del b5
def fonk2(mode):
    b10 = Input(shape=(a2,))
    b11 = Input(shape=(1,))
    b12 = Huffmax(a3, verbose=True, mode=mode)([b10, b11])
    b13 = Model(inputs=[b10, b11], outputs=b12)
    b13.compile(b7 = 'mse', optimizer='sgd')
    b13.predict([b2[:1], b3[:1]])
    b8 = time.time()
    b13.fit([b2, b3], np.ones((a4, 1)), b9 = a1)
    b1[f'Huffmax (mode {mode})'] = time.time() - b8
    del b13
fonk1()
for mode in [0, 1]:
    fonk2(mode)
for model_name, elapsed_time in b1.items():
    print(f'{model_name}: {elapsed_time:.2f} seconds')