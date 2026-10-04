import keras
from keras.datasets import reuters
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import to_categorical
(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=None, test_split=0.2)
word_index = reuters.get_word_index(path="reuters_word_index.json")
num_classes = max(y_train) + 1
index_to_word = {value: key for key, value in word_index.items()}
first_article = ' '.join([index_to_word.get(x, '?') for x in x_train[0]])
print('First news article in the training set:')
print(first_article)
print('Class:', y_train[0])
max_words = 10000
tokenizer = Tokenizer(num_words=max_words)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
print('Sample training data (binary matrix):')
print(x_train[0])
print('Length of sample training data:', len(x_train[0]))
print('Sample training label:', y_train[0])
print('Length of sample training label:', len(y_train[0]))
def build_model(input_shape, num_classes):
    model = Sequential()
    model.add(Dense(512, input_shape=(input_shape,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))
    return model
model = build_model(max_words, num_classes)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print('Model metrics:', model.metrics_names)
batch_size = 32
epochs = 3
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.1)
score = model.evaluate(x_test, y_test, batch_size=batch_size, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])