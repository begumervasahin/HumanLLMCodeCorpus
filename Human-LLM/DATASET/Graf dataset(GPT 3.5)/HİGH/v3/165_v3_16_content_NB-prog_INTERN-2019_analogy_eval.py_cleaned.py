import os
import numpy as np
from scipy.spatial.distance import cdist
from prettytable import PrettyTable
def fonk1(embedding_file):
    b1 = {}
    with open(embedding_file, 'r', b2 = 'utf-8') as file:
        for line in file:
            b3 = line.strip().split()
            b4 = b3[0]
            b5 = np.array(b3[1:], dtype=np.float32)
            b1[b4] = b5
    b6 = np.array(list(b1.b3()))
    b7 = {b4: idx for idx, b4 in enumerate(b1.keys())}
    b8 = {idx: b4 for b4, idx in b7.items()}
    b9 = set(b7.keys())
    return b6, b7, b8, b9
def fonk2(words_list, b7):
    return [b7[b4] for b4 in words_list]
def fonk3(b44, b20):
    if b20 >= len(b44):
        return [b44]
    b10 = []
    for k in range(0, len(b44), b20):
        b10.append(b44[k : k + b20])
    return b10
def fonk4(file_path):
    with open(file_path, "r") as file:
        b11 = file.read().strip().split('\n')
    b12 = []
    b13 = None
    for line in b11:
        if line.startswith(":"):
            b13 = line.lower().split()[1]
        else:
            b14 = line.split()
            b12.append((b13, b14[0], b14[1], b14[2], b14[3]))
    b15 = set([question[0] for question in b12])
    b16 = set([b13 for b13 in b15 if b13.startswith('gram')])
    b17 = set([b13 for b13 in b15 if b13 not in b16])
    b18 = [question[1:] for question in b12 if question[0] in b16]
    b19 = [question[1:] for question in b12 if question[0] in b17]
    return b18, b19
def fonk5(b44, b6, b7, b9, b20 = 1000):
    b21 = PrettyTable(['Category', 'Accuracy', 'Total Questions', 'Missing Words'])
    for b13 in b44:
        b22 = b44[b13]
        a1 = 0
        b23 = []
        for question in b22:
            if all(b4 in b9 for b4 in question):
                b23.append(question)
            else:
                a1 += 1
        b24 = []
        b25 = []
        for mini_questions in fonk3(b23, b20):
            b26 = np.array(mini_questions)
            word1, word2, word3, b27 = b26[:, 0], b26[:, 1], b26[:, 2], b26[:, 3]
            b28 = fonk2(list(word1), b7)
            b29 = fonk2(list(word2), b7)
            b30 = fonk2(list(word3), b7)
            b31 = fonk2(list(b27), b7)
            b32 = b6[b28]
            b33 = b6[b29]
            b34 = b6[b30]
            b35 = b33 - b32 + b34
            b36 = 1 - cdist(b35, b6, 'cosine')
            b36[:, 0] = -1
            b37 = np.argmax(b36, b45=1)
            b24.extend(list(b37))
            b25.extend(b31)
        b25 = np.array(b25)
        b24 = np.array(b24)
        b38 = round(np.sum(b24 == b25) / len(b25) * 100, 2)
        b21.add_row([b13, b38, len(b22), a1])
    print(b21)
b39 = os.path.join('b1', 'input_embeddings.txt')
b40 = os.path.join('b1', 'output_embeddings.txt')
b41 = os.path.join('evaluation data', 'analogy', 'EN-GOOGLE.txt')
input_idx2vec, input_word2idx, b43, b42 = fonk1(b39)
output_idx2vec, b43, b43, b43 = fonk1(b40)
b18, b19 = fonk4(b41)
b44 = {'Syntactic': b18, 'Semantic': b19}
input_idx2vec /= np.linalg.norm(input_idx2vec, b45 = 1, keepdims=True)
output_idx2vec /= np.linalg.norm(output_idx2vec, b45 = 1, keepdims=True)
print('\nResults of input b1:')
fonk5(b44, input_idx2vec, input_word2idx, b42, b20 = 1000)
print('\nResults of output b1:')
fonk5(b44, output_idx2vec, input_word2idx, b42, b20 = 1000)