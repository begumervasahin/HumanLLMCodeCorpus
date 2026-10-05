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
    b8 = []
    b9 = []
    for a2 in range(b3):
        b8.append(a2)
        b9.append(0)
    a1 = 0
    a2 = 0
    while a1 < b3 - 1:
        u, v, b10 = b7[a2]
        a2 = a2 + 1
        b11 = fonk1(b8, u)
        b12 = fonk1(b8, v)
        if b11 != b12:
            a1 = a1 + 1
            b4.append([u, v, b10])
            fonk2(b8, b9, b11, b12)
    return b4
def fonk4(graph):
    b13 = [False] * graph.get_num_vertices()
    b14 = []
    for item in range(graph.get_num_vertices()):
        if b13[item] == False:
            fonk5(graph, item, b13, b14)
    return b14
def fonk5(graph, v, b13, b14):
    b13[v] = True
    b15 = time.perf_counter()
    for item in graph.get_vertices_reachable_from(v):
        if b13[item] == False:
            fonk5(graph, item, b13, b14)
    b14.insert(0, v)
b16 = GraphAM(initial_num_vertices=11, is_directed=True)
b16.add_edge(0, 1, 2)
b16.add_edge(0, 2, 3)
b16.add_edge(0, 3, 4)
b16.add_edge(1, 4, 2)
b16.add_edge(2, 5, 2)
b16.add_edge(3, 6, 5)
b16.add_edge(4, 7, 1)
b16.add_edge(5, 8, 3)
b16.add_edge(6, 9, 8)
b16.add_edge(7, 10, 5)
b16.add_edge(8, 10, 6)
b16.add_edge(9, 10, 2)
print("Topological sort: ", fonk4(b16))
print('Kruskal b4: ')
b4 = fonk3(b16)
for u, v, weight in b4:
    print("From " + str(u) + " to " + str(v) + " weight is " + str(weight))
b17 = GraphAM(initial_num_vertices=7, is_directed=True)
b17.add_edge(0, 1, 4)
b17.add_edge(0, 4, 2)
b17.add_edge(4, 5, 4)
b17.add_edge(4, 1, 5)
b17.add_edge(5, 2, 8)
b17.add_edge(5, 1, 1)
b17.add_edge(5, 6, 2)
b17.add_edge(2, 1, 6)
b17.add_edge(6, 3, 4)
b17.add_edge(6, 2, 7)
b17.add_edge(3, 2, 5)
print("Topological sort: ", fonk4(b17))
print('Kruskal b4: ')
b4 = fonk3(b17)
for u, v, weight in b4:
    print("From " + str(u) + " to " + str(v) + " weight is " + str(weight))