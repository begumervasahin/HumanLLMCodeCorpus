import keras
from keras.datasets import reuters
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import to_categorical
(b6, b8), (b7, b9) = reuters.load_data(b1 = None, test_split=0.2)
b2 = reuters.get_word_index(path="reuters_word_index.json")
b3 = max(b8) + 1
print(f'Number of classes: {b3}')
b4 = {value: key for key, value in b2.items()}
print(' '.join([b4.get(x, '?') for x in b6[0]]))
print(f'Label: {b8[0]}')
a1 = 10000
b5 = Tokenizer(b1=a1)
b6 = b5.sequences_to_matrix(b6, mode='binary')
b7 = b5.sequences_to_matrix(b7, mode='binary')
b8 = to_categorical(b8, b3)
b9 = to_categorical(b9, b3)
print(f'First training example (binary vector): {b6[0]}')
print(f'Length of first training example: {len(b6[0])}')
print(f'First training label (one-hot vector): {b8[0]}')
print(f'Length of first training label: {len(b8[0])}')
b10 = Sequential()
b10.add(Dense(512, b11 = (a1,)))
b10.add(Activation('relu'))
b10.add(Dropout(0.5))
b10.add(Dense(b3))
b10.add(Activation('softmax'))
b10.compile(b12 = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(f'Metrics names: {b10.metrics_names}')
a2 = 32
a3 = 3
b13 = b10.fit(b6, b8, a2=a2, a3=a3, verbose=1, validation_split=0.1)
b14 = b10.evaluate(b7, b9, a2=a2, verbose=1)
print(f'Test b12: {b14[0]}')
print(f'Test accuracy: {b14[1]}')