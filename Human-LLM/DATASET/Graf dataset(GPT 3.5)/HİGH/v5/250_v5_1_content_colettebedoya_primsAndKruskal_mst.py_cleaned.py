import sys
import heapq
from DisjointSet import DisjointSet
def fonk1(b18):
    b1 = open(b18)
    b2 = {}
    b3 = set()
    b4 = set()
    for line in b1:
        b5 = line.split()
        node1, b15, b6 = b5[0], b5[1], int(b5[2])
        b2.setdefault(node1, []).append((b15, b6))
        b2.setdefault(b15, []).append((node1, b6))
        b3.update([node1, b15])
        b4.update([node1, b15])
    return b2, b3, b4
def fonk2(b18):
    b2, b3, b4 = fonk1(b18)
    b7 = (0, next(iter(b4)))
    b8 = {node: float('inf') for node in b4}
    b9 = {node: None for node in b4}
    b10 = {}
    b11 = list(b3)
    b12 = []
    heapq.heappush(b12, b7)
    b11.remove(b7[1])
    a1 = 0
    while b12:
        b7 = heapq.heappop(b12)
        b13 = b2.get(b7[1], [])
        for neighbor, b6 in b13:
            if neighbor in b11:
                heapq.heappush(b12, (b6, neighbor))
                b8[neighbor] = b6
                b9[neighbor] = b7[1]
                b11.remove(neighbor)
                b10[neighbor] = (b6, neighbor, b7[1])
            else:
                if b6 < b8[neighbor]:
                    b8[neighbor] = b6
                    b9[neighbor] = b7[1]
                    b10[neighbor] = (b6, neighbor, b7[1])
                    a1 += b6
    print("Prims total cost: %d with b14:" % a1)
    return b10
def fonk3(b18):
    b1 = open(b18)
    b14 = []
    b4 = {}
    a2 = 0
    for line in b1:
        b5 = line.split()
        b6, node1, b15 = int(b5[2]), b5[0], b5[1]
        b14.append((b6, node1, b15))
        if node1 not in b4:
            b4[node1] = a2
            a2 += 1
    a1 = 0
    b10 = []
    b16 = DisjointSet(len(b4))
    b14.sort()
    for b6, node1, b15 in b14:
        if b16.find(b4[node1]) != b16.find(b4[b15]):
            b16.union(b4[node1], b4[b15])
            b10.append((b6, node1, b15))
            a1 += b6
    return a1, b10
if b17 = = '__main__':
    if len(sys.argv) != 3:
        print('Usage python mst1.py [input file] [prims | kruskals]')
        quit()
    b18 = sys.argv[1]
    b19 = sys.argv[2]
    if b19 = = 'prims':
        print(fonk2(b18))
    elif b19 = = 'kruskals':
        print(fonk3(b18))
    else:
        print('Illegal b19. Must be either \'prims\' or \'kruskals\' ')