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
    a2 = 0
    for i in range(len(instance)):
        a2 += (instance[i] - center[i]) ** 2
    return math.sqrt(a2)
def fonk3(instance, center):
    a2 = 0
    for i in range(len(instance)):
        a2 += abs(instance[i] - center[i])
    return a2
def fonk4(instance, center):
    a3 = 0
    a4 = 0
    a5 = 0
    for i in range(len(instance)):
        a3 += instance[i] * center[i]
        a4 += instance[i] ** 2
        a5 += center[i] ** 2
    if a4 = = 0 or a5 == 0:
        return 1
    return a3 / (math.sqrt(a4) * math.sqrt(a5))
def fonk5(cluster):
    if len(cluster) == 0:
        return [0] * len(cluster[0][1])
    b5 = len(cluster[0][1])
    b6 = [sum(instance[1][i] for instance in cluster) / len(cluster) for i in range(b5)]
    return b6
def fonk6(server_data, b9):
    b7 = {}
    b8 = {}
    for k_num in b9:
        print("For b9 = ", k_num, ":")
        b10 = copy.deepcopy(server_data)
        b11 = {}
        b12 = {}
        for i in range(k_num):
            b13 = random.randint(0, len(b10) - 1)
            b11[i] = b10[b13]
            b12[i] = []
            b12[i].append([b13, b10[b13]])
            del b10[b13]
        for b13, ins in enumerate(b10):
            b14 = sys.maxsize
            a6 = -1
            for center in b11.keys():
                b15 = fonk2(ins, b11[center])
                if b15 < b14:
                    b14 = b15
                    a6 = center
            b12[a6].append([b13, ins])
        for inter_num in range(a1):
            for a6 in b12.keys():
                b16 = fonk5(b12[a6])
                b11[a6] = b16
            for a6 in b12.keys():
                a7 = 0
                while a7 < len(b12[a6]):
                    b14 = sys.maxsize
                    a8 = -1
                    for center in b11.keys():
                        b15 = fonk2(b12[a6][a7][1], b11[center])
                        if b15 < b14:
                            b14 = b15
                            a8 = center
                    b12[a8].append(b12[a6][a7])
                    del b12[a6][a7]
                    a7 += 1
            a9 = 0
            for a6 in b12.keys():
                for a7 in range(len(b12[a6])):
                    a9 += (fonk2(b12[a6][a7][1], b11[a6])) ** 2
            a9 /= len(server_data)
            plt.scatter(inter_num, a9, b17 = 'black')
        print('Cluster Centers:')
        print(b11)
        b7[k_num] = b11
        b8[k_num] = b12
        a10 = 0
        a11 = 0
        for center_id in b11.keys():
            for val in b12[center_id]:
                a10 += fonk2(val[1], b11[center_id])
        a10 /= len(server_data)
        for center_id in b11.keys():
            for val in b12[center_id]:
                for b18 in b11.keys():
                    if not b18 = = center_id:
                        a11 += fonk2(val[1], b11[b18])
        a11 /= len(server_data)
        print("Inner b15:", a10)
        print("Outer b15:", a11)
        for a6 in b12.keys():
            b19 = f'./Clusters/{k_num}_{a6}_Kcluster.txt'
            try:
                os.remove(b19)
            except OSError:
                pass
            with open(b19, 'a') as the_file:
                for item in b12[a6]:
                    the_file.write(str(item))
                    the_file.write('\n')
        plt.show()
    return b7, b8
def fonk7(b3, b4, b9):
    seen_classes, b11 = [], []
    for b13, ins in enumerate(b3):
        if len(b11) == b9:
            break
        if b4[b13] not in seen_classes:
            seen_classes.append(b4[b13])
            b11.append(b13)
    return b11
def fonk8(b21):
    if b21[0] >= b21[1] and b21[0] >= b21[2]:
        return 1
    if b21[1] >= b21[0] and b21[1] >= b21[2]:
        return 2
    if b21[2] >= b21[1] and b21[2] >= b21[0]:
        return 3
def fonk9(b24, b4):
    b20 = {}
    for k_val in b24.keys():
        b20[k_val] = {}
        for class_number in b24[k_val].keys():
            b21 = [0, 0, 0]
            for ins in b24[k_val][class_number]:
                b21[b4[ins[0]][0] - 1] += 1
            b20[k_val][class_number] = fonk8(b21)
    return b20
def fonk10(b24, b4, b20):
    b22 = {}
    for k_val in b24.keys():
        all_instances, b23 = 0, 0
        for class_number in b24[k_val].keys():
            for ins in b24[k_val][class_number]:
                all_instances += 1
                if b4[ins[0]][0] != b20[k_val][class_number]:
                    b23 += 1
        b22[k_val] = [all_instances, b23]
    return b22
def fonk11(b3, b4):
    my_centers, b24 = fonk6(b3, [5])
    return b24[5]
if b25 = = "__main__":
    b3, b4 = fonk1()
    fonk11(b3, b4)