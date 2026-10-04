import numpy as np
import random
import copy
import sys
import math
import matplotlib.pyplot as plt
import os
a1 = 200
b1 = './HW_data.mat'
b2 = './HW_labels.mat'
def fonk1(file_path, variable_name):
    return np.random.rand(100, 4)
def fonk2():
    b3 = fonk1(b1, 'data2')
    b4 = fonk1(b2, 'b4')
    return b3, b4
def fonk3(ins, center):
    return math.sqrt(sum((ins[i] - center[i]) ** 2 for i in range(len(ins))))
def fonk4(ins, center):
    return sum(abs(ins[i] - center[i]) for i in range(len(ins)))
def fonk5(ins, center):
    b5 = sum(ins[i] * center[i] for i in range(len(ins)))
    b6 = math.sqrt(sum((ins[i]) ** 2 for i in range(len(ins))))
    b7 = math.sqrt(sum((center[i]) ** 2 for i in range(len(ins))))
    return b5 / (b6 * b7) if b6 != 0 and b7 != 0 else 1
def fonk6(cluster):
    if len(cluster) == 0:
        return [0] * 4
    return [sum(ins[1][i] for ins in cluster) / len(cluster) for i in range(len(cluster[0][1]))]
def fonk7(b3, k_values):
    b8 = {}
    b9 = {}
    for b10 in k_values:
        print(f"For b10 = {b10}:")
        b11 = copy.deepcopy(b3)
        b12 = {i: b11.pop(random.randint(0, len(b11)-1)) for i in range(b10)}
        b13 = {i: [[i, center]] for i, center in b12.items()}
        for ins in b11:
            min_dist, b14 = min((fonk3(ins, b12[c]), c) for c in b12)
            b13[b14].append([len(b3) - len(b11), ins])
        for iteration in range(a1):
            for b14 in b13:
                b12[b14] = fonk6(b13[b14])
            for b14 in list(b13.keys()):
                for ins in b13[b14]:
                    min_dist, b15 = min((fonk3(ins[1], b12[c]), c) for c in b12)
                    if b15 != b14:
                        b13[b15].append(ins)
                        b13[b14].remove(ins)
            b16 = sum(fonk3(ins[1], b12[c])**2 for c in b13 for ins in b13[c]) / len(b3)
            plt.scatter(iteration, b16, b17 = 'black')
        b8[b10] = b12
        b9[b10] = b13
        b18 = sum(fonk3(ins[1], b12[c]) for c in b13 for ins in b13[c]) / len(b3)
        b19 = sum(fonk3(ins[1], b12[c2]) for c in b13 for ins in b13[c] for c2 in b12 if c2 != c) / len(b3)
        print(f"Inner distance: {b18}")
        print(f"Outer distance: {b19}")
        for b14 in b13:
            b20 = f'./Clusters/{b10}_{b14}_Kcluster.txt'
            with open(b20, 'w') as file:
                for item in b13[b14]:
                    file.write(f"{item}\n")
        plt.show()
    return b8, b9
def fonk8(b3, b4, b10):
    seen_classes, b12 = set(), []
    for ind, ins in enumerate(b3):
        if len(b12) == b10:
            break
        if b4[ind] not in seen_classes:
            seen_classes.add(b4[ind])
            b12.append(ind)
    return b12
def fonk9(count_each_class):
    return count_each_class.index(max(count_each_class)) + 1
def fonk10(b13, b4):
    b21 = {}
    for b10 in b13:
        b21[b10] = {}
        for b14 in b13[b10]:
            b22 = [0, 0, 0]
            for ins in b13[b10][b14]:
                b22[b4[ins[0]][0] - 1] += 1
            b21[b10][b14] = fonk9(b22)
    return b21
def fonk11(b13, b4, b21):
    b23 = {}
    for b10 in b13:
        all_instances, b24 = 0, 0
        for b14 in b13[b10]:
            for ins in b13[b10][b14]:
                all_instances += 1
                if b4[ins[0]][0] != b21[b10][b14]:
                    b24 += 1
        b23[b10] = [all_instances, b24]
    return b23
def fonk12():
    b3, b4 = fonk2()
    b12, b13 = fonk7(b3, [5])
    b13 = b13[5]
    b21 = fonk10(b13, b4)
    b25 = fonk11(b13, b4, b21)
    print(f"Clusters: {b13}")
    print(f"Majority: {b21}")
    print(f"Wrongly Classified Stats: {b25}")
if b26 = = "__main__":
    fonk12()