import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
SEQ_LENGTH = 168
OUTPUT_SEQ_LENGTH = 168
TOTAL_SEQUENCE_LENGTH = 33600 + OUTPUT_SEQ_LENGTH
INPUT_DIM = 1
OUTPUT_DIM = 1
BATCH_SIZE = 16
EPOCHS = 100
LEARNING_RATE = 1e-3
data = np.random.randn(TOTAL_SEQUENCE_LENGTH, INPUT_DIM)
X_train = data[:33600]
y_train = data[OUTPUT_SEQ_LENGTH:]
X_train = X_train.reshape(-1, SEQ_LENGTH, INPUT_DIM)
y_train = y_train.reshape(-1, OUTPUT_SEQ_LENGTH, OUTPUT_DIM)
def build_lstm_model(input_shape, output_shape, learning_rate):
    input_layer = Input(shape=input_shape)
    lstm_layer = LSTM(50)(input_layer)
    output_layer = Dense(output_shape[0])(lstm_layer)
    model = Model(inputs=input_layer, outputs=output_layer)
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='mse')
    return model
input_shape = (SEQ_LENGTH, INPUT_DIM)
output_shape = (OUTPUT_SEQ_LENGTH, OUTPUT_DIM)
model = build_lstm_model(input_shape, output_shape, LEARNING_RATE)
model.fit(X_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS)
print("Model training completed.")