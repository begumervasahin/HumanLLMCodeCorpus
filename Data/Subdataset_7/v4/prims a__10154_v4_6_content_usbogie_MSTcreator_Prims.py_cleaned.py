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
    b8 = False
    while not b8:
        if len(b2) == len(tree):
            b8 = True
        else:
            b9 = fonk3(b2, tree, b3, b4)
            b2.append(b9)
    return b2
def fonk3(b2, tree, b3, b4):
    b10 = Node(0, 0, 0, {})
    a1 = -1
    b11 = Node(0, 0, 0, {})
    b12 = Node(0, 0, 0, {})
    for node in b2:
        b13 = b4[node]
        for adjacent_node, weight in b13.b6.items():
            if (weight < a1 or a1 = = -1) and b3[adjacent_node] not in b2:
                a1 = weight
                b10 = b3[adjacent_node]
                b12 = adjacent_node
                b11 = node
    b14 = b4[b11]
    del b14.b6[b12]
    del b12.b6[b14]
    b11.b6[b10] = a1
    b10.b6[b11] = a1
    return b10