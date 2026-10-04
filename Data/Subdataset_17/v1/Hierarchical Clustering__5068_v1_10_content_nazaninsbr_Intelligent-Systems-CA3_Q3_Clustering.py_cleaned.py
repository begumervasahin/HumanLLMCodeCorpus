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
def calculateDist(ins, center):
    return math.sqrt(sum((ins[i] - center[i]) ** 2 for i in range(len(ins))))
def calculateManhattanDist(ins, center):
    return sum(abs(ins[i] - center[i]) for i in range(len(ins)))
def calculateCosineSimilarity(ins, center):
    dot = sum(ins[i]*center[i] for i in range(len(ins)))
    norm_1 = math.sqrt(sum((ins[i])**2 for i in range(len(ins))))
    norm_2 = math.sqrt(sum((center[i])**2 for i in range(len(ins))))
    return dot / (norm_1 * norm_2) if norm_1 != 0 and norm_2 != 0 else 1
def findMeanOfEverything(cluster):
    if len(cluster) == 0:
        return [0] * 4
    s = [sum(ins[1][fieldId] for ins in cluster) / len(cluster) for fieldId in range(len(cluster[0][1]))]
    return s
def clusterBasedOnEveryThingWithEuclideanDistance(server_data, k_values):
    resultingCenters = {}
    resultingClusters = {}
    for k_num in k_values:
        print(f"For k = {k_num}:")
        server_data_copy = copy.deepcopy(server_data)
        centers = {i: server_data_copy.pop(random.randint(0, len(server_data_copy)-1)) for i in range(k_num)}
        clusters = {i: [[i, center]] for i, center in centers.items()}
        for ins in server_data_copy:
            minDist, clusterNum = min((calculateDist(ins, centers[center]), center) for center in centers)
            clusters[clusterNum].append([len(server_data) - len(server_data_copy) + i, ins])
        for inter_num in range(ITERATION):
            for clusterNum in clusters:
                centers[clusterNum] = findMeanOfEverything(clusters[clusterNum])
            for clusterNum in clusters:
                for insId in range(len(clusters[clusterNum])):
                    minDist, newClusterNum = min((calculateDist(clusters[clusterNum][insId][1], centers[center]), center) for center in centers)
                    clusters[newClusterNum].append(clusters[clusterNum][insId])
                    del clusters[clusterNum][insId]
            cost_func = sum(calculateDist(ins[1], centers[clusterNum])**2 for clusterNum in clusters for ins in clusters[clusterNum]) / len(server_data)
            plt.scatter(inter_num, cost_func, color='black')
        resultingCenters[k_num] = centers
        resultingClusters[k_num] = clusters
        inner_dist = sum(calculateDist(val[1], centers[centerId]) for centerId in centers for val in clusters[centerId]) / len(server_data)
        outer_dist = sum(calculateDist(val[1], centers[centerId2]) for centerId in centers for val in clusters[centerId] for centerId2 in centers if centerId2 != centerId) / len(server_data)
        print(f"Inner dist: {inner_dist}")
        print(f"Outer dist: {outer_dist}")
        for clusterNum in clusters:
            fileName = f'./Clusters/{k_num}_{clusterNum}_Kcluster.txt'
            with open(fileName, 'w') as the_file:
                for item in clusters[clusterNum]:
                    the_file.write(str(item) + '\n')
        plt.show()
    return resultingCenters, resultingClusters
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
    return count_each_class.index(max(count_each_class)) + 1
def calculate_cluster_majority(myClusters, labels):
    majority = {}
    for kVal in myClusters:
        majority[kVal] = {}
        for classNumber in myClusters[kVal]:
            count_each_class = [0, 0, 0]
            for ins in myClusters[kVal][classNumber]:
                count_each_class[labels[ins[0]][0]-1] += 1
            majority[kVal][classNumber] = find_most_seen(count_each_class)
    return majority
def calculate_how_many_wrongly_classified(myClusters, labels, majority):
    stats = {}
    for kVal in myClusters:
        all_instances, wrongly_clustered = 0, 0
        for classNumber in myClusters[kVal]:
            for ins in myClusters[kVal][classNumber]:
                all_instances += 1
                if labels[ins[0]][0] != majority[kVal][classNumber]:
                    wrongly_clustered += 1
        stats[kVal] = [all_instances, wrongly_clustered]
    return stats
def main():
    data, labels = get_the_data()
    myCenters, myClusters = clusterBasedOnEveryThingWithEuclideanDistance(data, [5])
    clusters = myClusters[5]
    majority = calculate_cluster_majority(myClusters, labels)
    wrongly_classified_stats = calculate_how_many_wrongly_classified(myClusters, labels, majority)
    print(f"Clusters: {clusters}")
    print(f"Majority: {majority}")
    print(f"Wrongly Classified Stats: {wrongly_classified_stats}")
if __name__ == "__main__":
    main()