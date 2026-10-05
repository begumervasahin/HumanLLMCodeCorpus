import copy
from Node import Node
def fonk1(trees):
    b1 = []
    for tree in trees:
        b1.append(fonk2(tree))
    return b1
def fonk2(tree):
    b2 = []
    b3 = {}
    b4 = {}
    for node in tree:
        b5 = copy.copy(node)
        b5.b6 = {}
        b3[node] = b5
        b4[b5] = node
    b7 = b3[next(iter(tree))]
    b2.append(b7)
    while len(b2) < len(tree):
        b8 = fonk3(b2, tree, b3, b4)
        b2.append(b8)
    return b2
def fonk3(b2, tree, b3, b4):
    b9 = None
    b10 = float('inf')
    b11 = None
    b12 = None
    for node in b2:
        b13 = b4[node]
        for adjacent_node, weight in b13.b6.items():
            if (weight < b10) and (b3[adjacent_node] not in b2):
                b10 = weight
                b9 = b3[adjacent_node]
                b12 = adjacent_node
                b11 = node
    if b11 is not None and b9 is not None:
        b14 = b4[b11]
        del b14.b6[b12]
        del b12.b6[b14]
        b11.b6[b9] = b10
        b9.b6[b11] = b10
    return b9