import numpy as np
from gensim.models import Word2Vec
from keras.layers import LSTM, Embedding, Dense, Dropout, GRU, BatchNormalization
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.optimizers import Adadelta
from keras.metrics import *
from matplotlib import pyplot as plt
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            sequence, label = line.strip().split('\t')
            data.append((sequence, label))
    return data
def convert_to_indices(data, char_mapping):
    indexed_data = []
    for sequence, label in data:
        indexed_sequence = [char_mapping[char] for char in sequence]
        indexed_data.append((indexed_sequence, label))
    return indexed_data
def save_data(data, prefix):
    x_data = np.array([item[0] for item in data])
    y_data = np.array([item[1] for item in data])
    np.save(f'{prefix}_data.npy', x_data)
    np.save(f'{prefix}_label.npy', y_data)
def one_hot_encode(labels):
    num_labels = len(set(labels))
    num_instances = len(labels)
    encoded_labels = np.zeros((num_instances, num_labels))
    for i, label in enumerate(labels):
        encoded_labels[i][int(label) - 1] = 1
    return encoded_labels
def build_embedding_matrix(word2vec_model, char_mapping, embedding_dims):
    embedding_matrix = np.zeros((len(char_mapping) + 1, embedding_dims))
    for char, index in char_mapping.items():
        if char in word2vec_model.wv:
            embedding_matrix[index] = word2vec_model.wv[char]
    return embedding_matrix
def build_model(embedding_layer, layer_type, dims):
    model = Sequential()
    model.add(embedding_layer)
    if layer_type == 'GRU_1':
        model.add(GRU(64, input_shape=(None, dims), activation='relu'))
    elif layer_type == 'GRU_2':
        model.add(GRU(128, input_shape=(None, dims), return_sequences=True))
        model.add(GRU(64))
    elif layer_type == 'LSTM_1':
        model.add(LSTM(64, input_shape=(None, dims)))
    elif layer_type == 'LSTM_2':
        model.add(LSTM(256, input_shape=(None, dims), activation='relu', return_sequences=True))
        model.add(LSTM(128, return_sequences=True))
        model.add(LSTM(64))
    return model
def train_model(model, x_train, y_train, batch_size, epochs, validation_split):
    model.compile(loss='categorical_crossentropy', optimizer=Adadelta(), metrics=['accuracy', f1score])
    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=validation_split, shuffle=True)
    return history
def plot_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Train vs Validation Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper right')
    plt.show()
def evaluate_model(model, x_test, y_test, batch_size):
    return model.evaluate(x_test, y_test, batch_size=batch_size)
def save_results(score, dim, layer, padding_len):
    np.save(f'result/word2vec_{dim}_{layer}_len{padding_len}.npy', score)
    with open(f'result/word2vec_{dim}_{layer}_len{padding_len}.txt', 'w') as file:
        file.write(f'Test Score: {score[0]}, Test Accuracy: {score[1]}, Test Recall: {score[2]}')
def run(dim, layer, train_size, padding_len):
    word2vec_model = Word2Vec.load('word2vec/word2vec_wx')
    embedding_dims = 256
    data_splits = ['train', 'test', 'val']
    char_mapping = {}
    for split in data_splits:
        data = load_data(f'data/zh_simplified_{split}.txt')
        for sequence, _ in data:
            for char in sequence:
                if char not in char_mapping:
                    char_mapping[char] = len(char_mapping)
        indexed_data = convert_to_indices(data, char_mapping)
        save_data(indexed_data, f'zh_simplified_word2vec_{split}')
    embedding_matrix = build_embedding_matrix(word2vec_model, char_mapping, embedding_dims)
    x_train = np.load('zh_simplified_word2vec_train_data.npy')
    y_train = np.load('zh_simplified_word2vec_train_label.npy')
    x_test = np.load('zh_simplified_word2vec_test_data.npy')
    y_test = np.load('zh_simplified_word2vec_test_label.npy')
    x_train = np.append(x_train, x_test)
    y_train = np.append(y_train, y_test)
    embedding_layer = Embedding(
        len(char_mapping) + 1,
        embedding_dims,
        weights=[embedding_matrix],
        input_length=padding_len,
        trainable=True
    )
    model_word2vec = build_model(embedding_layer, layer, dim)
    model_img2vec = Sequential([
        embedding_layer,
        BatchNormalization(axis=1),
        LSTM(256, input_shape=(None, dim), activation='tanh', return_sequences=True),
        LSTM(128, activation='tanh', return_sequences=True),
        LSTM(64)
    ])
    model = Sequential([
        model_img2vec,
        Dropout(0.5),
        Dense(12, activation='softmax')
    ])
    history = train_model(model, pad_sequences(x_train, maxlen=padding_len), one_hot_encode(y_train), batch_size=128, epochs=50, validation_split=1 - train_size)
    plot_loss(history)
    score = evaluate_model(model, pad_sequences(x_test, maxlen=padding_len), one_hot_encode(y_test), batch_size=128)
    print(f'Test Score: {score[0]}, Test Accuracy: {score[1]}')
    save_results(score, dim, layer, padding_len)
if __name__ == '__main__':
    dimensions = [256]
    layers = ['LSTM_2']
    train_size = [0.75]
    padding_lengths = [10]
    for dim in dimensions:
        for layer in layers:
            for size in train_size:
                for padding_len in padding_lengths:
                    run(dim, layer, size, padding_len)