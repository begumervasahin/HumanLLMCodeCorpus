import numpy as np
from eval_utils import pairwise_f1
def fonk1(filepath):
    return np.loadtxt(filepath, b1 = '\t', dtype=np.float64)[:, 1]
def fonk2(block_name):
    b2 = fonk1(f'data/rexa/{block_name}/gtClusters.tsv')
    b3 = len(b2)
    b4 = int(np.max(b2)) + 1
    b5 = np.zeros(b3)
    b6 = np.arange(b3)
    b7 = np.random.randint(low=0, high=b4, size=b3)
    b8 = pairwise_f1(b2, b5)
    b9 = pairwise_f1(b2, b6)
    b10 = pairwise_f1(b2, b7)
    return b8, b9, b10
def fonk3():
    b11 = ['allen_d', 'moore_a', 'lee_l', 'robinson_h', 'mcguire_j', 'blum_a', 'jones_s', 'young_s']
    b12 = []
    b13 = []
    b14 = []
    for block in b11:
        b8, b9, b10 = fonk2(block)
        b12.append(b8)
        b13.append(b9)
        b14.append(b10)
    print(f'One cluster F1: {np.mean(b12):.4f}')
    print(f'N clusters F1: {np.mean(b13):.4f}')
    print(f'Random F1: {np.mean(b14):.4f}')
if b15 = = '__main__':
    fonk3()