import time
import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential, Model
from huffmax import Huffmax
BATCH_SIZE = 32
INPUT_DIM = 100
NB_CLASSES = 100000
NB_SAMPLES = 10000
execution_times = {}
X = np.random.random((NB_SAMPLES, INPUT_DIM))
Y_softmax = np.zeros((NB_SAMPLES, NB_CLASSES))
for i in range(NB_SAMPLES):
    Y_softmax[i, np.random.randint(0, NB_CLASSES)] = 1
Y_huffmax = np.random.randint(0, NB_CLASSES, size=(NB_SAMPLES, 1))
softmax_model = Sequential()
softmax_model.add(Dense(units=NB_CLASSES, input_dim=INPUT_DIM, activation='softmax'))
softmax_model.compile(loss='mse', optimizer='sgd')
softmax_model.predict(X[:1])
start_time = time.time()
softmax_model.fit(X, Y_softmax, batch_size=BATCH_SIZE)
end_time = time.time()
execution_times['Softmax'] = end_time - start_time
del softmax_model
for mode in [0, 1]:
    vector_input = Input(shape=(INPUT_DIM,))
    target_class_input = Input(shape=(1,))
    probability = Huffmax(NB_CLASSES, verbose=True, mode=mode)([vector_input, target_class_input])
    huffmax_model = Model(inputs=[vector_input, target_class_input], outputs=probability)
    huffmax_model.compile(loss='mse', optimizer='sgd')
    huffmax_model.predict([X[:1], Y_huffmax[:1]])
    start_time = time.time()
    huffmax_model.fit([X, Y_huffmax], np.ones((NB_SAMPLES, 1)), batch_size=BATCH_SIZE)
    end_time = time.time()
    execution_times[f'Huffmax (mode {mode})'] = end_time - start_time
for key, value in execution_times.items():
    print(f'{key} : {value:.2f} seconds')