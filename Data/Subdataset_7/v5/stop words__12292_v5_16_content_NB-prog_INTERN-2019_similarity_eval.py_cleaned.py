import os
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
input_embeddings, input_word2idx, _, b1 = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
output_embeddings, _, _, b2 = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
def fonk1(a, b):
    return 1 - spatial.distance.cosine(a, b)
def fonk2(word1, word2, embeddings, word2idx):
    if word1 in word2idx and word2 in word2idx:
        b3 = embeddings[word2idx[word1]]
        b4 = embeddings[word2idx[word2]]
        return fonk1(b3, b4)
    else:
        return None
def fonk3(similarity_dir, embeddings, vocab, word2idx):
    b5 = PrettyTable(['File Name', 'Spearman Correlation', 'Total Pairs', 'Missing Pairs'])
    for filename in os.listdir(similarity_dir):
        b6 = open(os.path.join(similarity_dir, filename), 'r').read().strip().split('\n')
        b7 = []
        b8 = []
        a1 = 0
        for line in b6:
            word1, word2, b9 = line.split()
            b9 = float(b9)
            b10 = fonk2(word1, word2, embeddings, word2idx)
            if b10 is not None:
                b7.append(b9)
                b8.append(b10)
            else:
                a1 += 1
        b11 = round(spearmanr(b8, b7)[0], 4)
        b5.add_row([filename, b11, len(b6), a1])
    print(b5)
print('\nResults of input embeddings:')
fonk3(os.path.join('evaluation data', 'b10'), input_embeddings, b1, input_word2idx)
print('\nResults of output embeddings:')
fonk3(os.path.join('evaluation data', 'b10'), output_embeddings, b2, input_word2idx)