import time
import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential, Model
from huffmax import Huffmax
BATCH_SIZE = 32
INPUT_DIM = 100
NUM_CLASSES = 100000
NUM_SAMPLES = 10000
execution_times = {}
X = np.random.random((NUM_SAMPLES, INPUT_DIM))
Y_softmax = np.zeros((NUM_SAMPLES, NUM_CLASSES))
for i in range(NUM_SAMPLES):
    Y_softmax[i, np.random.randint(0, NUM_CLASSES)] = 1
Y_huffmax = np.random.randint(0, NUM_CLASSES, size=(NUM_SAMPLES, 1))
def build_softmax_model(input_dim, num_classes):
    model = Sequential([
        Dense(units=num_classes, input_dim=input_dim, activation='softmax')
    ])
    model.compile(loss='mse', optimizer='sgd')
    return model
def build_huffmax_model(input_dim, num_classes, mode):
    vector_input = Input(shape=(input_dim,))
    target_class_input = Input(shape=(1,))
    probability = Huffmax(num_classes, verbose=True, mode=mode)([vector_input, target_class_input])
    model = Model(inputs=[vector_input, target_class_input], outputs=probability)
    model.compile(loss='mse', optimizer='sgd')
    return model
def time_model_training(model, X, Y, model_name):
    model.predict(X[:1])
    start_time = time.time()
    model.fit(X, Y, batch_size=BATCH_SIZE)
    execution_times[model_name] = time.time() - start_time
softmax_model = build_softmax_model(INPUT_DIM, NUM_CLASSES)
time_model_training(softmax_model, X, Y_softmax, 'Softmax')
for mode in [0, 1]:
    huffmax_model = build_huffmax_model(INPUT_DIM, NUM_CLASSES, mode)
    time_model_training(huffmax_model, [X, Y_huffmax], np.ones((NUM_SAMPLES, 1)), f'Huffmax (mode {mode})')
for model_name, exec_time in execution_times.items():
    print(f'{model_name} : {exec_time:.2f} seconds')