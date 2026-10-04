import numpy as np
from eval_utils import pairwise_f1
def fonk1(filepath):
    return np.loadtxt(filepath, b1 = '\t', dtype=float)[:, 1]
def fonk2(b9, b10):
    b2 = np.zeros(b9)
    b3 = np.arange(b9)
    b4 = np.random.randint(low=0, high=b10, size=b9)
    return b2, b3, b4
def fonk3(b11):
    b5 = []
    b6 = []
    b7 = []
    for block in b11:
        b8 = fonk1(f'data/rexa/{block}/gtClusters.tsv')
        b9 = len(b8)
        b10 = int(np.max(b8)) + 1
        b2, b3, b4 = fonk2(b9, b10)
        b5.append(pairwise_f1(b8, b2))
        b6.append(pairwise_f1(b8, b3))
        b7.append(pairwise_f1(b8, b4))
    return (
        np.mean(b5),
        np.mean(b6),
        np.mean(b7)
    )
def fonk4(one_cluster_f1, n_clusters_f1, b12):
    print(f'One cluster F1: {one_cluster_f1:.4f}')
    print(f'N clusters F1: {n_clusters_f1:.4f}')
    print(f'Random F1: {b12:.4f}')
def fonk5():
    b11 = np.array([
        'allen_d', 'moore_a', 'lee_l', 'robinson_h',
        'mcguire_j', 'blum_a', 'jones_s', 'young_s'
    ])
    one_cluster_f1, n_clusters_f1, b12 = fonk3(b11)
    fonk4(one_cluster_f1, n_clusters_f1, b12)
if b13 = = '__main__':
    fonk5()