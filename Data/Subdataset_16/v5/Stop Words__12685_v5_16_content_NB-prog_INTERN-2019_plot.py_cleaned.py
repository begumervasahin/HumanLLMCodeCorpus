import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import pickle
import time
from DataHandler import load_embeddings
from config import words_to_plot
b1 = os.path.join('embeddings', 'input_embeddings.txt')
b2 = os.path.join('embeddings', 'output_embeddings.txt')
b3 = os.path.join('data', 'b6.dat')
input_idx2vec, word2idx, idx2word, b4 = load_embeddings(b1)
output_idx2vec, b5, b5, b5 = load_embeddings(b2)
b6 = pickle.load(open(b3, 'rb'))
def fonk1(embeddings, vocab_size, image_name, b12):
    np.random.b12(b12)
    b7 = np.random.choice(len(idx2word), size=vocab_size, replace=False, p=b6)
    b8 = TSNE(n_components=2, method='exact', n_iter=5000)
    b9 = [embeddings[idx] for idx in b7]
    b10 = b8.fit_transform(b9)
    plt.figure(b11 = (30, 30))
    for i, idx in enumerate(b7):
        plt.text(b10[i, 0], b10[i, 1], idx2word[idx])
    plt.xlim(np.min(b10[:, 0]), np.max(b10[:, 0]))
    plt.ylim(np.min(b10[:, 1]), np.max(b10[:, 1]))
    plt.savefig(f'{image_name}.png')
b12 = int(time.time())
print('Plotting input embeddings ...')
fonk2(input_idx2vec, words_to_plot, 'input_embedding_plot', b12)
print('Plotting output embeddings ...')
fonk2(output_idx2vec, words_to_plot, 'output_embedding_plot', b12)
import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import pickle
import time
from DataHandler import load_embeddings
from config import words_to_plot
b1 = os.path.join('embeddings', 'input_embeddings.txt')
b2 = os.path.join('embeddings', 'output_embeddings.txt')
b3 = os.path.join('data', 'b6.dat')
input_idx2vec, word2idx, idx2word, b4 = load_embeddings(b1)
output_idx2vec, b5, b5, b5 = load_embeddings(b2)
b6 = pickle.load(open(b3, 'rb'))
def fonk2(embeddings, vocab_size, image_name, b12):
    np.random.b12(b12)
    b7 = np.random.choice(len(idx2word), size=vocab_size, replace=False, p=b6)
    b8 = TSNE(n_components=2, method='exact', n_iter=5000)
    b9 = [embeddings[idx] for idx in b7]
    b10 = b8.fit_transform(b9)
    plt.figure(b11 = (30, 30))
    for i, idx in enumerate(b7):
        plt.text(b10[i, 0], b10[i, 1], idx2word[idx])
    plt.xlim(np.min(b10[:, 0]), np.max(b10[:, 0]))
    plt.ylim(np.min(b10[:, 1]), np.max(b10[:, 1]))
    plt.savefig(f'{image_name}.png')
b12 = int(time.time())
print('Plotting input embeddings ...')
fonk2(input_idx2vec, words_to_plot, 'input_embedding_plot', b12)
print('Plotting output embeddings ...')
fonk2(output_idx2vec, words_to_plot, 'output_embedding_plot', b12)