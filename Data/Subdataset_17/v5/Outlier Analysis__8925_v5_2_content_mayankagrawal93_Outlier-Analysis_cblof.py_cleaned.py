
import pandas as pd
import time
import numpy as np
def to_float(x):
    return float(x)
def mutate_dict(f, d):
    for k, v in d.items():
        d[k] = f(v)
def new_cluster(key, current_tuple):
    summary = [{current_tuple[k]: 1} for k in current_tuple]
    return [[key], summary]
def add_to_cluster(cluster, current_tuple):
    for k in current_tuple:
        cluster_entry = cluster[k][0]
        if current_tuple[k] in cluster_entry:
            cluster_entry[current_tuple[k]] += 1
        else:
            cluster_entry[current_tuple[k]] = 1
def calculate_similarity(cluster_summary, current_tuple):
    similarity = 0
    for k in current_tuple:
        support = cluster_summary[k][0].get(current_tuple[k], 0)
        total_support = sum(cluster_summary[k][0].values())
        similarity += support / float(total_support)
    return similarity
def main():
    df = pd.read_csv("fsd.csv")
    data_array = np.array(df)
    value_counts = {}
    for col in df:
        col_array = np.array(df[col])
        for key in col_array:
            value_counts[key] = value_counts.get(key, 0) + 1
        break
    print("Value frequency count completed")
    data_dict = {i: {j: to_float(val) for j, val in enumerate(row)} for i, row in enumerate(data_array)}
    print("Data processing completed")
    clusters = []
    similarity_threshold = 5
    for key, current_tuple in data_dict.items():
        if key == 0:
            clusters.append(new_cluster(key, current_tuple))
        else:
            similarities = [calculate_similarity(c[1], current_tuple) for c in clusters]
            max_similarity = max(similarities)
            max_index = similarities.index(max_similarity)
            if max_similarity >= similarity_threshold:
                clusters[max_index][0].append(key)
                add_to_cluster(clusters[max_index][1], current_tuple)
            else:
                clusters.append(new_cluster(key, current_tuple))
                print(f"New cluster created for key {key}")
    cluster_dict = {len(c[0]): c for c in clusters}
    sorted_cluster_sizes = sorted(cluster_dict.keys())
    a = 0.1
    cumulative_size = 0
    large_clusters = []
    small_clusters = []
    for size in sorted_cluster_sizes:
        cumulative_size += size
        if cumulative_size <= a * len(data_dict):
            small_clusters.append(size)
        else:
            large_clusters.append(size)
    cblof = {}
    for key, current_tuple in data_dict.items():
        cluster_size = next(size for size, cluster in cluster_dict.items() if key in cluster[0])
        if cluster_size in large_clusters:
            similarity = calculate_similarity(cluster_dict[cluster_size][1], current_tuple)
            lof = cluster_size * similarity
            cblof[key] = round(lof, 6)
        else:
            similarities = [calculate_similarity(cluster_dict[size][1], current_tuple) for size in large_clusters]
            max_similarity = min(similarities)
            lof = cluster_size * max_similarity
            cblof[key] = round(lof, 6)
    sorted_cblof = sorted(cblof, key=cblof.get, reverse=True)
    top_n_percent = 5
    num_outliers = int((top_n_percent / 100.0) * len(sorted_cblof))
    outliers = sorted_cblof[:num_outliers]
    print("Outliers:", outliers)
if __name__ == "__main__":
    main()