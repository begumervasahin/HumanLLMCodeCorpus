import pdb
def fonk1(b4, source):
    b1 = {node: float('Inf') for node in b4}
    b2 = {node: None for node in b4}
    b1[source] = 0
    return b1, b2
def fonk2(node, neighbor, b4, b1, b2):
    b3 = b1[node] + b4[node][neighbor]
    if b1[neighbor] > b3:
        b1[neighbor] = b3
        b2[neighbor] = node
def fonk3(b4, source):
    b1, b2 = fonk1(b4, source)
    for _ in range(len(b4) - 1):
        for node in b4:
            for neighbor in b4[node]:
                fonk2(node, neighbor, b4, b1, b2)
    for node in b4:
        for neighbor in b4[node]:
            if b1[neighbor] > b1[node] + b4[node][neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    return b1, b2
def fonk4():
    b4 = {
        'a': {'b': -2, 'c': 1, 'd': 4},
        'b': {'e': 3},
        'c': {'b': -3, 'd': 2},
        'd': {'e': -1},
        'e': {'c': 5}
    }
    b1, b2 = fonk3(b4, 'a')
    print("The shortest b1 from source 'a' to all other nodes are:")
    for node in b4:
        print(f"{node} = {b1[node]}")
    print("\nThe paths (b2) from source 'a' to all other nodes are:")
    for node in b4:
        print(f"{node} = {b2[node]}")
if b5 = = '__main__':
    fonk4()