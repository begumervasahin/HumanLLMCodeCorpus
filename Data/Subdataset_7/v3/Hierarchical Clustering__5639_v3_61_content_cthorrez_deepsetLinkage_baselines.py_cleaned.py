import numpy as np
from eval_utils import pairwise_f1
def fonk1(block):
    b1 = 'data/rexa/{}/gtClusters.tsv'.format(block)
    b2 = np.loadtxt(b1, delimiter='\t', dtype=np.float)[:, 1]
    return b2
def fonk2(b2):
    b3 = len(b2)
    b4 = np.max(b2) + 1
    b5 = np.zeros(b3)
    b6 = np.arange(b3)
    b7 = np.random.randint(low=0, high=b4, size=b3)
    return b5, b6, b7
def fonk3(b8, b9, b10, b11):
    print('Average F1 score for one cluster prediction:', np.mean(b9))
    print('Average F1 score for b3 clusters prediction:', np.mean(b10))
    print('Average F1 score for random prediction:', np.mean(b11))
def fonk4():
    b8 = np.array(['allen_d', 'moore_a', 'lee_l', 'robinson_h', 'mcguire_j', 'blum_a', 'jones_s', 'young_s' ])
    b9 = []
    b10 = []
    b11 = []
    for block in b8:
        b2 = fonk1(block)
        b5, b6, b7 = fonk2(b2)
        b9.append(pairwise_f1(b2, b5))
        b10.append(pairwise_f1(b2, b6))
        b11.append(pairwise_f1(b2, b7))
    fonk3(b8, b9, b10, b11)
if b12 = = '__main__':
    fonk4()