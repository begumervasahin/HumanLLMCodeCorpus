def fonk1(pqueue):
    b1 = min(pqueue, key=pqueue.get)
    del pqueue[b1]
    return b1
def fonk2(b7, start):
    b2 = {node: float('inf') for node in b7}
    b3 = {node: -1 for node in b7}
    b4 = {node: float('inf') for node in b7}
    b2[start] = 0
    b4[start] = 0
    while b4:
        b5 = fonk1(b4)
        for neighbor, weight in b7[b5].items():
            b6 = b2[b5] + weight
            if b6 < b2[neighbor]:
                b2[neighbor] = b6
                b3[neighbor] = b5
                b4[neighbor] = b6
    return b2, b3
b7 = {
    0: {1: 6, 2: 1, 3: 4},
    1: {4: 3},
    2: {1: -3, 3: 2},
    3: {4: -1},
    4: {2: 5},
}
shortest_distances, b3 = fonk2(b7, 0)
print("Shortest b2 from start node 0 to all other nodes:")
for node, distance in shortest_distances.items():
    print(f"{node} = {distance}")
print("Predecessors of nodes in the shortest paths:")
for node, predecessor in b3.items():
    print(f"{node} = {predecessor}")