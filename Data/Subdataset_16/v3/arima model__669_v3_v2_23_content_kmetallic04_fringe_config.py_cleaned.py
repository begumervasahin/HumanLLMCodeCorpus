import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
a1 = 168
a2 = 168
b1 = 33600 + a2
a3 = 1
a4 = 1
a5 = 16
a6 = 100
a7 = 1e-3
P, D, b2 = 24, 1, 2
b3 = (P, D, b2)
b4 = np.random.randn(b1, a3)
b5 = b4[:33600]
b6 = b4[a2:]
b5 = b5.reshape(-1, a1, a3)
b6 = b6.reshape(-1, a2, a4)
def fonk1(input_shape):
    b7 = Input(shape=input_shape)
    b8 = LSTM(50)(b7)
    b9 = Dense(a2)(b8)
    b10 = Model(inputs=b7, outputs=b9)
    return b10
b10 = fonk1((a1, a3))
b11 = Adam(learning_rate=a7)
b10.compile(b11 = b11, loss='mse')
b10.fit(b5, b6, b12 = a5, epochs=a6)
