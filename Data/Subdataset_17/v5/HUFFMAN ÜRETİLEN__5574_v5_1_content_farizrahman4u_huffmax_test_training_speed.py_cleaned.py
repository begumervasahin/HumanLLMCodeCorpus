import time
import numpy as np
from keras.layers import Dense, Input
from keras.models import Sequential, Model
from huffmax import Huffmax
BATCH_SIZE = 32
INPUT_DIM = 100
NB_CLASSES = 100000
NB_SAMPLES = 10000
training_times = {}
X = np.random.random((NB_SAMPLES, INPUT_DIM))
Y_huffmax = np.random.randint(0, NB_CLASSES, size=(NB_SAMPLES, 1))
Y_softmax = np.zeros((NB_SAMPLES, NB_CLASSES))
Y_softmax[np.arange(NB_SAMPLES), np.random.randint(0, NB_CLASSES, NB_SAMPLES)] = 1
def create_and_train_softmax_model():
    softmax_model = Sequential([
        Dense(units=NB_CLASSES, input_dim=INPUT_DIM, activation='softmax')
    ])
    softmax_model.compile(loss='mse', optimizer='sgd')
    softmax_model.predict(X[:1])
    start_time = time.time()
    softmax_model.fit(X, Y_softmax, batch_size=BATCH_SIZE)
    training_times['Softmax'] = time.time() - start_time
    del softmax_model
def create_and_train_huffmax_model(mode):
    vector_input = Input(shape=(INPUT_DIM,))
    target_class_input = Input(shape=(1,))
    probability_output = Huffmax(NB_CLASSES, verbose=True, mode=mode)([vector_input, target_class_input])
    huffmax_model = Model(inputs=[vector_input, target_class_input], outputs=probability_output)
    huffmax_model.compile(loss='mse', optimizer='sgd')
    huffmax_model.predict([X[:1], Y_huffmax[:1]])
    start_time = time.time()
    huffmax_model.fit([X, Y_huffmax], np.ones((NB_SAMPLES, 1)), batch_size=BATCH_SIZE)
    training_times[f'Huffmax (mode {mode})'] = time.time() - start_time
    del huffmax_model
create_and_train_softmax_model()
for mode in [0, 1]:
    create_and_train_huffmax_model(mode)
for model_name, elapsed_time in training_times.items():
    print(f'{model_name}: {elapsed_time:.2f} seconds')