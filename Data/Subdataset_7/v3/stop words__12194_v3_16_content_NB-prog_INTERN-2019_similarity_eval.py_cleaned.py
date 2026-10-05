import os
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
def fonk1(b6, b7):
    return 1 - spatial.distance.cosine(b6, b7)
def fonk2(b13, idx2vec, b14):
    b1 = PrettyTable(['File Name', 'Spearman Rho', 'Total Pairs', 'Missing Pairs'])
    for filename in os.listdir(b13):
        with open(os.path.join(b13, filename), 'r') as file:
            b2 = file.read().strip().split('\n')
        b3 = []
        b4 = []
        a1 = 0
        for line in b2:
            word1, word2, b5 = line.split()
            if word1 in b14 and word2 in b14:
                b3.append(float(b5))
                b6 = idx2vec[word2idx[word1]]
                b7 = idx2vec[word2idx[word2]]
                b8 = fonk1(b6, b7)
                b4.append(b8)
            else:
                a1 += 1
        b9 = round(spearmanr(b4, b3)[0], 4)
        b1.add_row([filename, b9, len(b2), a1])
    print(b1)
if b10 = = "__main__":
    b11 = os.path.join('embeddings', 'input_embeddings.txt')
    b12 = os.path.join('embeddings', 'output_embeddings.txt')
    b13 = os.path.join('evaluation data', 'similarity')
    input_idx2vec, word2idx, idx2word, b14 = load_embeddings(b11)
    output_idx2vec, b15, b15, b15 = load_embeddings(b12)
    print('\nResults of input embeddings:')
    fonk2(b13, input_idx2vec, b14)
    print('\nResults of output embeddings:')
    fonk2(b13, output_idx2vec, b14)