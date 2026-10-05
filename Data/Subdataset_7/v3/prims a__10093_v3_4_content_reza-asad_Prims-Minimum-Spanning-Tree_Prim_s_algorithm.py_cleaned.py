from heapq import heappush, heappop, heapify
from collections import defaultdict
def fonk1(b9):
    b1 = len(b9)
    b2 = set()
    b3 = next(iter(b9.keys()))
    b2.add(b3)
    b4 = list(b9[b3])
    b5 = b4
    heapify(b5)
    b6 = [b3]
    a1 = 0
    while len(b6) != b1:
        b7 = heappop(b5)
        b10, b8 = b7
        if b8 in b2:
            continue
        a1 += b10
        b6.append(b8)
        b2.add(b8)
        for edge_cost, adjacent_vertex in b9[b8]:
            if adjacent_vertex not in b2:
                heappush(b5, (edge_cost, adjacent_vertex))
    return b6, a1
def fonk2(filename):
    b9 = defaultdict(set)
    with open(filename, 'r') as data_file:
        next(data_file)
        for line in data_file:
            vertex1, vertex2, b10 = line.split()
            b10 = int(b10)
            b9[vertex1].add((b10, vertex2))
            b9[vertex2].add((b10, vertex1))
    return b9
if b11 = = "__main__":
    b9 = fonk2('edges.txt')
    mst_nodes, a1 = fonk1(b9)
    print("Minimum Spanning Tree Nodes:", mst_nodes)
    print("Total Cost:", a1)