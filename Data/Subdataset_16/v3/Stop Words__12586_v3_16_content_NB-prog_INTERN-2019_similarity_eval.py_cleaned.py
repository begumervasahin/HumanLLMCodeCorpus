import os
import numpy as np
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
def fonk1():
    b1 = os.path.join('embeddings', 'input_embeddings.txt')
    b2 = os.path.join('embeddings', 'output_embeddings.txt')
    input_idx2vec, word2idx, idx2word, b3 = load_embeddings(b1)
    output_idx2vec, b4, b4, b4 = load_embeddings(b2)
    return input_idx2vec, output_idx2vec, word2idx, idx2word, b3
def fonk2(b5, b6):
    return 1 - spatial.distance.cosine(b5, b6)
def fonk3(word1, word2, idx2vec, word2idx):
    b5 = idx2vec[word2idx[word1]]
    b6 = idx2vec[word2idx[word2]]
    return fonk2(b5, b6)
def fonk4(b13, idx2vec, word2idx, b3):
    b7 = PrettyTable(['File Name', 'Rho', 'Total', 'Missing'])
    for filename in os.listdir(b13):
        b8 = os.path.join(b13, filename)
        with open(b8, 'r') as file:
            b9 = file.read().strip().split('\n')
        actual_similarities, b10 = [], []
        a1 = 0
        for line in b9:
            word1, word2, b11 = line.split()
            if word1 in b3 and word2 in b3:
                actual_similarities.append(float(b11))
                b12 = fonk3(word1, word2, idx2vec, word2idx)
                b10.append(b12)
            else:
                a1 += 1
        rho, b4 = spearmanr(b10, actual_similarities)
        b7.add_row([filename, round(rho, 4), len(b9), a1])
    print(b7)
def fonk5():
    input_idx2vec, output_idx2vec, word2idx, idx2word, b3 = fonk1()
    b13 = os.path.join('evaluation data', 'similarity')
    print('\nResults of input embeddings:')
    fonk4(b13, input_idx2vec, word2idx, b3)
    print('\nResults of output embeddings:')
    fonk4(b13, output_idx2vec, word2idx, b3)
if b14 = = "__main__":
    fonk5()