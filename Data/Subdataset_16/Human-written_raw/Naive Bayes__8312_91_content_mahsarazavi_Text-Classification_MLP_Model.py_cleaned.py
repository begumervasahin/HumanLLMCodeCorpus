import keras
from keras.datasets import reuters
(b6, b8), (b7, b9) = reuters.load_data(b1 = None, test_split=0.2)
b2 = reuters.get_word_index(path="reuters_word_index.json")
print('
print('
b3 = max(b8) + 1
print('
b4 = {}
for key, value in b2.items():
    b4[value] = key
print(' '.join([b4[x] for x in b6[0]]))
print(b8[0])
from keras.preprocessing.text import Tokenizer
a1 = 10000
b5 = Tokenizer(b1=a1)
b6 = b5.sequences_to_matrix(b6, mode='binary')
b7 = b5.sequences_to_matrix(b7, mode='binary')
b8 = keras.utils.to_categorical(b8, b3)
b9 = keras.utils.to_categorical(b9, b3)
print(b6[0])
print(len(b6[0]))
print(b8[0])
print(len(b8[0]))
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
b10 = Sequential()
b10.add(Dense(512, b11 = (a1,)))
b10.add(Activation('relu'))
b10.add(Dropout(0.5))
b10.add(Dense(b3))
b10.add(Activation('softmax'))
b10.compile(b12 = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(b10.metrics_names)
['b12', 'acc']
a2 = 32
a3 = 3
b13 = b10.fit(b6, b8, a2=a2, a3=a3, verbose=1, validation_split=0.1)
b14 = b10.evaluate(b7, b9, a2=a2, verbose=1)
print('Test b12:', b14[0])
print('Test accuracy:', b14[1])