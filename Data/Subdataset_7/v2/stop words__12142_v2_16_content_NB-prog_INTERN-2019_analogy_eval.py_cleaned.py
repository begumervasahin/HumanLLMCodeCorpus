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
    b10 = [b7[b4] for b4 in words_list]
    return b10
def fonk3(b46, b21):
    if b21 >= len(b46):
        return [b46]
    b11 = []
    for k in range(int(len(b46) / b21)):
        b11.append(b46[k * b21: (k + 1) * b21])
    if len(b46) % b21 != 0:
        b11.append(b46[(k + 1) * b21:])
    return b11
def fonk4(ang_path):
    with open(ang_path, "r") as file:
        b12 = file.read().strip().split('\n')
    b13 = []
    b14 = None
    for line in b12:
        if line.startswith(":"):
            b14 = line.lower().split()[1]
        else:
            b15 = line.split()
            b13.append((b14, b15[0], b15[1], b15[2], b15[3]))
    b16 = set([question[0] for question in b13])
    b17 = set([b14 for b14 in b16 if b14.startswith('gram')])
    b18 = set([b14 for b14 in b16 if b14 not in b17])
    b19 = [question[1:] for question in b13 if question[0] in b17]
    b20 = [question[1:] for question in b13 if question[0] in b18]
    return b19, b20
def fonk5(b46, b6, b7, b9, b21 = 1000):
    b22 = PrettyTable(['Category', 'Accuracy', 'Total Questions', 'Missing Words'])
    for b14 in b46:
        b23 = b46[b14]
        a1 = 0
        b24 = []
        for question in b23:
            if all(b4 in b9 for b4 in question):
                b24.append(question)
            else:
                a1 += 1
        b25 = []
        b26 = []
        for mini_questions in fonk3(b24, b21):
            b27 = np.array(mini_questions)
            word1, word2, word3, b28 = b27[:, 0], b27[:, 1], b27[:, 2], b27[:, 3]
            b29 = fonk2(list(word1), b7)
            b30 = fonk2(list(word2), b7)
            b31 = fonk2(list(word3), b7)
            b32 = fonk2(list(b28), b7)
            b33 = b6[b29]
            b34 = b6[b30]
            b35 = b6[b31]
            b36 = b34 - b33 + b35
            b37 = 1 - cdist(b36, b6, 'cosine')
            b37[:, 0] = -1
            b38 = np.argmax(b37, b47=1)
            b25.extend(list(b38))
            b26.extend(b32)
        b26 = np.array(b26)
        b25 = np.array(b25)
        b39 = (b25 == b26)
        b40 = round(np.sum(b39) / len(b39) * 100, 2)
        b22.add_row([b14, b40, len(b23), a1])
    print(b22)
b41 = os.path.join('b1', 'input_embeddings.txt')
b42 = os.path.join('b1', 'output_embeddings.txt')
b43 = os.path.join('evaluation data', 'analogy', 'EN-GOOGLE.txt')
input_idx2vec, input_word2idx, b45, b44 = fonk1(b41)
output_idx2vec, b45, b45, b45 = fonk1(b42)
b19, b20 = fonk4(b43)
b46 = {'Syntactic': b19, 'Semantic': b20}
input_idx2vec /= np.linalg.norm(input_idx2vec, b47 = 1, keepdims=True)
output_idx2vec /= np.linalg.norm(output_idx2vec, b47 = 1, keepdims=True)
print('\nResults of input b1:')
fonk5(b46, input_idx2vec, input_word2idx, b44, b21 = 1000)
print('\nResults of output b1:')
fonk5(b46, output_idx2vec, input_word2idx, b44, b21 = 1000)