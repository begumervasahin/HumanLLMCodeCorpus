import keras
from keras.datasets import reuters
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
import numpy as np
(b7, b9), (b8, b10) = reuters.load_data(b1 = None, test_split=0.2)
b2 = reuters.get_word_index(path="reuters_word_index.json")
b3 = max(b9) + 1
b4 = {value: key for key, value in b2.items()}
b5 = ' '.join([b4.get(x - 3, '?') for x in b7[0]])
print('First sample words:', b5)
print('Label:', b9[0])
a1 = 10000
b6 = Tokenizer(b1=a1)
b7 = b6.sequences_to_matrix(b7, mode='binary')
b8 = b6.sequences_to_matrix(b8, mode='binary')
b9 = keras.utils.to_categorical(b9, b3)
b10 = keras.utils.to_categorical(b10, b3)
b11 = Sequential()
b11.add(Dense(512, b12 = (a1,)))
b11.add(Activation('relu'))
b11.add(Dropout(0.5))
b11.add(Dense(b3))
b11.add(Activation('softmax'))
b11.compile(b13 = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
a2 = 32
a3 = 3
b14 = b11.fit(b7, b9, a2=a2, a3=a3, verbose=1, validation_split=0.1)
b15 = b11.evaluate(b8, b10, a2=a2, verbose=1)
print('Test b13:', b15[0])
print('Test accuracy:', b15[1])