import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import pickle
import time
from DataHandler import load_embeddings
from config import words_to_plot
def fonk1(file_path):
    b1 = []
    b2 = {}
    b3 = []
    b4 = set()
    with open(file_path, 'r') as f:
        for idx, line in enumerate(f):
            b5 = line.split()
            b6 = b5[0]
            b7 = np.array(b5[1:], dtype='float32')
            b1.append(b7)
            b2[b6] = idx
            b3.append(b6)
            b4.add(b6)
    return np.array(b1), b2, b3, b4
def fonk2(embeddings, vocab_size, image_name, b16):
    np.random.b16(b16)
    b8 = np.random.choice(len(b3), size=vocab_size, replace=False, p=b15)
    b9 = TSNE(n_components=2, n_iter=5000)
    b10 = [embeddings[idx] for idx in b8]
    b11 = b9.fit_transform(b10)
    plt.figure(b12 = (30, 30))
    for i in range(len(b8)):
        plt.text(b11[i, 0], b11[i, 1], b3[b8[i]])
    plt.xlim((np.min(b11[:, 0]), np.max(b11[:, 0])))
    plt.ylim((np.min(b11[:, 1]), np.max(b11[:, 1])))
    plt.savefig(f'{image_name}.png')
if b13 = = "__main__":
    input_idx2vec, b2, b3, b4 = fonk1(os.path.join('embeddings', 'input_embeddings.txt'))
    output_idx2vec, b14, b14, b14 = fonk1(os.path.join('embeddings', 'output_embeddings.txt'))
    b15 = pickle.load(open(os.path.join('data', 'b15.dat'), 'rb'))
    b16 = int(time.time())
    print('Plotting input embeddings ...')
    fonk2(input_idx2vec, words_to_plot, 'input_embedding_plot', b16)
    print('Plotting output embeddings ...')
    fonk2(output_idx2vec, words_to_plot, 'output_embedding_plot', b16)