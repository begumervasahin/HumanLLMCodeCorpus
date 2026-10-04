import sys
import heapq
from DisjointSet import DisjointSet
def fonk1(b15):
    with open(b15) as graph:
        b1 = {}
        b2 = set()
        b3 = []
        for line in graph:
            vertex1, vertex2, b4 = line.split()
            b4 = int(b4)
            if vertex1 not in b1:
                b1[vertex1] = []
                b2.add(vertex1)
            if vertex2 not in b1:
                b1[vertex2] = []
                b2.add(vertex2)
            b1[vertex1].append((vertex2, b4))
            b1[vertex2].append((vertex1, b4))
            b3.extend([vertex1, vertex2])
        for vertex in b1:
            print(f"{vertex}: {b1[vertex]}")
        b5 = (0, b3[0])
        b6 = {b3[0]: 0}
        b7 = {b3[0]: '-'}
        b8 = {v: (0, '-') for v in b2}
        b9 = []
        heapq.heappush(b9, b5)
        b10 = list(b2)
        b10.remove(b3[0])
        a1 = 0
        while b9:
            b5 = heapq.heappop(b9)
            current_distance, b11 = b5
            if b11 in b10:
                b10.remove(b11)
                a1 += current_distance
                for neighbor, b4 in b1.get(b11, []):
                    if neighbor in b10:
                        heapq.heappush(b9, (b4, neighbor))
                        if b6.get(neighbor, sys.maxsize) > b4:
                            b6[neighbor] = b4
                            b7[neighbor] = b11
                            b8[neighbor] = (b4, neighbor, b11)
        print(f"Prim's total a1: {a1} with b12:")
        return b8
def fonk2(b15):
    with open(b15) as graph:
        b12 = []
        b3 = {}
        a2 = 0
        for line in graph:
            vertex1, vertex2, b4 = line.split()
            b4 = int(b4)
            b12.append((b4, vertex1, vertex2))
            if vertex1 not in b3:
                b3[vertex1] = a2
                a2 += 1
            if vertex2 not in b3:
                b3[vertex2] = a2
                a2 += 1
        b13 = DisjointSet(len(b3))
        b12.sort()
        a3 = 0
        b8 = []
        for b4, vertex1, vertex2 in b12:
            if b13.find(b3[vertex1]) != b13.find(b3[vertex2]):
                b13.union(b3[vertex1], b3[vertex2])
                b8.append((b4, vertex1, vertex2))
                a3 += b4
        return a3, b8
if b14 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python mst.py [input file] [prims | kruskals]")
        sys.exit(1)
    b15 = sys.argv[1]
    b16 = sys.argv[2]
    if b16 = = 'prims':
        b17 = fonk1(b15)
        for key, value in b17.items():
            print(f"Edge from {value[2]} to {value[1]} with b4 {value[0]}")
    elif b16 = = 'kruskals':
        total, b17 = fonk2(b15)
        print(f"Kruskal's total a1: {total} with b12:")
        for edge in b17:
            print(f"Edge from {edge[1]} to {edge[2]} with b4 {edge[0]}")
    else:
        print("Illegal b16. Must be either 'prims' or 'kruskals'.")
        sys.exit(1)