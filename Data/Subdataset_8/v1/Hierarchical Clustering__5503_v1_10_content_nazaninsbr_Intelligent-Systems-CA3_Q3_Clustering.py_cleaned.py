from helper import *
import numpy as np
import random
import copy
import sys
import math
import matplotlib.pyplot as plt
import os
ITERATION = 200
KNN_DATA_FILE = './HW'
KNN_LABELS_FILE = './HW'
def get_the_data():
    data = read_mat_file(KNN_DATA_FILE, 'data2')
    labels = read_mat_file(KNN_LABELS_FILE, 'labels')
    return data, labels
def calculateDist(ins, center):
    dist = 0
    for i in range(len(ins)):
        dist += (ins[i] - center[i]) ** 2
    return math.sqrt(dist)
def findMeanOfEverything(cluster):
    if len(cluster) == 0:
        return [0] * len(cluster[0][1])
    s = [0] * len(cluster[0][1])
    for fieldId in range(len(cluster[0][1])):
        for ins in cluster:
            s[fieldId] += ins[1][fieldId]
        s[fieldId] /= len(cluster)
    return s
def clusterBasedOnEveryThingWithEuclideanDistance(server_data, k):
    resultingCenters = {}
    resultingClusters = {}
    for k_num in k:
        server_data_copy = copy.deepcopy(server_data)
        centers = {}
        clusters = {}
        for i in range(k_num):
            ind = random.randint(0, len(server_data_copy)-1)
            centers[i] = server_data_copy[ind]
            clusters[i] = []
            clusters[i].append([ind, server_data_copy[ind]])
            del server_data_copy[ind]
        for ind, ins in enumerate(server_data_copy):
            minDist = sys.maxsize
            clusterNum = -1
            for center in centers.keys():
                dist = calculateDist(ins, centers[center])
                if dist < minDist:
                    minDist = dist
                    clusterNum = center
            clusters[clusterNum].append([ind, ins])
        for inter_num in range(ITERATION):
            for clusterNum in clusters.keys():
                mean = findMeanOfEverything(clusters[clusterNum])
                centers[clusterNum] = mean
            for clusterNum in clusters.keys():
                insId = 0
                while insId < len(clusters[clusterNum]):
                    minDist = sys.maxsize
                    newClusterNum = -1
                    for center in centers.keys():
                        dist = calculateDist(clusters[clusterNum][insId][1], centers[center])
                        if dist < minDist:
                            minDist = dist
                            newClusterNum = center
                    clusters[newClusterNum].append(clusters[clusterNum][insId])
                    del clusters[clusterNum][insId]
                insId += 1
            cost_func = 0
            for clusterNum in clusters.keys():
                for insId in range(len(clusters[clusterNum])):
                    cost_func += (calculateDist(clusters[clusterNum][insId][1], centers[clusterNum]))**2
            cost_func /= len(server_data)
            plt.scatter(inter_num, cost_func, color='black')
        print('Cluster Centers: ')
        print(centers)
        resultingCenters[k_num] = centers
        resultingClusters[k_num] = clusters
        inner_dist = 0
        outer_dist = 0
        for centerId in centers.keys():
            for val in clusters[centerId]:
                inner_dist += calculateDist(val[1], centers[centerId])
        inner_dist /= len(server_data)
        for centerId in centers.keys():
            for val in clusters[centerId]:
                for centerId2 in centers.keys():
                    if not centerId2 == centerId:
                        outer_dist += calculateDist(val[1], centers[centerId2])
        outer_dist /= len(server_data)
        print("Inner dist:", inner_dist)
        print("Outer dist:", outer_dist)
        for clusterNum in clusters.keys():
            fileName = f'./Clusters/{k_num}_{clusterNum}_Kcluster.txt'
            try:
                os.remove(fileName)
            except OSError:
                pass
            with open(fileName, 'a') as the_file:
                for item in clusters[clusterNum]:
                    the_file.write(str(item))
                    the_file.write('\n')
        plt.show()
    return resultingCenters, resultingClusters
def main():
    data, labels = get_the_data()
    myClusters = clusterBasedOnEveryThingWithEuclideanDistance(data, [5])
    return myClusters[5]
if __name__ == "__main__":
    main()