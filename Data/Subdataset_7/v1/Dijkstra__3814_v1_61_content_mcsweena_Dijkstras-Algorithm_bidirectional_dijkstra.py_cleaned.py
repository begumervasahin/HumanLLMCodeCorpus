import networkx as nx
import math
from time import time
from collections import deque
from priority_queue import PriorityQueue
def fonk1(b17, start, target):
    b1 = {start}
    b2 = {target}
    b3 = PriorityQueue()
    b4 = PriorityQueue()
    b5 = {b22: (0 if b22 == start else b17[start][b22]["weight"]) for b22 in b17.nodes()}
    b6 = {b22: (0 if b22 == target else b17[target][b22]["weight"]) for b22 in b17.nodes()}
    b7 = {b22: start for b22 in b17.nodes()}
    b8 = {b22: target for b22 in b17.nodes()}
    for b22, dist in b5.items():
        b3.add_task(b22, dist)
    for b22, dist in b6.items():
        b4.add_task(b22, dist)
    b9 = True
    while b9:
        u, b10 = b3.pop_task()
        if u in b1:
            continue
        b1.add(u)
        for v, Dv in b3:
            if v in b1:
                continue
            if b17.has_edge(u, v):
                if b5[v] > b5[u] + b17[u][v]["weight"]:
                    b5[v] = b5[u] + b17[u][v]["weight"]
                    b7[v] = u
                    b3.add_task(v, b5[v])
        if u in b2:
            b9 = False
            b11 = u
            continue
        u, b10 = b4.pop_task()
        if u in b2:
            continue
        b2.add(u)
        for v, Dv in b4:
            if v in b2:
                continue
            if b17.has_edge(u, v):
                if b6[v] > b6[u] + b17[u][v]["weight"]:
                    b6[v] = b6[u] + b17[u][v]["weight"]
                    b8[v] = u
                    b4.add_task(v, b6[v])
        if u in b1:
            b9 = False
            b11 = u
            continue
    b12 = b5[b11] + b6[b11]
    b13 = b11
    for b16 in b17.nodes():
        if b5[b16] + b6[b16] < b12:
            b12 = b5[b16] + b6[b16]
            b13 = b16
            b14 = deque()
        else:
            b14 = deque([b13])
    b15 = b13
    while b15 != start:
        for b16, k in b7.items():
            if b16 = = b15:
                b14.appendleft(k)
                b15 = k
    b15 = b13
    while b15 != target:
        for b16, k in b8.items():
            if b16 = = b15:
                b14.append(k)
                b15 = k
    return list(b14)
def fonk2():
    b17 = nx.Graph()
    b18 = (
        ("A", "B", 2),
        ("A", "C", 6),
        ("A", "D", 8),
        ("B", "b17", 10),
        ("B", "C", 8),
        ("C", "D", 1),
        ("C", "b18", 5),
        ("C", "b17", 9),
        ("C", "F", 3),
        ("D", "F", 9),
        ("b17", "b18", 4),
        ("b18", "F", 1)
    )
    b17.add_weighted_edges_from(b18)
    print(" === NetworkX Shortest b19 = == ")
    b20 = time()
    print("Shortest b19:", nx.dijkstra_path(b17, "A", "b18"))
    b21 = time()
    print("Runtime: {0:6.8f}".format(b21 - b20))
    print("\b22 = = Bidirectional Dijkstra PQ ===")
    b23 = time()
    print("Shortest b19:", fonk1(b17, "A", "b18"))
    b24 = time()
    print("Runtime: {0:6.8f}".format(b24 - b23))
if b25 = = '__main__':
    fonk2()