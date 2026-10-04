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
b2 = np.random.randn(b1, a3)
b3 = b2[:33600]
b4 = b2[a2:]
b3 = b3.reshape(-1, a1, a3)
b4 = b4.reshape(-1, a2, a4)
def fonk1(input_shape, output_units):
    b5 = Input(shape=input_shape)
    b6 = LSTM(units=50)(b5)
    b7 = Dense(units=output_units)(b6)
    return Model(b8 = b5, outputs=b7)
b9 = fonk1(input_shape=(a1, a3), output_units=a2)
b10 = Adam(learning_rate=a7)
b9.compile(b10 = b10, loss='mse')
b9.fit(b3, b4, b11 = a5, epochs=a6)
