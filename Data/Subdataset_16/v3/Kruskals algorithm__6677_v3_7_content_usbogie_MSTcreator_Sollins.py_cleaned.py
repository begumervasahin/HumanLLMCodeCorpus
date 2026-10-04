import copy
from Node import Node
def fonk1(trees):
    return [fonk2(tree) for tree in trees]
def fonk2(tree):
    b1 = fonk3(tree)
    while len(b1) > 1:
        b1 = fonk4(b1)
    return b1[0]
def fonk3(tree):
    b2 = {}
    b3 = {}
    b1 = []
    for node in tree:
        b4 = copy.copy(node)
        b4.b5 = {}
        b2[node] = b4
        b3[b4] = node
        b1.append([b4])
    return b1
def fonk4(b1):
    for subtree in b1:
        parent, b8, b6 = fonk5(subtree)
        if parent and b8:
            fonk6(b1, subtree, parent, b8, b6)
    return b1
def fonk5(subtree):
    b7 = float('inf')
    parent, b8 = None, None
    for node in subtree:
        b9 = b3[node]
        for neighbor, b6 in b9.b5.items():
            b10 = b2[neighbor]
            if b10 not in subtree and b6 < b7:
                b7 = b6
                parent, b8 = node, b10
    return parent, b8, b7
def fonk6(b1, subtree, parent, b8, b6):
    b11 = next(sub for sub in b1 if b8 in sub)
    if b11:
        parent.b5[b8] = b6
        b8.b5[parent] = b6
        subtree.extend(b11)
        b1.remove(b11)