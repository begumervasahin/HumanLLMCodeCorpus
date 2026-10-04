
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
def calculate_similarity(cluster, current_tuple):
    similarity = 0
    for k in current_tuple:
        support = cluster[k][0].get(current_tuple[k], 0)
        total_support = sum(cluster[k][0].values())
        similarity += support / float(total_support)
    return similarity
dataframe = pd.read_csv("fsd.csv")
data_array = np.array(dataframe)
value_counts = {}
for col in dataframe:
    col_array = np.array(dataframe[col])
    for key in col_array:
        value_counts[key] = value_counts.get(key, 0) + 1
    break
print("1")
clusters_dict = {}
index = 0
start_time = time.time()
for row in data_array:
    clusters_dict[index] = {i: key for i, key in enumerate(row)}
    mutate_dict(to_float, clusters_dict[index])
    index += 1
processing_time = time.time() - start_time
clusters = []
start_time = time.time()
for key, current_tuple in clusters_dict.items():
    print("2", key)
    if key == 0:
        clusters.append(new_cluster(key, current_tuple))
    else:
        similarities = [calculate_similarity(cluster[1], current_tuple) for cluster in clusters]
        max_similarity = max(similarities)
        max_index = similarities.index(max_similarity)
        similarity_threshold = 5
        if max_similarity >= similarity_threshold:
            clusters[max_index][0].append(key)
            add_same(clusters[max_index][1], current_tuple)
        else:
            clusters.append(new_cluster(key, current_tuple))
            print(key)
clustering_time = time.time() - start_time
cluster_size_dict = {len(cluster[0]): cluster for cluster in clusters}
sorted_cluster_sizes = sorted(cluster_size_dict.keys())
alpha = 0.1
sum_of_cluster_sizes = 0
large_clusters = []
small_clusters = []
for size in sorted_cluster_sizes:
    sum_of_cluster_sizes += size
    if sum_of_cluster_sizes <= alpha * len(clusters_dict):
        small_clusters.append(size)
    else:
        large_clusters.append(size)
start_time = time.time()
cblof_scores = {}
for key, current_tuple in clusters_dict.items():
    for cluster_size in cluster_size_dict:
        if key in cluster_size_dict[cluster_size][0]:
            cluster = cluster_size
            break
    print("2")
    if cluster in large_clusters:
        similarity = calculate_similarity(cluster_size_dict[cluster][1], current_tuple)
        lof = cluster * similarity
        cblof_scores[key] = round(lof, 6)
        print("yes")
    else:
        similarities = [calculate_similarity(cluster_size_dict[c][1], current_tuple) for c in large_clusters]
        max_similarity = min(similarities)
        lof = cluster * max_similarity
        cblof_scores[key] = round(lof, 6)
        print("no")
    print("4")
cblof_calculation_time = time.time() - start_time
sorted_cblof = sorted(cblof_scores, key=cblof_scores.get, reverse=True)
top_n_percentage = 5
num_outliers = int((top_n_percentage / 100.0) * len(sorted_cblof))
outliers = sorted_cblof[:num_outliers]
print("Outliers:", outliers)