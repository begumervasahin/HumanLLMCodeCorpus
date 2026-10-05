from helper import *
import numpy as np
import random
import copy
import sys
import math
import matplotlib.pyplot as plt
import os
a1 = 200
b1 = './HW'
b2 = './HW'
def fonk1():
    b3 = read_mat_file(b1, 'data2')
    b4 = read_mat_file(b2, 'b4')
    return b3, b4
def fonk2(ins, center):
    a2 = 0
    for i in range(len(ins)):
        a2 += (ins[i] - center[i]) ** 2
    return math.sqrt(a2)
def fonk3(cluster):
    if len(cluster) == 0:
        return [0] * len(cluster[0][1])
    b5 = [0] * len(cluster[0][1])
    for fieldId in range(len(cluster[0][1])):
        for ins in cluster:
            b5[fieldId] += ins[1][fieldId]
        b5[fieldId] /= len(cluster)
    return b5
def fonk4(server_data, k):
    b6 = {}
    b7 = {}
    for k_num in k:
        b8 = copy.deepcopy(server_data)
        b9 = {}
        b10 = {}
        for i in range(k_num):
            b11 = random.randint(0, len(b8)-1)
            b9[i] = b8[b11]
            b10[i] = []
            b10[i].append([b11, b8[b11]])
            del b8[b11]
        for b11, ins in enumerate(b8):
            b12 = sys.maxsize
            a3 = -1
            for center in b9.keys():
                a2 = fonk2(ins, b9[center])
                if a2 < b12:
                    b12 = a2
                    a3 = center
            b10[a3].append([b11, ins])
        for inter_num in range(a1):
            for a3 in b10.keys():
                b13 = fonk3(b10[a3])
                b9[a3] = b13
            for a3 in b10.keys():
                a4 = 0
                while a4 < len(b10[a3]):
                    b12 = sys.maxsize
                    a5 = -1
                    for center in b9.keys():
                        a2 = fonk2(b10[a3][a4][1], b9[center])
                        if a2 < b12:
                            b12 = a2
                            a5 = center
                    b10[a5].append(b10[a3][a4])
                    del b10[a3][a4]
                a4 += 1
            a6 = 0
            for a3 in b10.keys():
                for a4 in range(len(b10[a3])):
                    a6 += (fonk2(b10[a3][a4][1], b9[a3]))**2
            a6 /= len(server_data)
            plt.scatter(inter_num, a6, b14 = 'black')
        print('Cluster Centers: ')
        print(b9)
        b6[k_num] = b9
        b7[k_num] = b10
        a7 = 0
        a8 = 0
        for centerId in b9.keys():
            for val in b10[centerId]:
                a7 += fonk2(val[1], b9[centerId])
        a7 /= len(server_data)
        for centerId in b9.keys():
            for val in b10[centerId]:
                for b15 in b9.keys():
                    if not b15 = = centerId:
                        a8 += fonk2(val[1], b9[b15])
        a8 /= len(server_data)
        print("Inner a2:", a7)
        print("Outer a2:", a8)
        for a3 in b10.keys():
            b16 = f'./Clusters/{k_num}_{a3}_Kcluster.txt'
            try:
                os.remove(b16)
            except OSError:
                pass
            with open(b16, 'a') as the_file:
                for item in b10[a3]:
                    the_file.write(str(item))
                    the_file.write('\n')
        plt.show()
    return b6, b7
def fonk5():
    b3, b4 = fonk1()
    b17 = fonk4(b3, [5])
    return b17[5]
if b18 = = "__main__":
    fonk5()