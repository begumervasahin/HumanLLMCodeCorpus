import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import pickle
import time
from DataHandler import load_embeddings
from config import words_to_plot
input_embeddings_path = os.path.join('embeddings', 'input_embeddings.txt')
output_embeddings_path = os.path.join('embeddings', 'output_embeddings.txt')
word_freq_path = os.path.join('data', 'word_freq.dat')
input_idx2vec, word2idx, idx2word, vocab = load_embeddings(input_embeddings_path)
output_idx2vec, _, _, _ = load_embeddings(output_embeddings_path)
word_freq = pickle.load(open(word_freq_path, 'rb'))
def plot_embedding(embeddings, vocab_size, image_name, seed):
    np.random.seed(seed)
    idxs = np.random.choice(len(idx2word), size=vocab_size, replace=False, p=word_freq)
    tsne = TSNE(n_components=2, method='exact', n_iter=5000)
    selected_embeddings = [embeddings[idx] for idx in idxs]
    reduced_embeddings = tsne.fit_transform(selected_embeddings)
    plt.figure(figsize=(30, 30))
    for i, idx in enumerate(idxs):
        plt.text(reduced_embeddings[i, 0], reduced_embeddings[i, 1], idx2word[idx])
    plt.xlim(np.min(reduced_embeddings[:, 0]), np.max(reduced_embeddings[:, 0]))
    plt.ylim(np.min(reduced_embeddings[:, 1]), np.max(reduced_embeddings[:, 1]))
    plt.savefig(f'{image_name}.png')
seed = int(time.time())
print('Plotting input embeddings ...')
plot_embedding(input_idx2vec, words_to_plot, 'input_embedding_plot', seed)
print('Plotting output embeddings ...')
plot_embedding(output_idx2vec, words_to_plot, 'output_embedding_plot', seed)
import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import pickle
import time
from DataHandler import load_embeddings
from config import words_to_plot
input_embeddings_path = os.path.join('embeddings', 'input_embeddings.txt')
output_embeddings_path = os.path.join('embeddings', 'output_embeddings.txt')
word_freq_path = os.path.join('data', 'word_freq.dat')
input_idx2vec, word2idx, idx2word, vocab = load_embeddings(input_embeddings_path)
output_idx2vec, _, _, _ = load_embeddings(output_embeddings_path)
word_freq = pickle.load(open(word_freq_path, 'rb'))
def plot_embedding(embeddings, vocab_size, image_name, seed):
    np.random.seed(seed)
    idxs = np.random.choice(len(idx2word), size=vocab_size, replace=False, p=word_freq)
    tsne = TSNE(n_components=2, method='exact', n_iter=5000)
    selected_embeddings = [embeddings[idx] for idx in idxs]
    reduced_embeddings = tsne.fit_transform(selected_embeddings)
    plt.figure(figsize=(30, 30))
    for i, idx in enumerate(idxs):
        plt.text(reduced_embeddings[i, 0], reduced_embeddings[i, 1], idx2word[idx])
    plt.xlim(np.min(reduced_embeddings[:, 0]), np.max(reduced_embeddings[:, 0]))
    plt.ylim(np.min(reduced_embeddings[:, 1]), np.max(reduced_embeddings[:, 1]))
    plt.savefig(f'{image_name}.png')
seed = int(time.time())
print('Plotting input embeddings ...')
plot_embedding(input_idx2vec, words_to_plot, 'input_embedding_plot', seed)
print('Plotting output embeddings ...')
plot_embedding(output_idx2vec, words_to_plot, 'output_embedding_plot', seed)