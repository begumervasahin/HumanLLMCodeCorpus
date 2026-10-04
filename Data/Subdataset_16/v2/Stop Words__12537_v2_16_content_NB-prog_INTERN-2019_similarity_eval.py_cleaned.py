import os
import numpy as np
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
def fonk1():
    input_idx2vec, word2idx, idx2word, b1 = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
    output_idx2vec, b2, b2, b2 = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
    return input_idx2vec, output_idx2vec, word2idx, idx2word, b1
def fonk2(b3, b4):
    return 1 - spatial.distance.cosine(b3, b4)
def fonk3(word1, word2, idx2vec, word2idx):
    b3 = idx2vec[word2idx[word1]]
    b4 = idx2vec[word2idx[word2]]
    return fonk2(b3, b4)
def fonk4(sim_dir, idx2vec, word2idx, b1):
    b5 = PrettyTable(['File Name', 'Rho', 'Total', 'Missing'])
    for filename in os.listdir(sim_dir):
        with open(os.path.join(sim_dir, filename), 'r') as file:
            b6 = file.read().strip().split('\n')
        b7 = []
        b8 = []
        a1 = 0
        for line in b6:
            word1, word2, b9 = line.split()
            if word1 in b1 and word2 in b1:
                b7.append(float(b9))
                b8.append(fonk3(word1, word2, idx2vec, word2idx))
            else:
                a1 += 1
        rho, b2 = spearmanr(b8, b7)
        b5.add_row([filename, round(rho, 4), len(b6), a1])
    print(b5)
def fonk5():
    input_idx2vec, output_idx2vec, word2idx, idx2word, b1 = fonk1()
    print('\nResults of input embeddings:')
    fonk4(os.path.join('evaluation data', 'similarity'), input_idx2vec, word2idx, b1)
    print('\nResults of output embeddings:')
    fonk4(os.path.join('evaluation data', 'similarity'), output_idx2vec, word2idx, b1)
if b10 = = "__main__":
    fonk5()