import numpy as np
import random
import copy
import sys
import math
import matplotlib.pyplot as plt
import os
ITERATION = 200
KNN_DATA_FILE = './HW_data.mat'
KNN_LABELS_FILE = './HW_labels.mat'
def read_mat_file(file_path, variable_name):
    return np.random.rand(100, 4)
def get_the_data():
    data = read_mat_file(KNN_DATA_FILE, 'data2')
    labels = read_mat_file(KNN_LABELS_FILE, 'labels')
    return data, labels
def calculate_euclidean_distance(ins, center):
    return math.sqrt(sum((ins[i] - center[i]) ** 2 for i in range(len(ins))))
def calculate_manhattan_distance(ins, center):
    return sum(abs(ins[i] - center[i]) for i in range(len(ins)))
def calculate_cosine_similarity(ins, center):
    dot_product = sum(ins[i] * center[i] for i in range(len(ins)))
    norm_ins = math.sqrt(sum((ins[i]) ** 2 for i in range(len(ins))))
    norm_center = math.sqrt(sum((center[i]) ** 2 for i in range(len(ins))))
    return dot_product / (norm_ins * norm_center) if norm_ins != 0 and norm_center != 0 else 1
def find_mean_of_cluster(cluster):
    if len(cluster) == 0:
        return [0] * 4
    return [sum(ins[1][i] for ins in cluster) / len(cluster) for i in range(len(cluster[0][1]))]
def cluster_with_euclidean_distance(data, k_values):
    resulting_centers = {}
    resulting_clusters = {}
    for k in k_values:
        print(f"For k = {k}:")
        data_copy = copy.deepcopy(data)
        centers = {i: data_copy.pop(random.randint(0, len(data_copy)-1)) for i in range(k)}
        clusters = {i: [[i, center]] for i, center in centers.items()}
        for ins in data_copy:
            min_dist, cluster_num = min((calculate_euclidean_distance(ins, centers[c]), c) for c in centers)
            clusters[cluster_num].append([len(data) - len(data_copy), ins])
        for iteration in range(ITERATION):
            for cluster_num in clusters:
                centers[cluster_num] = find_mean_of_cluster(clusters[cluster_num])
            for cluster_num in list(clusters.keys()):
                for ins in clusters[cluster_num]:
                    min_dist, new_cluster_num = min((calculate_euclidean_distance(ins[1], centers[c]), c) for c in centers)
                    if new_cluster_num != cluster_num:
                        clusters[new_cluster_num].append(ins)
                        clusters[cluster_num].remove(ins)
            cost_func = sum(calculate_euclidean_distance(ins[1], centers[c])**2 for c in clusters for ins in clusters[c]) / len(data)
            plt.scatter(iteration, cost_func, color='black')
        resulting_centers[k] = centers
        resulting_clusters[k] = clusters
        inner_dist = sum(calculate_euclidean_distance(ins[1], centers[c]) for c in clusters for ins in clusters[c]) / len(data)
        outer_dist = sum(calculate_euclidean_distance(ins[1], centers[c2]) for c in clusters for ins in clusters[c] for c2 in centers if c2 != c) / len(data)
        print(f"Inner distance: {inner_dist}")
        print(f"Outer distance: {outer_dist}")
        for cluster_num in clusters:
            filename = f'./Clusters/{k}_{cluster_num}_Kcluster.txt'
            with open(filename, 'w') as file:
                for item in clusters[cluster_num]:
                    file.write(f"{item}\n")
        plt.show()
    return resulting_centers, resulting_clusters
def find_cluster_centers(data, labels, k):
    seen_classes, centers = set(), []
    for ind, ins in enumerate(data):
        if len(centers) == k:
            break
        if labels[ind] not in seen_classes:
            seen_classes.add(labels[ind])
            centers.append(ind)
    return centers
def find_most_seen(count_each_class):
    return count_each_class.index(max(count_each_class)) + 1
def calculate_cluster_majority(clusters, labels):
    majority = {}
    for k in clusters:
        majority[k] = {}
        for cluster_num in clusters[k]:
            class_counts = [0, 0, 0]
            for ins in clusters[k][cluster_num]:
                class_counts[labels[ins[0]][0] - 1] += 1
            majority[k][cluster_num] = find_most_seen(class_counts)
    return majority
def calculate_wrongly_classified(clusters, labels, majority):
    stats = {}
    for k in clusters:
        all_instances, wrongly_classified = 0, 0
        for cluster_num in clusters[k]:
            for ins in clusters[k][cluster_num]:
                all_instances += 1
                if labels[ins[0]][0] != majority[k][cluster_num]:
                    wrongly_classified += 1
        stats[k] = [all_instances, wrongly_classified]
    return stats
def main():
    data, labels = get_the_data()
    centers, clusters = cluster_with_euclidean_distance(data, [5])
    clusters = clusters[5]
    majority = calculate_cluster_majority(clusters, labels)
    wrongly_classified_stats = calculate_wrongly_classified(clusters, labels, majority)
    print(f"Clusters: {clusters}")
    print(f"Majority: {majority}")
    print(f"Wrongly Classified Stats: {wrongly_classified_stats}")
if __name__ == "__main__":
    main()