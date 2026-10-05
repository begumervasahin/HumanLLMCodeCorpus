import os
import numpy as np
from scipy.spatial.distance import cdist
from prettytable import PrettyTable
from DataHandler import load_embeddings
b1 = os.path.join('embeddings', 'input_embeddings.txt')
b2 = os.path.join('embeddings', 'output_embeddings.txt')
b3 = os.path.join('evaluation data', 'analogy', 'EN-GOOGLE.txt')
b6, word2idx, idx2word, b4 = load_embeddings(b1)
b7, b5, b5, b5 = load_embeddings(b2)
b6 = b6 / np.linalg.norm(b6, b35=1, keepdims=True)
b7 = b7 / np.linalg.norm(b7, b35=1, keepdims=True)
def fonk1(words_list):
    return [word2idx[word] for word in words_list]
def fonk2(b18, b19):
    if b19 >= len(b18):
        return [b18]
    b8 = []
    for i in range(0, len(b18), b19):
        b8.append(b18[i:i + b19])
    return b8
def fonk3(file_path):
    b9 = open(file_path, "r").read().strip().split('\n')
    b10 = []
    b11 = None
    for line in b9:
        if line.startswith(":"):
            b11 = line.lower().split()[1]
        else:
            b12 = line.split()
            b10.append((b11, b12[0], b12[1], b12[2], b12[3]))
    b13 = set(question[0] for question in b10)
    b14 = {b11 for b11 in b13 if b11.startswith('gram')}
    b15 = b13 - b14
    b16 = [question[1:] for question in b10 if question[0] in b14]
    b17 = [question[1:] for question in b10 if question[0] in b15]
    return b16, b17
b16, b17 = fonk3(b3)
b18 = {'Syntactic': b16, 'Semantic': b17}
def fonk4(b18, embeddings, b19 = 1000):
    b20 = PrettyTable(['Category', 'Accuracy', 'Total Questions', 'Missing Words'])
    for b11, cat_questions in b18.items():
        a1 = 0
        b21 = []
        for question in cat_questions:
            if all(word in b4 for word in question):
                b21.append(question)
            else:
                a1 += 1
        b22 = []
        b23 = []
        for b24 in fonk2(b21, b19):
            b24 = np.array(b24)
            word1, word2, word3, b25 = b24[:, 0], b24[:, 1], b24[:, 2], b24[:, 3]
            b26 = fonk1(word1)
            b27 = fonk1(word2)
            b28 = fonk1(word3)
            b29 = fonk1(b25)
            b30 = embeddings[b26]
            b31 = embeddings[b27]
            b32 = embeddings[b28]
            b33 = b31 - b30 + b32
            b34 = 1 - cdist(b33, embeddings, 'cosine')
            b34[:, 0] = -1
            b22.extend(np.argmax(b34, b35 = 1))
            b23.extend(b29)
        b23 = np.array(b23)
        b22 = np.array(b22)
        b36 = (b22 == b23)
        b37 = round(np.sum(b36) / len(b36) * 100, 2)
        b20.add_row([b11, b37, len(cat_questions), a1])
    print(b20)
print('\nResults of input embeddings:')
fonk4(b18, b6, b19 = 1000)
print('\nResults of output embeddings:')
fonk4(b18, b7, b19 = 1000)