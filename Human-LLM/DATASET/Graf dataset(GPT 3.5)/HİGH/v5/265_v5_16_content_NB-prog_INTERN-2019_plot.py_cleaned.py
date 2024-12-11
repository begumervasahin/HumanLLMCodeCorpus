import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import pickle
import time
from DataHandler import load_embeddings
from config import words_to_plot
input_idx2vec, word2idx, idx2word, b1 = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
output_idx2vec, b2, b2, b2 = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
b3 = pickle.load(open(os.path.join('data', 'b3.dat'), 'rb'))
def fonk1(embeddings, vocab_size, image_name, b9):
    np.random.b9(b9)
    b4 = np.random.choice(len(idx2word), size=vocab_size, replace=False, p=b3)
    b5 = TSNE(n_components=2, method='exact', n_iter=5000)
    b6 = [embeddings[idx] for idx in b4]
    b7 = b5.fit_transform(b6)
    plt.figure(b8 = (30, 30))
    for i in range(len(b4)):
        plt.text(b7[i, 0], b7[i, 1], idx2word[b4[i]])
    plt.xlim((np.min(b7[:, 0]), np.max(b7[:, 0])))
    plt.ylim((np.min(b7[:, 1]), np.max(b7[:, 1])))
    plt.savefig(image_name + '.png')
b9 = int(time.time())
print('Plotting input embeddings ...')
fonk1(input_idx2vec, words_to_plot, 'input_embedding_plot', b9)
print('Plotting output embeddings ...')
fonk1(output_idx2vec, words_to_plot, 'output_embedding_plot', b9)