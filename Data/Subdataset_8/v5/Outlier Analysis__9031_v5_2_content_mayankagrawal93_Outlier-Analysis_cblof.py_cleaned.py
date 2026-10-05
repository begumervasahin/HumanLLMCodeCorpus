import pandas as pd
import numpy as np
import time
def to_float(x):
    return float(x)
def apply_to_dict(func, dictionary):
    for key, value in dictionary.items():
        dictionary[key] = func(value)
def create_new_cluster(key, current_tuple):
    summary = []
    cluster_structure = [[key], summary]
    for k, v in current_tuple.items():
        summary.append([{v: 1}])
    return cluster_structure
def update_cluster(cluster, current_tuple):
    for k, v in current_tuple.items():
        if v in cluster[k][0]:
            cluster[k][0][v] += 1
        else:
            cluster[k][0][v] = 1
def calculate_similarity(cluster, current):
    similarity_score = 0
    for k, v in current.items():
        if v in cluster[k][0]:
            support = cluster[k][0][v]
        else:
            support = 0
        similarity_score += (support / float(sum(cluster[k][0].values())))
    return similarity_score
data = pd.read_csv("fsd.csv")
dataset = np.array(data)
unique_values = {}
for column in data:
    column_data = np.array(data[column])
    for value in column_data:
        if value in unique_values:
            unique_values[value] += 1
        else:
            unique_values[value] = 1
    break
float_dataset = {}
for index, row in enumerate(dataset):
    float_row = {}
    for i, value in enumerate(row):
        float_row[i] = to_float(value)
    float_dataset[index] = float_row
clusters = []
for key in float_dataset:
    current_tuple = float_dataset[key]
    print("Processing tuple", key)
    if key == 0:
        clusters.append(create_new_cluster(key, current_tuple))
    else:
        similarities = []
        for cluster in clusters:
            similarities.append(calculate_similarity(cluster[1], current_tuple))
        max_similarity = max(similarities)
        max_index = similarities.index(max_similarity)
        similarity_threshold = 5
        if max_similarity >= similarity_threshold:
            clusters[max_index][0].append(key)
            update_cluster(clusters[max_index][1], current_tuple)
        else:
            clusters.append(create_new_cluster(key, current_tuple))
            print("New cluster created for tuple", key)
cluster_info = {}
for cluster in clusters:
    cluster_info[len(cluster[0])] = cluster
sorted_cluster_sizes = sorted(cluster_info.keys())
alpha = 0.1
total_clusters = 0
large_clusters = []
small_clusters = []
for size in sorted_cluster_sizes:
    total_clusters += size
    if total_clusters <= alpha * len(float_dataset):
        small_clusters.append(size)
    else:
        large_clusters.append(size)
CBLOF_scores = {}
for key in float_dataset:
    current_tuple = float_dataset[key]
    for cluster_size in cluster_info:
        if key in cluster_info[cluster_size][0]:
            cluster = cluster_size
            break
    print("Processing tuple", key)
    if cluster in large_clusters:
        similarity_score = calculate_similarity(cluster_info[cluster][1], current_tuple)
        lof_score = cluster * similarity_score
        CBLOF_scores[key] = round(lof_score, 6)
        print("Tuple", key, "processed: in large cluster")
    else:
        similarities = []
        for cluster_size in large_clusters:
            similarities.append(calculate_similarity(cluster_info[cluster_size][1], current_tuple))
        min_similarity = min(similarities)
        lof_score = cluster * min_similarity
        CBLOF_scores[key] = round(lof_score, 6)
        print("Tuple", key, "processed: in small cluster")
sorted_CBLOF_scores = sorted(CBLOF_scores, key=CBLOF_scores.get, reverse=True)
top_outliers_percentage = 5
num_outliers = int((top_outliers_percentage / 100.0) * len(sorted_CBLOF_scores))
top_outliers = sorted_CBLOF_scores[:num_outliers]