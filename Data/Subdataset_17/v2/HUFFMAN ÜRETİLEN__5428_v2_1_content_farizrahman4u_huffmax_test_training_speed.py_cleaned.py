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
    model = Sequential()
    model.add(Dense(units=num_classes, input_dim=input_dim, activation='softmax'))
    model.compile(loss='mse', optimizer='sgd')
    return model
def build_huffmax_model(input_dim, num_classes, mode):
    vector_input = Input(shape=(input_dim,))
    target_class_input = Input(shape=(1,))
    probability = Huffmax(num_classes, verbose=True, mode=mode)([vector_input, target_class_input])
    model = Model(inputs=[vector_input, target_class_input], outputs=probability)
    model.compile(loss='mse', optimizer='sgd')
    return model
softmax_model = build_softmax_model(INPUT_DIM, NUM_CLASSES)
softmax_model.predict(X[:1])
start_time = time.time()
softmax_model.fit(X, Y_softmax, batch_size=BATCH_SIZE)
execution_times['Softmax'] = time.time() - start_time
del softmax_model
for mode in [0, 1]:
    huffmax_model = build_huffmax_model(INPUT_DIM, NUM_CLASSES, mode)
    huffmax_model.predict([X[:1], Y_huffmax[:1]])
    start_time = time.time()
    huffmax_model.fit([X, Y_huffmax], np.ones((NUM_SAMPLES, 1)), batch_size=BATCH_SIZE)
    execution_times[f'Huffmax (mode {mode})'] = time.time() - start_time
for model_name, exec_time in execution_times.items():
    print(f'{model_name} : {exec_time:.2f} seconds')