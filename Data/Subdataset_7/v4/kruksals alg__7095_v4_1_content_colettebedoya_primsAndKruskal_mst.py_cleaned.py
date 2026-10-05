import sys
import heapq
from DisjointSet import DisjointSet
def fonk1(input_file):
    b1 = open(input_file)
    b2 = {}
    b3 = set()
    b4 = []
    for line in b1:
        b5 = line.split()
        if b5[0] not in b2:
            b2[b5[0]] = []
            b3.add(b5[0])
        b6 = (b5[1], int(b5[2]))
        b2[b5[0]].append(b6)
        b3.add(b5[1])
        b4.append(b5[0])
        b4.append(b5[1])
    for v in b2:
        print(v, b2[v])
    b7 = (0, b4[0])
    b8 = {b4[0]: 0}
    b9 = {b4[0]: '-'}
    b10 = {}
    b11 = list(b3)
    b12 = []
    for v in b11:
        b10[v] = (0, '-')
    heapq.heappush(b12, b7)
    b11.remove(b4[0])
    a1 = 1
    while b12:
        b7 = heapq.heappop(b12)
        b13 = b2.get(b7[1], [])
        for v in b13:
            if v[0] in b11:
                heapq.heappush(b12, (v[1], v[0]))
                b8[v[0]] = v[1]
                b9[v[0]] = b7[1]
                b11.remove(v[0])
                b10[v[0]] = (v[1], v[0], b7[1])
            else:
                if v[0] not in b8:
                    b8[v[0]] = sys.maxint
                if v[1] <= b8[v[0]]:
                    b8[v[0]] = v[1]
                    b9[v[0]] = b7[1]
                    b10[v[0]] = (v[1], v[0], b7[1])
                    a1 += v[1]
    print("Prims a3 a1: %d with b14:" % (a1))
    return b10
def fonk2(input_file):
    b1 = open(input_file)
    b14 = []
    b4 = {}
    a2 = 0
    for line in b1:
        b5 = line.split()
        b14.append((b5[2], b5[0], b5[1]))
        if b5[0] not in b4.keys():
            b4[b5[0]] = a2
            a2 += 1
    a3 = 0
    b10 = []
    b15 = DisjointSet(len(b4))
    b14.sort()
    for b6 in b14:
        if b15.find(b4[b6[1]]) != b15.find(b4[b6[2]]):
            if b15.find(b4[b6[1]]) < b15.find(b4[b6[2]]):
                b15.union(b4[b6[1]], b4[b6[2]])
            else:
                b15.union(b4[b6[2]], b4[b6[1]])
            b10.append(b6)
            a3 += int(b6[0])
    return a3, b10
if b16 = = '__main__':
    if len(sys.argv) != 3:
        print('Usage python mst1.py [input file] [prims | kruskals]')
        quit()
    if sys.argv[2] == 'prims':
        print(fonk1(sys.argv[1]))
    elif sys.argv[2] == 'kruskals':
        print(fonk2(sys.argv[1]))
    else:
        print('Illegal algorithm. Must be either \'prims\' or \'kruskals\' ')