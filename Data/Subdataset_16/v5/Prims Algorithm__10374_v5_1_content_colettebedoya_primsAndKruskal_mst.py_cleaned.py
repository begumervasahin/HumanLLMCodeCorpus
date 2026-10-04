import sys
import heapq
from DisjointSet import DisjointSet
def fonk1(b13):
    b1 = {}
    b2 = set()
    with open(b13) as graph:
        for line in graph:
            vertex1, vertex2, b3 = line.split()
            b3 = int(b3)
            if vertex1 not in b1:
                b1[vertex1] = []
            if vertex2 not in b1:
                b1[vertex2] = []
            b1[vertex1].append((vertex2, b3))
            b1[vertex2].append((vertex1, b3))
            b2.update([vertex1, vertex2])
    return b1, list(b2)
def fonk2(b13):
    b1, b2 = fonk1(b13)
    for vertex, neighbors in b1.items():
        print(f"{vertex}: {neighbors}")
    b4 = b2[0]
    b5 = [(0, b4)]
    b6 = set()
    a1 = 0
    b7 = []
    while b5:
        b3, b8 = heapq.heappop(b5)
        if b8 in b6:
            continue
        b6.add(b8)
        a1 += b3
        if b3 != 0:
            b7.append((b9, b8, b3))
        for neighbor, edge_weight in b1[b8]:
            if neighbor not in b6:
                heapq.heappush(b5, (edge_weight, neighbor))
                b9 = b8
    print(f"Prim's total cost: {a1} with b10:")
    return b7
def fonk3(b13):
    b10 = []
    b2 = {}
    a2 = 0
    with open(b13) as graph:
        for line in graph:
            vertex1, vertex2, b3 = line.split()
            b3 = int(b3)
            b10.append((b3, vertex1, vertex2))
            if vertex1 not in b2:
                b2[vertex1] = a2
                a2 += 1
            if vertex2 not in b2:
                b2[vertex2] = a2
                a2 += 1
    b11 = DisjointSet(len(b2))
    b10.sort()
    a1 = 0
    b7 = []
    for b3, vertex1, vertex2 in b10:
        if b11.find(b2[vertex1]) != b11.find(b2[vertex2]):
            b11.union(b2[vertex1], b2[vertex2])
            b7.append((b3, vertex1, vertex2))
            a1 += b3
    return a1, b7
if b12 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python mst.py [input file] [prims | kruskals]")
        sys.exit(1)
    b13 = sys.argv[1]
    b14 = sys.argv[2]
    if b14 = = 'prims':
        b15 = fonk2(b13)
        for edge in b15:
            print(f"Edge from {edge[0]} to {edge[1]} with b3 {edge[2]}")
    elif b14 = = 'kruskals':
        total_cost, b15 = fonk3(b13)
        print(f"Kruskal's total cost: {total_cost} with b10:")
        for edge in b15:
            print(f"Edge from {edge[1]} to {edge[2]} with b3 {edge[0]}")
    else:
        print("Illegal b14. Must be either 'prims' or 'kruskals'.")
        sys.exit(1)