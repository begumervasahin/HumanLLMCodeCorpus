import copy
from Node import Node
def fonk1(trees):
    return [fonk2(tree) for tree in trees]
def fonk2(tree):
    b1 = fonk3(tree)
    while len(b1) > 1:
        b1 = fonk4(b1, tree)
    return b1[0]
def fonk3(tree):
    b1 = []
    b2 = {}
    b3 = {}
    for node in tree:
        b4 = copy.copy(node)
        b4.b5 = {}
        b2[node] = b4
        b3[b4] = node
        b1.append([b4])
    return b1
def fonk4(b1, tree):
    for subtree in b1:
        parent, b7, b6 = fonk5(subtree, tree)
        if parent and b7:
            fonk6(b1, subtree, parent, b7, b6)
    return b1
def fonk5(subtree, tree):
    b6 = float('inf')
    parent, b7 = None, None
    for node in subtree:
        b8 = b3[node]
        for neighbor, weight in b8.b5.items():
            b9 = b2[neighbor]
            if b9 not in subtree and weight < b6:
                b6 = weight
                parent, b7 = node, b9
    return parent, b7, b6
def fonk6(b1, subtree, parent, b7, weight):
    b10 = next(sub for sub in b1 if b7 in sub)
    if b10:
        parent.b5[b7] = weight
        b7.b5[parent] = weight
        subtree.extend(b10)
        b1.remove(b10)