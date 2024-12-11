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
    b5 = {}
    b6 = {}
    b7 = {}
    b8 = {}
    for b9 in b17.nodes():
        if b9 = = start:
            b5[b9] = 0
        else:
            b5[b9] = b17[start][b9]["weight"] if b17.has_edge(start, b9) else math.inf
            b7[b9] = start
            b3.add_task(b9, b5[b9])
        if b9 = = target:
            b6[b9] = 0
        else:
            b6[b9] = b17[target][b9]["weight"] if b17.has_edge(target, b9) else math.inf
            b8[b9] = target
            b4.add_task(b9, b6[b9])
    while True:
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
            b11 = u
            break
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
            b11 = u
            break
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
    print("\b9 = = Bidirectional Dijkstra PQ ===")
    b22 = time()
    print("Shortest b19:", fonk1(b17, "A", "b18"))
    b23 = time()
    print("Runtime: {0:6.8f}".format(b23 - b22))
if b24 = = '__main__':
    fonk2()