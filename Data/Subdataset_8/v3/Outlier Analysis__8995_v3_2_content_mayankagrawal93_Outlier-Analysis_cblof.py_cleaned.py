import pandas as pd
import numpy as np
import time
def to_float(x):
    return float(x)
def convert_dict_to_floats(f, d):
    for k, v in d.items():
        d[k] = f(v)
def create_new_cluster_structure(key, current_tuple):
    summary = []
    cluster_structure = []
    for k in current_tuple:
        value_stats = {current_tuple[k]: 1}
        summary.append([value_stats])
    cluster_structure.append([key])
    cluster_structure.append(summary)
    return cluster_structure
def update_existing_cluster(cluster, current_tuple):
    for k in current_tuple:
        if current_tuple[k] in cluster[k][0]:
            cluster[k][0][current_tuple[k]] += 1
        else:
            cluster[k][0][current_tuple[k]] = 1
def calculate_similarity_with_cluster(cluster, current_tuple):
    similarity = 0
    for k in current_tuple:
        if current_tuple[k] in cluster[k][0]:
            support = cluster[k][0][current_tuple[k]]
        else:
            support = 0
        similarity += (support / float(sum(cluster[k][0].values())))
    return similarity
def identify_outliers(data, converted_data, clusters):
    cblof_scores = {}
    for key in converted_data:
        current_data = converted_data[key]
        for cluster_size in clusters:
            if key in clusters[cluster_size][0]:
                cluster_id = cluster_size
                break
        if cluster_id in large_clusters:
            similarity = calculate_similarity_with_cluster(clusters[cluster_id][1], current_data)
            lof = cluster_id * similarity
            cblof_scores[key] = round(lof, 6)
        else:
            all_similarities = []
            for lc in large_clusters:
                all_similarities.append(calculate_similarity_with_cluster(clusters[lc][1], current_data))
            max_similarity = min(all_similarities)
            lof = cluster_id * max_similarity
            cblof_scores[key] = round(lof, 6)
    return cblof_scores
data = pd.read_csv("fsd.csv")
data_array = np.array(data)
converted_data = {}
for column_name in data:
    column_data = np.array(data[column_name])
    for index, value in enumerate(column_data):
        converted_data[index] = {i: to_float(v) for i, v in enumerate(column_data)}
    break
clusters = {}
for key in converted_data:
    current_tuple = converted_data[key]
    print("Processing tuple", key)
    if key == 0:
        clusters[key] = create_new_cluster_structure(key, current_tuple)
    else:
        all_similarities = {}
        for cluster_key in clusters:
            all_similarities[cluster_key] = calculate_similarity_with_cluster(clusters[cluster_key][1], current_tuple)
        max_similarity_cluster = max(all_similarities, key=all_similarities.get)
        similarity_threshold = 5
        if all_similarities[max_similarity_cluster] >= similarity_threshold:
            clusters[max_similarity_cluster][0].append(key)
            update_existing_cluster(clusters[max_similarity_cluster][1], current_tuple)
        else:
            clusters[key] = create_new_cluster_structure(key, current_tuple)
            print("New cluster created for tuple", key)
cluster_statistics = {len(clusters[cluster_size][0]): clusters[cluster_size] for cluster_size in clusters}
sorted_cluster_sizes = sorted(cluster_statistics.keys())
alpha = 0.1
sum_of_clusters = 0
large_clusters = []
small_clusters = []
for size in sorted_cluster_sizes:
    sum_of_clusters += size
    if sum_of_clusters <= alpha * len(converted_data):
        small_clusters.append(size)
    else:
        large_clusters.append(size)
cblof_scores = identify_outliers(data, converted_data, clusters)
sorted_cblof_scores = sorted(cblof_scores, key=cblof_scores.get, reverse=True)
top_n_percent = 5
num_outliers = int((top_n_percent / 100.0) * len(sorted_cblof_scores))
outliers = sorted_cblof_scores[:num_outliers]