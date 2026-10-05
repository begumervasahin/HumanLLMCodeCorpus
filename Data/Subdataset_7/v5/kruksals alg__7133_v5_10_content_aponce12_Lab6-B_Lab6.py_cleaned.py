import os
import random
import time
import re
import math
from Graphs.GraphAM import GraphAM
from Graphs.GraphAL import GraphAL
def fonk1(b8, a2):
    if b8[a2] == a2:
        return a2
    return fonk1(b8, b8[a2])
def fonk2(b8, b9, b11, b12):
    b1 = fonk1(b8, b11)
    b2 = fonk1(b8, b12)
    if b9[b1] < b9[b2]:
        b8[b1] = b2
    elif b9[b1] > b9[b2]:
        b8[b2] = b1
    else:
        b8[b2] = b1
        b9[b1] += 1
def fonk3(graph):
    b3 = graph.get_num_vertices()
    b4 = []
    b5 = []
    for a2 in range(b3):
        for j in range(b3):
            if graph.adj_matrix[a2][j] != 0 and (j, a2) not in b5:
                b6 = graph.adj_matrix[a2][j]
                b5.append([a2, j, b6])
    b7 = sorted(b5, key=lambda a1: graph.adj_matrix[a1[0]][a1[1]])
    b8 = [a2 for a2 in range(b3)]
    b9 = [0] * b3
    a1 = 0
    a2 = 0
    while a1 < b3 - 1:
        u, v, b10 = b7[a2]
        a2 += 1
        b11 = fonk1(b8, u)
        b12 = fonk1(b8, v)
        if b11 != b12:
            a1 += 1
            b4.append([u, v, b10])
            fonk2(b8, b9, b11, b12)
    return b4
def fonk4(graph):
    b13 = [False] * graph.get_num_vertices()
    b14 = []
    for item in range(graph.get_num_vertices()):
        if not b13[item]:
            fonk5(graph, item, b13, b14)
    return b14
def fonk5(graph, v, b13, b14):
    b13[v] = True
    for item in graph.get_vertices_reachable_from(v):
        if not b13[item]:
            fonk5(graph, item, b13, b14)
    b14.insert(0, v)
b15 = GraphAM(initial_num_vertices=11, is_directed=True)
b15.add_edge(0, 1, 2)
print("Topological sort: ", fonk4(b15))
print('Kruskal b4: ')
b4 = fonk3(b15)
for u, v, weight in b4:
    print("From " + str(u) + " to " + str(v) + " weight is " + str(weight))
b16 = GraphAM(initial_num_vertices=7, is_directed=True)
print("Topological sort: ", fonk4(b16))
print('Kruskal b4: ')
b4 = fonk3(b16)
for u, v, weight in b4:
    print("From " + str(u) + " to " + str(v) + " weight is " + str(weight))