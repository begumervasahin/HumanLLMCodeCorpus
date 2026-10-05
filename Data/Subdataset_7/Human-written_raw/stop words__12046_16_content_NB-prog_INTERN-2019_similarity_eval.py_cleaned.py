import os
import numpy as np
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
input_idx2vec, word2idx, idx2word, b1 = load_embeddings(os.path.join('embeddings','input_embeddings.txt'))
output_idx2vec, b2, b2, b2 = load_embeddings(os.path.join('embeddings','output_embeddings.txt'))
def fonk1(b3, b4):
    return 1 - spatial.distance.cosine(b3, b4)
def fonk2(b3, b4, idx2vec):
    b3 = idx2vec[word2idx[b3]]
    b4 = idx2vec[word2idx[b4]]
    return fonk1(b3, b4)
def fonk3(sim_dir, idx2vec):
    b5 = PrettyTable(['File Name', 'Rho', 'Total', 'Missing'])
    for filename in os.listdir(sim_dir):
        b6 = open(os.path.join(sim_dir,filename),'r').read().strip().split('\n')
        b7 = []
        b8 = []
        a1 = 0
        for line in b6:
            word1, word2, b9 = line.split()
            if word1 in b1 and word2 in b1:
                b7.append(float(b9))
                b10 = fonk2(word1,word2, idx2vec)
                b8.append(b10)
            else:
                a1 += 1
        b11 = round(spearmanr(b8, b7)[0],4)
        b5.add_row([filename, b11, len(b6), a1])
    print(b5)
print('\nResults of input embeddings:')
fonk3(os.path.join('evaluation data', 'similarity'), input_idx2vec)
print('\nResults of output embeddings:')
fonk3(os.path.join('evaluation data', 'similarity'), output_idx2vec)