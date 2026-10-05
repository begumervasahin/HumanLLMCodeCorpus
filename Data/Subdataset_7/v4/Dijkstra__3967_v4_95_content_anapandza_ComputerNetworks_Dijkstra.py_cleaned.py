def fonk1(b5):
    b1 = float('inf')
    b2 = None
    for key, value in b5.items():
        if value < b1:
            b1 = value
            b2 = key
    del b5[b2]
    return b2
def fonk2(b8, start_node):
    b3 = {}
    b4 = {}
    b5 = {}
    for node in b8:
        b3[node] = float('inf')
        b4[node] = -1
    b3[start_node] = 0
    for node in b8:
        b5[node] = b3[node]
    while b5:
        b6 = fonk1(b5)
        for neighbor, weight in b8[b6].items():
            b7 = b3[b6] + weight
            if b7 < b3[neighbor]:
                b3[neighbor] = b7
                b4[neighbor] = b6
                b5[neighbor] = b7
    return b3, b4
b8 = {
    0: {1: 6, 2: 1, 3: 4},
    1: {4: 3},
    2: {1: -3, 3: 2},
    3: {4: -1},
    4: {2: 5},
}
shortest_distances, b4 = fonk2(b8, 0)
print("Shortest distance from start node 0 to all other nodes:")
for node, distance in shortest_distances.items():
    print(f"{node} = {distance}")
print("Predecessors of nodes in the shortest paths:")
for node, predecessor in b4.items():
    print(f"{node} = {predecessor}")