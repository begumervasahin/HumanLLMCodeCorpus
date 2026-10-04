import numpy as np
import random
import copy
import sys
import math
import matplotlib.pyplot as plt
import os
from helper import *
a1 = 200
b1 = './HW_data.mat'
b2 = './HW_labels.mat'
def fonk1():
    b3 = read_mat_file(b1, 'data2')
    b4 = read_mat_file(b2, 'b4')
    return b3, b4
def fonk2(point1, point2):
    return math.sqrt(sum((point1[i] - point2[i]) ** 2 for i in range(len(point1))))
def fonk3(point1, point2):
    return sum(abs(point1[i] - point2[i]) for i in range(len(point1)))
def fonk4(point1, point2):
    b5 = sum(point1[i] * point2[i] for i in range(len(point1)))
    b6 = math.sqrt(sum(point1[i] ** 2 for i in range(len(point1))))
    b7 = math.sqrt(sum(point2[i] ** 2 for i in range(len(point2))))
    return b5 / (b6 * b7) if b6 != 0 and b7 != 0 else 1
def fonk5(cluster):
    if not cluster:
        return [0] * 4
    return [sum(instance[1][i] for instance in cluster) / len(cluster) for i in range(len(cluster[0][1]))]
def fonk6(b3, k_values):
    b8 = {}
    b9 = {}
    for b10 in k_values:
        print(f"For b10 = {b10}:")
        b11 = copy.deepcopy(b3)
        b12 = {i: b11.pop(random.randint(0, len(b11)-1)) for i in range(b10)}
        b13 = {i: [[i, center]] for i, center in b12.items()}
        for instance in b11:
            min_dist, b14 = min((fonk2(instance, b12[c]), c) for c in b12)
            b13[b14].append([len(b3) - len(b11), instance])
        for iteration in range(a1):
            for b14 in b13:
                b12[b14] = fonk5(b13[b14])
            for b14 in list(b13.keys()):
                for instance in b13[b14][:]:
                    min_dist, b15 = min((fonk2(instance[1], b12[c]), c) for c in b12)
                    if b15 != b14:
                        b13[b15].append(instance)
                        b13[b14].remove(instance)
            b16 = sum(fonk2(instance[1], b12[c]) ** 2 for c in b13 for instance in b13[c]) / len(b3)
            plt.scatter(iteration, b16, b17 = 'black')
        b8[b10] = b12
        b9[b10] = b13
        b18 = sum(fonk2(instance[1], b12[c]) for c in b13 for instance in b13[c]) / len(b3)
        b19 = sum(fonk2(instance[1], b12[c2]) for c in b13 for instance in b13[c] for c2 in b12 if c2 != c) / len(b3)
        print(f"Inner distance: {b18}")
        print(f"Outer distance: {b19}")
        for b14 in b13:
            b20 = f'./Clusters/{b10}_{b14}_Kcluster.txt'
            with open(b20, 'w') as file:
                for item in b13[b14]:
                    file.write(f"{item}\n")
        plt.show()
    return b8, b9
def fonk7(b3, b4, b10):
    seen_classes, b12 = set(), []
    for ind, instance in enumerate(b3):
        if len(b12) == b10:
            break
        if b4[ind] not in seen_classes:
            seen_classes.add(b4[ind])
            b12.append(ind)
    return b12
def fonk8(count_each_class):
    return count_each_class.index(max(count_each_class)) + 1
def fonk9(b13, b4):
    b21 = {}
    for b10 in b13:
        b21[b10] = {}
        for b14 in b13[b10]:
            b22 = [0, 0, 0]
            for instance in b13[b10][b14]:
                b22[b4[instance[0]][0] - 1] += 1
            b21[b10][b14] = fonk8(b22)
    return b21
def fonk10(b13, b4, b21):
    b23 = {}
    for b10 in b13:
        all_instances, b24 = 0, 0
        for b14 in b13[b10]:
            for instance in b13[b10][b14]:
                all_instances += 1
                if b4[instance[0]][0] != b21[b10][b14]:
                    b24 += 1
        b23[b10] = [all_instances, b24]
    return b23
def fonk11():
    b3, b4 = fonk1()
    b12, b13 = fonk6(b3, [5])
    b13 = b13[5]
    b21 = fonk9(b13, b4)
    b25 = fonk10(b13, b4, b21)
    print(f"Clusters: {b13}")
    print(f"Majority: {b21}")
    print(f"Wrongly Classified Stats: {b25}")
if b26 = = "__main__":
    fonk11()