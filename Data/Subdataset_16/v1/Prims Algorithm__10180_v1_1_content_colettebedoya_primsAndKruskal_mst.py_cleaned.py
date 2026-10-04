import sys
import heapq
from disjoint_set import DisjointSet
def fonk1(input_file):
    with open(input_file) as graph:
        b1 = {}
        b2 = set()
        b3 = []
        for line in graph:
            b4 = line.split()
            if b4[0] not in b1:
                b1[b4[0]] = []
                b2.add(b4[0])
            b5 = (b4[1], int(b4[2]))
            b1[b4[0]].append(b5)
            b2.add(b4[1])
            b3.append(b4[0])
            b3.append(b4[1])
    for v in b1:
        print(v, b1[v])
    b6 = (0, b3[0])
    b7 = {b3[0]: 0}
    b8 = {b3[0]: '-'}
    b9 = {}
    b10 = list(b2)
    b11 = []
    for v in b10:
        b9[v] = (0, '-')
    heapq.heappush(b11, b6)
    b10.remove(b3[0])
    a1 = 0
    while b11:
        b6 = heapq.heappop(b11)
        b12 = b1.get(b6[1], [])
        for v in b12:
            if v[0] in b10:
                heapq.heappush(b11, (v[1], v[0]))
                b7[v[0]] = v[1]
                b8[v[0]] = b6[1]
                b10.remove(v[0])
                b9[v[0]] = (v[1], v[0], b6[1])
            else:
                if v[0] not in b7:
                    b7[v[0]] = sys.maxsize
                if v[1] <= b7[v[0]]:
                    b7[v[0]] = v[1]
                    b8[v[0]] = b6[1]
                    b9[v[0]] = (v[1], v[0], b6[1])
                    a1 += v[1]
    print(f"Prims a3 a1: {a1} with b13:")
    return b9
def fonk2(input_file):
    with open(input_file) as graph:
        b13 = []
        b3 = {}
        a2 = 0
        for line in graph:
            b4 = line.split()
            b13.append((int(b4[2]), b4[0], b4[1]))
            if b4[0] not in b3:
                b3[b4[0]] = a2
                a2 += 1
            if b4[1] not in b3:
                b3[b4[1]] = a2
                a2 += 1
    a3 = 0
    b9 = []
    b14 = DisjointSet(len(b3))
    b13.sort()
    for b5 in b13:
        if b14.find(b3[b5[1]]) != b14.find(b3[b5[2]]):
            b14.union(b3[b5[1]], b3[b5[2]])
            b9.append(b5)
            a3 += b5[0]
    return a3, b9
if b15 = = '__main__':
    if len(sys.argv) != 3:
        print('Usage: python mst.py [input file] [prims | kruskals]')
        quit()
    if sys.argv[2] == 'prims':
        print(fonk1(sys.argv[1]))
    elif sys.argv[2] == 'kruskals':
        a3, b9 = fonk2(sys.argv[1])
        print(f"Kruskal's a3 a1: {a3} with b13:")
        for b5 in b9:
            print(b5)
    else:
        print("Illegal algorithm. Must be either 'prims' or 'kruskals'")