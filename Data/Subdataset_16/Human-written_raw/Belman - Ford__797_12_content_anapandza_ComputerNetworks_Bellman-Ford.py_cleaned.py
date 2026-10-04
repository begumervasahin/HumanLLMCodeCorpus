import pdb
def fonk1(b3, source):
    b1 = {}
    b2 = {}
    for node in b3:
        b1[node] = float('Inf')
        b2[node] = None
    b1[source] = 0
    return b1, b2
def fonk2(node, neighbour, b3, b1, b2):
    if b1[neighbour] > b1[node] + b3[node][neighbour]:
        b1[neighbour]  = b1[node] + b3[node][neighbour]
        b2[neighbour] = node
def fonk3(b3, source):
    b1, b2 = fonk1(b3, source)
    for i in range(len(b3)-1):
        for u in b3:
            for v in b3[u]:
                fonk2(u, v, b3, b1, b2)
    for u in b3:
        for v in b3[u]:
            assert b1[v] <= b1[u] + b3[u][v]
    return b1, b2
def fonk4():
    b3 = {
        'a': {'b': -2, 'c': 1, 'b1': 4},
        'b': {'e': 3},
        'c': {'b': -3, 'b1': 2},
        'b1': {'e': -1},
        'e': {'c': 5}
        }
    b1, b2 = fonk3(b3, 'a')
    print ("The shortest distance from source a to all other nodes is:")
    for u in b3:
        print(u,"=",b1[u])
    print ("Paths from source a to all other nodes(predecessors of nodes):")
    for u in b3:
        print(u,"=",b2[u])
if b4 = = '__main__': fonk4()