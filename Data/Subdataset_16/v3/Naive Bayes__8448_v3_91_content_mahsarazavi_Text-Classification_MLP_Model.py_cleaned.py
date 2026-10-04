import keras
from keras.datasets import reuters
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import to_categorical
def fonk1():
    (b5, b7), (b6, b8) = reuters.load_data(b1 = None, test_split=0.2)
    b2 = max(b7) + 1
    print(f'Number of classes: {b2}')
    return (b5, b7), (b6, b8), b2
def fonk2(b5, b7, word_index):
    b3 = {value: key for key, value in word_index.items()}
    print(' '.join([b3.get(x, '?') for x in b5[0]]))
    print(f'Label: {b7[0]}')
def fonk3(b5, b6, b7, b8, b17):
    b4 = Tokenizer(b1=b17)
    b5 = b4.sequences_to_matrix(b5, mode='binary')
    b6 = b4.sequences_to_matrix(b6, mode='binary')
    b7 = to_categorical(b7, b2)
    b8 = to_categorical(b8, b2)
    print(f'First training example (binary vector): {b5[0]}')
    print(f'Length of first training example: {len(b5[0])}')
    print(f'First training label (one-hot vector): {b7[0]}')
    print(f'Length of first training label: {len(b7[0])}')
    return b5, b6, b7, b8
def fonk4(b5, b7, b6, b8, b17, b2, b9 = 3, batch_size=32):
    b10 = Sequential()
    b10.add(Dense(512, b11 = (b17,)))
    b10.add(Activation('relu'))
    b10.add(Dropout(0.5))
    b10.add(Dense(b2))
    b10.add(Activation('softmax'))
    b10.compile(b12 = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    print(f'Metrics names: {b10.metrics_names}')
    b13 = b10.fit(b5, b7, batch_size=batch_size, b9=b9, verbose=1, validation_split=0.1)
    b14 = b10.evaluate(b6, b8, batch_size=batch_size, verbose=1)
    print(f'Test b12: {b14[0]}')
    print(f'Test accuracy: {b14[1]}')
if b15 = = '__main__':
    (b5, b7), (b6, b8), b2 = fonk1()
    fonk2(b5, b7, reuters.get_word_index(b16 = "reuters_word_index.json"))
    b5, b6, b7, b8 = fonk3(b5, b6, b7, b8, b17=10000)
    fonk4(b5, b7, b6, b8, b17 = 10000, b2=b2, b9=3, batch_size=32)