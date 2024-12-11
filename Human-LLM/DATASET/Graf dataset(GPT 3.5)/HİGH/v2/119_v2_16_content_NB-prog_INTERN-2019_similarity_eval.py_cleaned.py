import os
import numpy as np
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
def fonk1(a, b):
    return 1 - spatial.distance.cosine(a, b)
def fonk2(word1, word2, idx2vec):
    b1 = idx2vec[word2idx[word1]]
    b2 = idx2vec[word2idx[word2]]
    return fonk1(b1, b2)
def fonk3(similarity_directory, idx2vec):
    b3 = PrettyTable(['File Name', 'Spearman Rho', 'Total Pairs', 'Missing Pairs'])
    for filename in os.listdir(similarity_directory):
        b4 = open(os.path.join(similarity_directory, filename), 'r').read().strip().split('\n')
        b5 = []
        b6 = []
        a1 = 0
        for line in b4:
            word1, word2, b7 = line.split()
            if word1 in b11 and word2 in b11:
                b5.append(float(b7))
                b8 = fonk2(word1, word2, idx2vec)
                b6.append(b8)
            else:
                a1 += 1
        b9 = round(spearmanr(b6, b5)[0], 4)
        b3.add_row([filename, b9, len(b4), a1])
    print(b3)
if b10 = = "__main__":
    input_idx2vec, word2idx, idx2word, b11 = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
    output_idx2vec, b12, b12, b12 = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
    print('\nResults of input embeddings:')
    fonk3(os.path.join('evaluation data', 'similarity'), input_idx2vec)
    print('\nResults of output embeddings:')
    fonk3(os.path.join('evaluation data', 'similarity'), output_idx2vec)