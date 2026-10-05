import pandas as pd
import numpy as np
import time
def to_float(x):
    return float(x)
def mutate_dict(f, d):
    for k, v in d.items():
        d[k] = f(v)
def new_cluster(key, current_tuple):
    summary = []
    cluster_structure = []
    for k in current_tuple:
        vs = {}
        vs[current_tuple[k]] = 1
        summary.append([vs])
    cluster_structure.append([key])
    cluster_structure.append(summary)
    return cluster_structure
def add_same(cluster, current_tuple):
    for k in current_tuple:
        if current_tuple[k] in cluster[k][0]:
            cluster[k][0][current_tuple[k]] += 1
        else:
            cluster[k][0][current_tuple[k]] = 1
def similarity(c, current):
    sim = 0
    for k in current:
        if current[k] in c[k][0]:
            sup = c[k][0][current[k]]
        else:
            sup = 0
        sim += (sup / float(sum(c[k][0].values())))
    return sim
dn = pd.read_csv("fsd.csv")
ds = np.array(dn)
values = {}
for d in dn:
    dm = np.array(dn[d])
    for key in dm:
        if key in values:
            values[key] += 1
        else:
            values[key] = 1
    break
D = {}
N = 0
t3 = time.time()
while N < len(ds):
    m = 0
    D[N] = {}
    for key in ds[N]:
        D[N][m] = key
        m += 1
    mutate_dict(to_float, D[N])
    N += 1
t4 = time.time() - t3
CS = []
t5 = time.time()
for key in D:
    current_tuple = D[key]
    print("2", key)
    if key == 0:
        CS.append(new_cluster(key, current_tuple))
    else:
        all_clusters = []
        for c in CS:
            all_clusters.append(similarity(c[1], current_tuple))
        max_sim = max(all_clusters)
        index = all_clusters.index(max(all_clusters))
        Sth = 5
        if max_sim >= Sth:
            CS[index][0].append(key)
            cluster = CS[index]
            add_same(cluster[1], current_tuple)
        else:
            CS.append(new_cluster(key, current_tuple))
            print(key)
t6 = time.time() - t5
C = {}
for cl in CS:
    C[len(cl[0])] = cl
S = sorted(C.keys())
a = 0.1
sum_of_clusters = 0
LC = []
SC = []
for l in S:
    sum_of_clusters += l
    if sum_of_clusters <= a * len(D):
        SC.append(l)
    else:
        LC.append(l)
t7 = time.time()
CBLOF = {}
for key in D:
    current = D[key]
    for k in C:
        if key in C[k][0]:
            cluster = k
            break
    print("2")
    if cluster in LC:
        s = similarity(C[cluster][1], current)
        lof = cluster * s
        CBLOF[key] = round(lof, 6)
        print("yes")
    else:
        all_clusters = []
        for c in LC:
            all_clusters.append(similarity(C[c][1], current)))
        max_sim = min(all_clusters)
        lof = cluster * max_sim
        CBLOF[key] = round(lof, 6)
        print("no")
    print("4")
t8 = time.time() - t7
sort_cblof = sorted(CBLOF, key=CBLOF.get, reverse=True)
n = 5
num = int((n / 100.0) * len(sort_cblof))
outliers = sort_cblof[:num]