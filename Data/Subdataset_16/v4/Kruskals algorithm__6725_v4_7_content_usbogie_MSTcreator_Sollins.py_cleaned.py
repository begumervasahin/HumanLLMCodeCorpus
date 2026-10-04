import copy
from Node import Node
def fonk1(trees):
    return [fonk2(tree) for tree in trees]
def fonk2(tree):
    b1 = []
    b2 = {}
    b3 = {}
    for node in tree:
        b4 = copy.copy(node)
        b4.b5 = {}
        b2[node] = b4
        b3[b4] = node
        b1.append([b4])
    while len(b1) > 1:
        b1 = fonk3(b1, tree, b2, b3)
    return b1[0]
def fonk3(b1, tree, b2, b3):
    for subtree in b1:
        parent, child, b6 = fonk4(subtree, b2, b3)
        if parent and child:
            fonk5(b1, subtree, parent, child, b6)
    return b1
def fonk4(subtree, b2, b3):
    b6 = float('inf')
    b7 = b10 = None
    for b4 in subtree:
        b8 = b3[b4]
        for neighbor, weight in b8.b5.items():
            b9 = b2[neighbor]
            if b9 not in subtree and weight < b6:
                b6 = weight
                b7 = b4
                b10 = b9
    return b7, b10, b6
def fonk5(b1, subtree, parent, child, weight):
    b11 = next(sub for sub in b1 if child in sub)
    parent.b5[child] = weight
    child.b5[parent] = weight
    b11.extend(subtree)
    b1.remove(subtree)