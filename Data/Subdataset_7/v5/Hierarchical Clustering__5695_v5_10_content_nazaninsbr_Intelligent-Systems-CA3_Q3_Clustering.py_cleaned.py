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
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(instance, center)))
def fonk3(instance, center):
    return sum(abs(x - y) for x, y in zip(instance, center))
def fonk4(instance, center):
    b5 = sum(x * y for x, y in zip(instance, center))
    b6 = math.sqrt(sum(x ** 2 for x in instance))
    b7 = math.sqrt(sum(y ** 2 for y in center))
    if b6 = = 0 or b7 == 0:
        return 1
    return b5 / (b6 * b7)
def fonk5(cluster):
    b8 = len(cluster[0][1])
    return [sum(instance[1][i] for instance in cluster) / len(cluster) for i in range(b8)]
def fonk6(server_data, b11):
    b9 = {}
    b10 = {}
    for k_num in b11:
        print("For b11 = ", k_num, ":")
        b12 = copy.deepcopy(server_data)
        b13 = {}
        b14 = {}
        for i in range(k_num):
            b15 = random.randint(0, len(b12) - 1)
            b13[i] = b12[b15]
            b14[i] = [[b15, b12[b15]]]
            del b12[b15]
        for b15, ins in enumerate(b12):
            b16 = sys.maxsize
            a2 = -1
            for center in b13.keys():
                b17 = fonk2(ins, b13[center])
                if b17 < b16:
                    b16 = b17
                    a2 = center
            b14[a2].append([b15, ins])
        for _ in range(a1):
            for a2 in b14.keys():
                b18 = fonk5(b14[a2])
                b13[a2] = b18
            for a2 in b14.keys():
                a3 = 0
                while a3 < len(b14[a2]):
                    b16 = sys.maxsize
                    a4 = -1
                    for center in b13.keys():
                        b17 = fonk2(b14[a2][a3][1], b13[center])
                        if b17 < b16:
                            b16 = b17
                            a4 = center
                    b14[a4].append(b14[a2][a3])
                    del b14[a2][a3]
                    a3 += 1
            b19 = sum(fonk2(instance[1], b13[a2]) ** 2
                            for a2 in b14.keys()
                            for instance in b14[a2]) / len(server_data)
            plt.scatter(_, b19, b20 = 'black')
        print('Cluster Centers:')
        print(b13)
        b9[k_num] = b13
        b10[k_num] = b14
        b21 = sum(fonk2(val[1], b13[center_id])
                         for center_id in b13.keys()
                         for val in b14[center_id]) / len(server_data)
        b22 = sum(fonk2(val[1], b13[center_id2])
                         for center_id in b13.keys()
                         for val in b14[center_id]
                         for center_id2 in b13.keys()
                         if center_id2 != center_id) / len(server_data)
        print("Inner b17:", b21)
        print("Outer b17:", b22)
        for a2 in b14.keys():
            b23 = f'./Clusters/{k_num}_{a2}_Kcluster.txt'
            try:
                os.remove(b23)
            except OSError:
                pass
            with open(b23, 'a') as the_file:
                for item in b14[a2]:
                    the_file.write(str(item))
                    the_file.write('\n')
        plt.show()
    return b9, b10
def fonk7(b3, b4, b11):
    seen_classes, b13 = set(), []
    for b15, ins in enumerate(b3):
        if len(b13) == b11:
            break
        if b4[b15] not in seen_classes:
            seen_classes.add(b4[b15])
            b13.append(b15)
    return b13
def fonk8(b25):
    return b25.index(max(b25)) + 1
def fonk9(b28, b4):
    b24 = {}
    for k_val in b28.keys():
        b24[k_val] = {}
        for class_number in b28[k_val].keys():
            b25 = [0] * len(set(b4))
            for ins in b28[k_val][class_number]:
                b25[b4[ins[0]][0] - 1] += 1
            b24[k_val][class_number] = fonk8(b25)
    return b24
def fonk10(b28, b4, b24):
    b26 = {}
    for k_val in b28.keys():
        all_instances, b27 = 0, 0
        for class_number in b28[k_val].keys():
            for ins in b28[k_val][class_number]:
                all_instances += 1
                if b4[ins[0]][0] != b24[k_val][class_number]:
                    b27 += 1
        b26[k_val] = [all_instances, b27]
    return b26
def fonk11(b3, b4):
    my_centers, b28 = fonk6(b3, [5])
    return b28[5]
if b29 = = "__main__":
    b3, b4 = fonk1()
    fonk11(b3, b4)