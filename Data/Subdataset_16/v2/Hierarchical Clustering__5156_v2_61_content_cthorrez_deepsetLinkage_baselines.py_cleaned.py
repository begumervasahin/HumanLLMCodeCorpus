import numpy as np
from eval_utils import pairwise_f1
def fonk1(filepath):
    return np.loadtxt(filepath, b1 = '\t', dtype=float)[:, 1]
def fonk2(b11):
    b2 = []
    b3 = []
    b4 = []
    for block in b11:
        b5 = fonk1(f'data/rexa/{block}/gtClusters.tsv')
        b6 = len(b5)
        b7 = int(np.max(b5)) + 1
        b8 = np.zeros(b6)
        b9 = np.arange(b6)
        b10 = np.random.randint(low=0, high=b7, size=b6)
        b2.append(pairwise_f1(b5, b8))
        b3.append(pairwise_f1(b5, b9))
        b4.append(pairwise_f1(b5, b10))
    return np.mean(b2), np.mean(b3), np.mean(b4)
def fonk3():
    b11 = np.array(['allen_d', 'moore_a', 'lee_l', 'robinson_h',
                       'mcguire_j', 'blum_a', 'jones_s', 'young_s'])
    one_cluster_f1, n_clusters_f1, b12 = fonk2(b11)
    print(f'One cluster F1: {one_cluster_f1:.4f}')
    print(f'N clusters F1: {n_clusters_f1:.4f}')
    print(f'Random F1: {b12:.4f}')
if b13 = = '__main__':
    fonk3()