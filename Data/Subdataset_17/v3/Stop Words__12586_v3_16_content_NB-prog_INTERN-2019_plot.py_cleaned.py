import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import pickle
import time
from DataHandler import load_embeddings
from config import words_to_plot
def load_embeddings(file_path):
    idx2vec = []
    word2idx = {}
    idx2word = []
    vocab = set()
    with open(file_path, 'r') as f:
        for idx, line in enumerate(f):
            values = line.split()
            word = values[0]
            vector = np.array(values[1:], dtype='float32')
            idx2vec.append(vector)
            word2idx[word] = idx
            idx2word.append(word)
            vocab.add(word)
    return np.array(idx2vec), word2idx, idx2word, vocab
def plot_embedding(embeddings, vocab_size, image_name, seed):
    np.random.seed(seed)
    idxs = np.random.choice(len(idx2word), size=vocab_size, replace=False, p=word_freq)
    tsne = TSNE(n_components=2, n_iter=5000)
    selected_embeddings = [embeddings[idx] for idx in idxs]
    two_dim_embeddings = tsne.fit_transform(selected_embeddings)
    plt.figure(figsize=(30, 30))
    for i, idx in enumerate(idxs):
        plt.text(two_dim_embeddings[i, 0], two_dim_embeddings[i, 1], idx2word[idx])
    plt.xlim((np.min(two_dim_embeddings[:, 0]), np.max(two_dim_embeddings[:, 0])))
    plt.ylim((np.min(two_dim_embeddings[:, 1]), np.max(two_dim_embeddings[:, 1])))
    plt.savefig(f'{image_name}.png')
def main():
    input_idx2vec, word2idx, idx2word, vocab = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
    output_idx2vec, _, _, _ = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
    word_freq = pickle.load(open(os.path.join('data', 'word_freq.dat'), 'rb'))
    seed = int(time.time())
    print('Plotting input embeddings ...')
    plot_embedding(input_idx2vec, words_to_plot, 'input_embedding_plot', seed)
    print('Plotting output embeddings ...')
    plot_embedding(output_idx2vec, words_to_plot, 'output_embedding_plot', seed)
if __name__ == "__main__":
    main()