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
a8 = 24
a9 = 1
a10 = 2
b2 = (a8, a9, a10)
b3 = np.random.randn(b1, a3)
b4 = b3[:33600]
b5 = b3[a2:]
b4 = b4.reshape(-1, a1, a3)
b5 = b5.reshape(-1, a2, a4)
b6 = Input(shape=(a1, a3))
b7 = LSTM(50)(b6)
b8 = Dense(a2)(b7)
b9 = Model(inputs=b6, outputs=b8)
b10 = Adam(a7=a7)
b9.compile(b10 = b10, loss='mse')
b9.fit(b4, b5, a5 = a5, epochs=a6)
