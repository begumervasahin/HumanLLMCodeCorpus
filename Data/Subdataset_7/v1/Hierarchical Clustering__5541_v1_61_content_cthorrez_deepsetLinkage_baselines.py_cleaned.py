import numpy as np
from eval_utils import pairwise_f1
def fonk1():
    b1 = np.array(['allen_d', 'moore_a', 'lee_l', 'robinson_h',
                       'mcguire_j', 'blum_a', 'jones_s', 'young_s' ])
    b2 = []
    b3 = []
    b4 = []
    for block in b1:
        b5 = np.loadtxt('data/rexa/{}/gtClusters.tsv'.format(block), delimiter='\t', dtype=np.float)[:, 1]
        b6 = len(b5)
        b7 = np.max(b5) + 1
        b8 = np.zeros(b6)
        b9 = np.arange(b6)
        b10 = np.random.randint(low=0, high=b7, size=b6)
        b2.append(pairwise_f1(b5, b8))
        b3.append(pairwise_f1(b5, b9))
        b4.append(pairwise_f1(b5, b10))
    print('Average F1 score for one cluster prediction:', np.mean(b2))
    print('Average F1 score for b6 clusters prediction:', np.mean(b3))
    print('Average F1 score for random prediction:', np.mean(b4))
if b11 = = '__main__':
    fonk1()