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
    b5 = sum(ins[i]*center[i] for i in range(len(ins)))
    b6 = math.sqrt(sum((ins[i])**2 for i in range(len(ins))))
    b7 = math.sqrt(sum((center[i])**2 for i in range(len(ins))))
    return b5 / (b6 * b7) if b6 != 0 and b7 != 0 else 1
def fonk6(cluster):
    if len(cluster) == 0:
        return [0] * 4
    b8 = [sum(ins[1][fieldId] for ins in cluster) / len(cluster) for fieldId in range(len(cluster[0][1]))]
    return b8
def fonk7(server_data, k_values):
    b9 = {}
    b10 = {}
    for k_num in k_values:
        print(f"For b11 = {k_num}:")
        b12 = copy.deepcopy(server_data)
        b13 = {i: b12.pop(random.randint(0, len(b12)-1)) for i in range(k_num)}
        b14 = {i: [[i, center]] for i, center in b13.items()}
        for ins in b12:
            minDist, b15 = min((fonk3(ins, b13[center]), center) for center in b13)
            b14[b15].append([len(server_data) - len(b12) + i, ins])
        for inter_num in range(a1):
            for b15 in b14:
                b13[b15] = fonk6(b14[b15])
            for b15 in b14:
                for insId in range(len(b14[b15])):
                    minDist, b16 = min((fonk3(b14[b15][insId][1], b13[center]), center) for center in b13)
                    b14[b16].append(b14[b15][insId])
                    del b14[b15][insId]
            b17 = sum(fonk3(ins[1], b13[b15])**2 for b15 in b14 for ins in b14[b15]) / len(server_data)
            plt.scatter(inter_num, b17, b18 = 'black')
        b9[k_num] = b13
        b10[k_num] = b14
        b19 = sum(fonk3(val[1], b13[centerId]) for centerId in b13 for val in b14[centerId]) / len(server_data)
        b20 = sum(fonk3(val[1], b13[centerId2]) for centerId in b13 for val in b14[centerId] for centerId2 in b13 if centerId2 != centerId) / len(server_data)
        print(f"Inner dist: {b19}")
        print(f"Outer dist: {b20}")
        for b15 in b14:
            b21 = f'./Clusters/{k_num}_{b15}_Kcluster.txt'
            with open(b21, 'w') as the_file:
                for item in b14[b15]:
                    the_file.write(str(item) + '\n')
        plt.show()
    return b9, b10
def fonk8(b3, b4, b11):
    seen_classes, b13 = [], []
    for ind, ins in enumerate(b3):
        if len(b13) == b11:
            break
        if b4[ind] not in seen_classes:
            seen_classes.append(b4[ind])
            b13.append(ind)
    return b13
def fonk9(b23):
    return b23.index(max(b23)) + 1
def fonk10(b26, b4):
    b22 = {}
    for kVal in b26:
        b22[kVal] = {}
        for classNumber in b26[kVal]:
            b23 = [0, 0, 0]
            for ins in b26[kVal][classNumber]:
                b23[b4[ins[0]][0]-1] += 1
            b22[kVal][classNumber] = fonk9(b23)
    return b22
def fonk11(b26, b4, b22):
    b24 = {}
    for kVal in b26:
        all_instances, b25 = 0, 0
        for classNumber in b26[kVal]:
            for ins in b26[kVal][classNumber]:
                all_instances += 1
                if b4[ins[0]][0] != b22[kVal][classNumber]:
                    b25 += 1
        b24[kVal] = [all_instances, b25]
    return b24
def fonk12():
    b3, b4 = fonk2()
    myCenters, b26 = fonk7(b3, [5])
    b14 = b26[5]
    b22 = fonk10(b26, b4)
    b27 = fonk11(b26, b4, b22)
    print(f"Clusters: {b14}")
    print(f"Majority: {b22}")
    print(f"Wrongly Classified Stats: {b27}")
if b28 = = "__main__":
    fonk12()