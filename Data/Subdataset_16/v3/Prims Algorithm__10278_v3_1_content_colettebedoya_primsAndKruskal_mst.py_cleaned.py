import sys
import heapq
from b12 import DisjointSet
def fonk1(b17):
    b1 = {}
    b2 = set()
    b3 = set()
    with open(b17) as graph:
        for line in graph:
            vertex1, vertex2, b4 = line.split()
            b4 = int(b4)
            if vertex1 not in b1:
                b1[vertex1] = []
            if vertex2 not in b1:
                b1[vertex2] = []
            b1[vertex1].append((vertex2, b4))
            b1[vertex2].append((vertex1, b4))
            b2.add(vertex1)
            b2.add(vertex2)
            b3.update([vertex1, vertex2])
    return b1, b2, list(b3)
def fonk2(b17):
    b1, b2, b3 = fonk1(b17)
    b5 = b3[0]
    b6 = {node: sys.maxsize for node in b3}
    b7 = {node: None for node in b3}
    b6[b5] = 0
    b8 = [(0, b5)]
    b9 = []
    a1 = 0
    while b8:
        current_cost, b10 = heapq.heappop(b8)
        if current_cost > b6[b10]:
            continue
        for neighbor, b4 in b1[b10]:
            if b4 < b6[neighbor]:
                b6[neighbor] = b4
                b7[neighbor] = b10
                heapq.heappush(b8, (b4, neighbor))
                b9.append((b10, neighbor, b4))
                a1 += b4
    print(f"Prim's total cost: {a1}")
    return b9
def fonk3(b17):
    b1, _, b3 = fonk1(b17)
    b11 = [(b4, v1, v2) for v1 in b1 for v2, b4 in b1[v1]]
    b11 = list(set(b11))
    b11.sort()
    b12 = DisjointSet(len(b3))
    b13 = {node: idx for idx, node in enumerate(b3)}
    a1 = 0
    b9 = []
    for b4, v1, v2 in b11:
        b14 = b12.find(b13[v1])
        b15 = b12.find(b13[v2])
        if b14 != b15:
            b12.union(b14, b15)
            b9.append((v1, v2, b4))
            a1 += b4
    print(f"Kruskal's total cost: {a1}")
    return b9
if b16 = = '__main__':
    if len(sys.argv) != 3:
        print('Usage: python mst.py [input file] [prims | kruskals]')
        sys.exit(1)
    b17 = sys.argv[1]
    b18 = sys.argv[2]
    if b18 = = 'prims':
        b9 = fonk2(b17)
    elif b18 = = 'kruskals':
        b9 = fonk3(b17)
    else:
        print("Illegal b18. Must be either 'prims' or 'kruskals'")
        sys.exit(1)
    for edge in b9:
        print(edge)