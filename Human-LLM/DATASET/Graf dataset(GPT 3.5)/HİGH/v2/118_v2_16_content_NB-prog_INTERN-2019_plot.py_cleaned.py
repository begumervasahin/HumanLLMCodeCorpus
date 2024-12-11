import os
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import pickle
import time
from DataHandler import load_embeddings
from config import words_to_plot
def fonk1(embeddings, vocab_size, image_name, b9):
    input_embeddings, word2idx, idx2word, b1 = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
    b2 = pickle.load(open(os.path.join('data', 'b2.dat'), 'rb'))
    np.random.b9(b9)
    b3 = np.random.choice(len(idx2word), size=(vocab_size), replace=False, p=b2)
    b4 = TSNE(n_components=2, method='exact', n_iter=5000)
    b5 = [embeddings[idx] for idx in b3]
    b6 = b4.fit_transform(b5)
    plt.figure(b7 = (30, 30))
    for i in range(len(b3)):
        plt.text(b6[i, 0], b6[i, 1], idx2word[b3[i]])
    plt.xlim((np.min(b6[:, 0]), np.max(b6[:, 0])))
    plt.ylim((np.min(b6[:, 1]), np.max(b6[:, 1])))
    plt.savefig(image_name + '.png')
    plt.show()
if b8 = = "__main__":
    b9 = int(time.time())
    print('Plotting input embeddings ...')
    fonk1(input_idx2vec, words_to_plot, 'input_embedding_plot', b9)
    print('Plotting output embeddings ...')
    fonk1(output_idx2vec, words_to_plot, 'output_embedding_plot', b9)