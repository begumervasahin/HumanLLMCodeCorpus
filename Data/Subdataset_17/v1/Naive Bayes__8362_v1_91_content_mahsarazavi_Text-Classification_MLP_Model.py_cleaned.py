import keras
from keras.datasets import reuters
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import to_categorical
(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=None, test_split=0.2)
word_index = reuters.get_word_index(path="reuters_word_index.json")
num_classes = max(y_train) + 1
print(f'Number of classes: {num_classes}')
index_to_word = {value: key for key, value in word_index.items()}
print(' '.join([index_to_word.get(x, '?') for x in x_train[0]]))
print(f'Label: {y_train[0]}')
max_words = 10000
tokenizer = Tokenizer(num_words=max_words)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
print(f'First training example (binary vector): {x_train[0]}')
print(f'Length of first training example: {len(x_train[0])}')
print(f'First training label (one-hot vector): {y_train[0]}')
print(f'Length of first training label: {len(y_train[0])}')
model = Sequential()
model.add(Dense(512, input_shape=(max_words,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(f'Metrics names: {model.metrics_names}')
batch_size = 32
epochs = 3
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.1)
score = model.evaluate(x_test, y_test, batch_size=batch_size, verbose=1)
print(f'Test loss: {score[0]}')
print(f'Test accuracy: {score[1]}')