import os
import numpy as np
from scipy.spatial.distance import cdist
from prettytable import PrettyTable
from DataHandler import load_embeddings, pad_word
b3, word2idx, idx2word, b1 = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
b4, b2, b2, b2 = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
b3 = b3/((b3**2).sum(axis=1,keepdims=True))**0.5
b4 = b4/((b4**2).sum(axis=1,keepdims=True))**0.5
def fonk1(words_list):
    b5 = []
    for word in words_list:
        b5.append(word2idx[word])
    return b5
def fonk2(b16, b17):
    if b17 >= len(b16):
        return [b16]
    b6 = []
    for k in range(int(len(b16)/b17)):
        b6.append(b16[k * b17 : (k+1) * b17])
    if len(b16) % b17 != 0:
        b6.append(b16[(k + 1) * b17 : ])
    return b6
def fonk3(ang_path):
    b7 = open(ang_path, "r").read().strip().split('\n')
    b8 = []
    b9 = None
    for line in b7:
        if line.startswith(":"):
            b9 = line.lower().split()[1]
        else:
            b10 = line.split()
            b8.append((b9, b10[0], b10[1], b10[2], b10[3]))
    b11 = set([question[0] for question in b8])
    b12 = set([b9 for b9 in b11 if b9.startswith('gram')])
    b13 = set([b9 for b9 in b11 if b9 not in b12])
    b14 = [question[1:] for question in b8 if question[0] in b12]
    b15 = [question[1:] for question in b8 if question[0] in b13]
    return b14, b15
b14, b15 = fonk3(os.path.join('evaluation data', 'analogy', 'EN-GOOGLE.txt'))
b16 = {'Syntactic' : b14, 'Semantic' : b15}
def fonk4(b16, idx2vec, b17 = 1000):
    b18 = PrettyTable(['Category', 'Acc', 'Total', 'Missing'])
    for b9 in b16:
        b19 = b16[b9]
        a1 = 0
        b20 = []
        for question in b19:
            if question[0] in b1 and question[1] in b1 and question[2] in b1 and question[3] in b1:
                b20.append(question)
            else:
                a1 += 1
        b21 = []
        b22 = []
        for mini_questions in fonk2(b20, b17):
            b23 = np.array(mini_questions)
            word1, word2, word3, b24 = b23[:,0], b23[:,1], b23[:,2], b23[:,3]
            b25 = fonk1(list(word1))
            b26 = fonk1(list(word2))
            b27 = fonk1(list(word3))
            b28 = fonk1(list(b24))
            b29 = idx2vec[b25]
            b30 = idx2vec[b26]
            b31 = idx2vec[b27]
            b32 = b30 - b29 + b31
            b33 = 1-cdist(b32, idx2vec, 'cosine')
            b33[:,0] = -1
            b34 = np.argmax(b33,axis=1)
            b21 = b21 + list(b34)
            b22 = b22 + b28
        b22 = np.array(b22)
        b21 = np.array(b21)
        b35 = (b21 == b22)
        b36 = round(np.sum(b35)/len(b35)*100, 2)
        b18.add_row([b9, b36, len(b19), a1])
    print(b18)
print('\nResults of input embeddings:')
fonk4(b16, b3, b17 = 1000)
print('\nResults of output embeddings:')
fonk4(b16, b4, b17 = 1000)