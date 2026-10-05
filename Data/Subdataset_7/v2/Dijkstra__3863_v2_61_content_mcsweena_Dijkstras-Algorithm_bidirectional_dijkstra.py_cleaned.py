import networkx as nx
import math
from time import time
from collections import deque
from priority_queue import PriorityQueue
def fonk1(b16, start, target):
    b1 = {start}
    b2 = {target}
    b3 = PriorityQueue()
    b4 = PriorityQueue()
    b5 = {b21: 0 if b21 == start else b16[start][b21]["weight"] for b21 in b16.nodes()}
    b6 = {b21: 0 if b21 == target else b16[target][b21]["weight"] for b21 in b16.nodes()}
    b7 = {b21: start for b21 in b16.nodes()}
    b8 = {b21: target for b21 in b16.nodes()}
    for b21, dist in b5.items():
        b3.add_task(b21, dist)
    for b21, dist in b6.items():
        b4.add_task(b21, dist)
    while True:
        u, b9 = b3.pop_task()
        if u in b1:
            continue
        b1.add(u)
        for v, Dv in b3:
            if v in b1:
                continue
            if b16.has_edge(u, v):
                if b5[v] > b5[u] + b16[u][v]["weight"]:
                    b5[v] = b5[u] + b16[u][v]["weight"]
                    b7[v] = u
                    b3.add_task(v, b5[v])
        if u in b2:
            b10 = u
            break
        u, b9 = b4.pop_task()
        if u in b2:
            continue
        b2.add(u)
        for v, Dv in b4:
            if v in b2:
                continue
            if b16.has_edge(u, v):
                if b6[v] > b6[u] + b16[u][v]["weight"]:
                    b6[v] = b6[u] + b16[u][v]["weight"]
                    b8[v] = u
                    b4.add_task(v, b6[v])
        if u in b1:
            b10 = u
            break
    b11 = b5[b10] + b6[b10]
    b12 = b10
    for b15 in b16.nodes():
        if b5[b15] + b6[b15] < b11:
            b11 = b5[b15] + b6[b15]
            b12 = b15
            b13 = deque()
        else:
            b13 = deque([b12])
    b14 = b12
    while b14 != start:
        for b15, k in b7.items():
            if b15 = = b14:
                b13.appendleft(k)
                b14 = k
    b14 = b12
    while b14 != target:
        for b15, k in b8.items():
            if b15 = = b14:
                b13.append(k)
                b14 = k
    return list(b13)
def fonk2():
    b16 = nx.Graph()
    b17 = (
        ("A", "B", 2),
        ("A", "C", 6),
        ("A", "D", 8),
        ("B", "b16", 10),
        ("B", "C", 8),
        ("C", "D", 1),
        ("C", "b17", 5),
        ("C", "b16", 9),
        ("C", "F", 3),
        ("D", "F", 9),
        ("b16", "b17", 4),
        ("b17", "F", 1)
    )
    b16.add_weighted_edges_from(b17)
    print(" === NetworkX Shortest b18 = == ")
    b19 = time()
    print("Shortest b18:", nx.dijkstra_path(b16, "A", "b17"))
    b20 = time()
    print("Runtime: {0:6.8f}".format(b20 - b19))
    print("\b21 = = Bidirectional Dijkstra PQ ===")
    b22 = time()
    print("Shortest b18:", fonk1(b16, "A", "b17"))
    b23 = time()
    print("Runtime: {0:6.8f}".format(b23 - b22))
if b24 = = '__main__':
    fonk2()