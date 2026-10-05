import sys
import math
import random
import copy
import os
import numpy as np
import matplotlib.pyplot as plt
from helper import read_mat_file
ITERATION = 200
KNN_DATA_FILE = './HW'
KNN_LABELS_FILE = './HW'
def get_data():
    data = read_mat_file(KNN_DATA_FILE, 'data2')
    labels = read_mat_file(KNN_LABELS_FILE, 'labels')
    return data, labels
def euclidean_distance(instance, center):
    distance = 0
    for i in range(len(instance)):
        distance += (instance[i] - center[i]) ** 2
    return math.sqrt(distance)
def calculate_manhattan_distance(instance, center):
    distance = 0
    for i in range(len(instance)):
        distance += abs(instance[i] - center[i])
    return distance
def cosine_similarity(instance, center):
    dot_product = 0
    norm_1 = 0
    norm_2 = 0
    for i in range(len(instance)):
        dot_product += instance[i] * center[i]
        norm_1 += instance[i] ** 2
        norm_2 += center[i] ** 2
    if norm_1 == 0 or norm_2 == 0:
        return 1
    return dot_product / (math.sqrt(norm_1) * math.sqrt(norm_2))
def calculate_mean(cluster):
    if len(cluster) == 0:
        return [0] * len(cluster[0][1])
    num_features = len(cluster[0][1])
    mean_vector = [sum(instance[1][i] for instance in cluster) / len(cluster) for i in range(num_features)]
    return mean_vector
def cluster_based_on_everything_with_euclidean_distance(server_data, k):
    resulting_centers = {}
    resulting_clusters = {}
    for k_num in k:
        print("For k =", k_num, ":")
        server_data_copy = copy.deepcopy(server_data)
        centers = {}
        clusters = {}
        for i in range(k_num):
            ind = random.randint(0, len(server_data_copy) - 1)
            centers[i] = server_data_copy[ind]
            clusters[i] = []
            clusters[i].append([ind, server_data_copy[ind]])
            del server_data_copy[ind]
        for ind, ins in enumerate(server_data_copy):
            min_dist = sys.maxsize
            cluster_num = -1
            for center in centers.keys():
                dist = euclidean_distance(ins, centers[center])
                if dist < min_dist:
                    min_dist = dist
                    cluster_num = center
            clusters[cluster_num].append([ind, ins])
        for inter_num in range(ITERATION):
            for cluster_num in clusters.keys():
                mean = calculate_mean(clusters[cluster_num])
                centers[cluster_num] = mean
            for cluster_num in clusters.keys():
                ins_id = 0
                while ins_id < len(clusters[cluster_num]):
                    min_dist = sys.maxsize
                    new_cluster_num = -1
                    for center in centers.keys():
                        dist = euclidean_distance(clusters[cluster_num][ins_id][1], centers[center])
                        if dist < min_dist:
                            min_dist = dist
                            new_cluster_num = center
                    clusters[new_cluster_num].append(clusters[cluster_num][ins_id])
                    del clusters[cluster_num][ins_id]
                    ins_id += 1
            cost_func = 0
            for cluster_num in clusters.keys():
                for ins_id in range(len(clusters[cluster_num])):
                    cost_func += (euclidean_distance(clusters[cluster_num][ins_id][1], centers[cluster_num])) ** 2
            cost_func /= len(server_data)
            plt.scatter(inter_num, cost_func, color='black')
        print('Cluster Centers:')
        print(centers)
        resulting_centers[k_num] = centers
        resulting_clusters[k_num] = clusters
        inner_dist = 0
        outer_dist = 0
        for center_id in centers.keys():
            for val in clusters[center_id]:
                inner_dist += euclidean_distance(val[1], centers[center_id])
        inner_dist /= len(server_data)
        for center_id in centers.keys():
            for val in clusters[center_id]:
                for center_id2 in centers.keys():
                    if not center_id2 == center_id:
                        outer_dist += euclidean_distance(val[1], centers[center_id2])
        outer_dist /= len(server_data)
        print("Inner dist:", inner_dist)
        print("Outer dist:", outer_dist)
        for cluster_num in clusters.keys():
            file_name = f'./Clusters/{k_num}_{cluster_num}_Kcluster.txt'
            try:
                os.remove(file_name)
            except OSError:
                pass
            with open(file_name, 'a') as the_file:
                for item in clusters[cluster_num]:
                    the_file.write(str(item))
                    the_file.write('\n')
        plt.show()
    return resulting_centers, resulting_clusters
def find_cluster_centers(data, labels, k):
    seen_classes, centers = [], []
    for ind, ins in enumerate(data):
        if len(centers) == k:
            break
        if labels[ind] not in seen_classes:
            seen_classes.append(labels[ind])
            centers.append(ind)
    return centers
def find_most_seen(count_each_class):
    if count_each_class[0] >= count_each_class[1] and count_each_class[0] >= count_each_class[2]:
        return 1
    if count_each_class[1] >= count_each_class[0] and count_each_class[1] >= count_each_class[2]:
        return 2
    if count_each_class[2] >= count_each_class[1] and count_each_class[2] >= count_each_class[0]:
        return 3
def calculate_cluster_majority(my_clusters, labels):
    majority = {}
    for k_val in my_clusters.keys():
        majority[k_val] = {}
        for class_number in my_clusters[k_val].keys():
            count_each_class = [0, 0, 0]
            for ins in my_clusters[k_val][class_number]:
                count_each_class[labels[ins[0]][0] - 1] += 1
            majority[k_val][class_number] = find_most_seen(count_each_class)
    return majority
def calculate_how_many_wrongly_classified(my_clusters, labels, majority):
    stats = {}
    for k_val in my_clusters.keys():
        all_instances, wrongly_clustered = 0, 0
        for class_number in my_clusters[k_val].keys():
            for ins in my_clusters[k_val][class_number]:
                all_instances += 1
                if labels[ins[0]][0] != majority[k_val][class_number]:
                    wrongly_clustered += 1
        stats[k_val] = [all_instances, wrongly_clustered]
    return stats
def main(data, labels):
    my_centers, my_clusters = cluster_based_on_everything_with_euclidean_distance(data, [5])
    return my_clusters[5]
if __name__ == "__main__":
    data, labels = get_data()
    main(data, labels)