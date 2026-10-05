import os
import numpy as np
from scipy.spatial.distance import cdist
from prettytable import PrettyTable
from DataHandler import load_embeddings
b1 = os.path.join('embeddings', 'input_embeddings.txt')
b2 = os.path.join('embeddings', 'output_embeddings.txt')
b5, word2idx, idx2word, b3 = load_embeddings(b1)
b6, b4, b4, b4 = load_embeddings(b2)
b5 = b5 / np.linalg.norm(b5, axis=1, keepdims=True)
b6 = b6 / np.linalg.norm(b6, axis=1, keepdims=True)
def fonk1(words_list):
    b7 = [word2idx[word] for word in words_list]
    return b7
def fonk2(b18, b19):
    if b19 >= len(b18):
        return [b18]
    b8 = []
    for k in range(int(len(b18) / b19)):
        b8.append(b18[k * b19: (k + 1) * b19])
    if len(b18) % b19 != 0:
        b8.append(b18[(k + 1) * b19:])
    return b8
def fonk3(ang_path):
    b9 = open(ang_path, "r").read().strip().split('\n')
    b10 = []
    b11 = None
    for line in b9:
        if line.startswith(":"):
            b11 = line.lower().split()[1]
        else:
            b12 = line.split()
            b10.append((b11, b12[0], b12[1], b12[2], b12[3]))
    b13 = set([question[0] for question in b10])
    b14 = set([b11 for b11 in b13 if b11.startswith('gram')])
    b15 = set([b11 for b11 in b13 if b11 not in b14])
    b16 = [question[1:] for question in b10 if question[0] in b14]
    b17 = [question[1:] for question in b10 if question[0] in b15]
    return b16, b17
b16, b17 = fonk3(os.path.join('evaluation data', 'analogy', 'EN-GOOGLE.txt'))
b18 = {'Syntactic': b16, 'Semantic': b17}
def fonk4(b18, idx2vec, b19 = 1000):
    b20 = PrettyTable(['Category', 'Acc', 'Total', 'Missing'])
    for b11 in b18:
        b21 = b18[b11]
        a1 = 0
        b22 = []
        for question in b21:
            if all(word in b3 for word in question):
                b22.append(question)
            else:
                a1 += 1
        b23 = []
        b24 = []
        for mini_questions in fonk2(b22, b19):
            b25 = np.array(mini_questions)
            word1, word2, word3, b26 = b25[:, 0], b25[:, 1], b25[:, 2], b25[:, 3]
            b27 = fonk1(list(word1))
            b28 = fonk1(list(word2))
            b29 = fonk1(list(word3))
            b30 = fonk1(list(b26))
            b31 = idx2vec[b27]
            b32 = idx2vec[b28]
            b33 = idx2vec[b29]
            b34 = b32 - b31 + b33
            b35 = 1 - cdist(b34, idx2vec, 'cosine')
            b35[:, 0] = -1
            b36 = np.argmax(b35, axis=1)
            b23 += list(b36)
            b24 += b30
        b24 = np.array(b24)
        b23 = np.array(b23)
        b37 = (b23 == b24)
        b38 = round(np.sum(b37) / len(b37) * 100, 2)
        b20.add_row([b11, b38, len(b21), a1])
    print(b20)
print('\nResults of input embeddings:')
fonk4(b18, b5, b19 = 1000)
print('\nResults of output embeddings:')
fonk4(b18, b6, b19 = 1000)