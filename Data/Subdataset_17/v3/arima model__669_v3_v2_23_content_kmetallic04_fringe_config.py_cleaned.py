import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
SEQUENCE_LENGTH = 168
OUTPUT_SEQUENCE_LENGTH = 168
TOTAL_SEQUENCE_LENGTH = 33600 + OUTPUT_SEQUENCE_LENGTH
INPUT_DIMENSION = 1
OUTPUT_DIMENSION = 1
BATCH_SIZE = 16
TRAINING_STEPS = 100
LEARNING_RATE = 1e-3
P, D, Q = 24, 1, 2
ORDER = (P, D, Q)
data = np.random.randn(TOTAL_SEQUENCE_LENGTH, INPUT_DIMENSION)
X_train = data[:33600]
y_train = data[OUTPUT_SEQUENCE_LENGTH:]
X_train = X_train.reshape(-1, SEQUENCE_LENGTH, INPUT_DIMENSION)
y_train = y_train.reshape(-1, OUTPUT_SEQUENCE_LENGTH, OUTPUT_DIMENSION)
def build_model(input_shape):
    input_layer = Input(shape=input_shape)
    lstm_layer = LSTM(50)(input_layer)
    output_layer = Dense(OUTPUT_SEQUENCE_LENGTH)(lstm_layer)
    model = Model(inputs=input_layer, outputs=output_layer)
    return model
model = build_model((SEQUENCE_LENGTH, INPUT_DIMENSION))
optimizer = Adam(learning_rate=LEARNING_RATE)
model.compile(optimizer=optimizer, loss='mse')
model.fit(X_train, y_train, batch_size=BATCH_SIZE, epochs=TRAINING_STEPS)
