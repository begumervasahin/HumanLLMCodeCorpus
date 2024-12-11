import networkx as nx
import math
from time import time
from collections import deque
from priority_queue import PriorityQueue
def fonk1(b18, start, target):
    b1 = {start}
    b2 = {target}
    b3 = PriorityQueue()
    b4 = PriorityQueue()
    b5 = {}
    b6 = {}
    b7 = {}
    b8 = {}
    for b9 in b18.nodes():
        if b9 = = start:
            b5[b9] = 0
        else:
            if b18.has_edge(start, b9):
                b5[b9] = b18[start][b9]["weight"]
            else:
                b5[b9] = math.inf
            b7[b9] = start
            b3.add_task(b9, b5[b9])
    for b9 in b18.nodes():
        if b9 = = target:
            b6[b9] = 0
        else:
            if b18.has_edge(target, b9):
                b6[b9] = b18[target][b9]["weight"]
            else:
                b6[b9] = math.inf
            b8[b9] = target
            b4.add_task(b9, b6[b9])
    b10 = True
    while b10 != False:
        u, b11 = b3.pop_task()
        if u in b1: continue
        b1.add(u)
        for v, Dv in b3:
            if v in b1: continue
            if b18.has_edge(u, v):
                if b5[v] > b5[u] + b18[u][v]["weight"]:
                    b5[v] = b5[u] + b18[u][v]["weight"]
                    b7[v] = u
                    b3.add_task(v, b5[v])
        if u in b2:
            b10 = False
            b12 = u
            continue
        else:
            pass
        u, b11 = b4.pop_task()
        if u in b2: continue
        b2.add(u)
        for v, Dv in b4:
            if v in b2: continue
            if b18.has_edge(u, v):
                if b6[v] > b6[u] + b18[u][v]["weight"]:
                    b6[v] = b6[u] + b18[u][v]["weight"]
                    b8[v] = u
                    b4.add_task(v, b6[v])
        if u in b1:
            b10 = False
            b12 = u
            continue
        else:
            pass
    b13 = b5[b12] + b6[b12]
    b14 = b12
    for b17 in b18.nodes():
        if b5[b17] + b6[b17] < b13:
            b13 = b5[b17] + b6[b17]
            b14 = b17
            b15 = deque()
        else:
            b15 = deque([b14])
    b16 = b14
    while b16 != start:
        for b17, k in b7.items():
            if b17 = = b16:
                b15.appendleft(k)
                b16 = k
    b16 = b14
    while b16 != target:
        for b17, k in b8.items():
            if b17 = = b16:
                b15.append(k)
                b16 = k
    return list(b15)
def fonk2():
    b18 = nx.Graph()
    b19 = (
        ("A", "B", 2),
        ("A", "C", 6),
        ("A", "D", 8),
        ("B", "b18", 10),
        ("B", "C", 8),
        ("C", "D", 1),
        ("C", "b19", 5),
        ("C", "b18", 9),
        ("C", "F", 3),
        ("D", "F", 9),
        ("b18", "b19", 4),
        ("b19", "F", 1)
    )
    b18.add_weighted_edges_from(b19)
    print(" === NetworkX Shortest b20 = == ")
    b21 = time()
    print("Shortest b20:", nx.dijkstra_path(b18, "A", "b19"))
    b22 = time()
    print("Runtime: {0:6.8f}".format(b22 - b21))
    print("\b9 = = Bidirectional Dijkstra PQ ===")
    b23 = time()
    print("Shortest b20:", fonk1(b18, "A", "b19"))
    b24 = time()
    print("Runtime: {0:6.8f}".format(b24 - b23))
if b25 = = '__main__':
    fonk2()