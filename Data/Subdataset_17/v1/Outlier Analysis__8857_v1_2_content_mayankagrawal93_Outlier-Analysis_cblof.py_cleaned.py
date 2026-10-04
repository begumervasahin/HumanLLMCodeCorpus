
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
        value_summary = {current_tuple[k]: 1}
        summary.append([value_summary])
    cluster_structure.append([key])
    cluster_structure.append(summary)
    return cluster_structure
def add_same(cluster, current_tuple):
    for k in current_tuple:
        if current_tuple[k] in cluster[k][0]:
            cluster[k][0][current_tuple[k]] += 1
        else:
            cluster[k][0][current_tuple[k]] = 1
def sim(cluster, current_tuple):
    similarity = 0
    for k in current_tuple:
        support = cluster[k][0].get(current_tuple[k], 0)
        total_support = sum(cluster[k][0].values())
        similarity += support / float(total_support)
    return similarity
dataframe = pd.read_csv("fsd.csv")
data_array = np.array(dataframe)
values = {}
for col in dataframe:
    col_array = np.array(dataframe[col])
    for key in col_array:
        if key in values:
            values[key] += 1
        else:
            values[key] = 1
    break
print("1")
D = {}
N = 0
start_time = time.time()
while N < len(data_array):
    D[N] = {i: key for i, key in enumerate(data_array[N])}
    mutate_dict(to_float, D[N])
    N += 1
elapsed_time = time.time() - start_time
clusters = []
start_time = time.time()
for key, current_tuple in D.items():
    print("2", key)
    if key == 0:
        clusters.append(new_cluster(key, current_tuple))
    else:
        all_similarities = [sim(cluster[1], current_tuple) for cluster in clusters]
        max_similarity = max(all_similarities)
        max_index = all_similarities.index(max_similarity)
        similarity_threshold = 5
        if max_similarity >= similarity_threshold:
            clusters[max_index][0].append(key)
            add_same(clusters[max_index][1], current_tuple)
        else:
            clusters.append(new_cluster(key, current_tuple))
            print(key)
elapsed_time = time.time() - start_time
cluster_dict = {len(cluster[0]): cluster for cluster in clusters}
sorted_cluster_sizes = sorted(cluster_dict.keys())
alpha = 0.1
sum_of_clusters = 0
large_clusters = []
small_clusters = []
for size in sorted_cluster_sizes:
    sum_of_clusters += size
    if sum_of_clusters <= alpha * len(D):
        small_clusters.append(size)
    else:
        large_clusters.append(size)
start_time = time.time()
cblof = {}
for key, current_tuple in D.items():
    for cluster_size in cluster_dict:
        if key in cluster_dict[cluster_size][0]:
            cluster = cluster_size
            break
    print("2")
    if cluster in large_clusters:
        similarity = sim(cluster_dict[cluster][1], current_tuple)
        lof = cluster * similarity
        cblof[key] = round(lof, 6)
        print("yes")
    else:
        all_similarities = [sim(cluster_dict[c][1], current_tuple) for c in large_clusters]
        max_similarity = min(all_similarities)
        lof = cluster * max_similarity
        cblof[key] = round(lof, 6)
        print("no")
    print("4")
elapsed_time = time.time() - start_time
sorted_cblof = sorted(cblof, key=cblof.get, reverse=True)
top_n_percentage = 5
num_outliers = int((top_n_percentage / 100.0) * len(sorted_cblof))
outliers = sorted_cblof[:num_outliers]
print("Outliers:", outliers)