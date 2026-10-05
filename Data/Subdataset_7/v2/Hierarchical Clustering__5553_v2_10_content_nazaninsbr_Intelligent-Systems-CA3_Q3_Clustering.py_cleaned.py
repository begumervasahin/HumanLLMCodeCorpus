import sys
import math
import random
import copy
import os
import numpy as np
import matplotlib.pyplot as plt
from helper import read_mat_file
a1 = 200
b1 = './HW'
b2 = './HW'
def fonk1():
    b3 = read_mat_file(b1, 'data2')
    b4 = read_mat_file(b2, 'b4')
    return b3, b4
def fonk2(instance, center):
    b5 = sum((x - y) ** 2 for x, y in zip(instance, center))
    return math.sqrt(b5)
def fonk3(cluster):
    if len(cluster) == 0:
        return [0] * len(cluster[0][1])
    b6 = len(cluster[0][1])
    b7 = [sum(instance[1][i] for instance in cluster) / len(cluster) for i in range(b6)]
    return b7
def fonk4(b3, k_values):
    b8 = {}
    b9 = {}
    for k in k_values:
        b10 = copy.deepcopy(b3)
        b11 = {i: b10.pop(random.randint(0, len(b10) - 1)) for i in range(k)}
        b12 = {i: [] for i in range(k)}
        for a2, instance in enumerate(b10):
            b13 = sys.maxsize
            b14 = None
            for center_idx, center_instance in b11.items():
                b15 = fonk2(instance, center_instance)
                if b15 < b13:
                    b13 = b15
                    b14 = center_idx
            b12[b14].append([a2, instance])
        for _ in range(a1):
            for center_idx, cluster_instances in b12.items():
                b7 = fonk3(cluster_instances)
                b11[center_idx] = b7
            for center_idx, cluster_instances in b12.items():
                a2 = 0
                while a2 < len(cluster_instances):
                    b13 = sys.maxsize
                    b14 = None
                    for center_id, center_instance in b11.items():
                        b15 = fonk2(cluster_instances[a2][1], center_instance)
                        if b15 < b13:
                            b13 = b15
                            b14 = center_id
                    b12[b14].append(cluster_instances[a2])
                    del b12[center_idx][a2]
                    a2 += 1
            b16 = sum(fonk2(instance[1], b11[center_idx]) ** 2
                            for center_idx, cluster_instances in b12.items()
                            for instance in cluster_instances) / len(b3)
            plt.scatter(_, b16, b17 = 'black')
        print('Cluster Centers:')
        print(b11)
        b8[k] = b11
        b9[k] = b12
        b18 = sum(fonk2(val[1], b11[center_id])
                         for center_id, cluster_instances in b11.items()
                         for val in cluster_instances) / len(b3)
        b19 = sum(fonk2(val[1], b11[center_id2])
                         for center_id, cluster_instances in b11.items()
                         for val in cluster_instances
                         for center_id2 in b11.keys() if center_id2 != center_id) / len(b3)
        print("Inner b15:", b18)
        print("Outer b15:", b19)
        for cluster_num, cluster_instances in b12.items():
            b20 = f'./Clusters/{k}_{cluster_num}_Kcluster.txt'
            try:
                os.remove(b20)
            except OSError:
                pass
            with open(b20, 'a') as file:
                for item in cluster_instances:
                    file.write(str(item))
                    file.write('\n')
        plt.show()
    return b8, b9
def fonk5():
    b3, b4 = fonk1()
    b21 = fonk4(b3, [5])
    return b21[5]
if b22 = = "__main__":
    fonk5()