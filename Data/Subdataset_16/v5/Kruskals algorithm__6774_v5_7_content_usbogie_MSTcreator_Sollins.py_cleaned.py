import copy
from Node import Node
def fonk1(trees):
    return [fonk2(tree) for tree in trees]
def fonk2(tree):
    b1 = fonk3(tree)
    b3, b2 = fonk4(tree, b1)
    while len(b1) > 1:
        b1 = fonk5(b1, tree, b3, b2)
    return b1[0]
def fonk3(tree):
    return [[copy.copy(node)] for node in tree]
def fonk4(tree, b1):
    b3 = {}
    b2 = {}
    for subtree in b1:
        b4 = subtree[0]
        b4.b5 = {}
        b6 = next(node for node in tree if node == b4)
        b3[b6] = b4
        b2[b4] = b6
    return b3, b2
def fonk5(b1, tree, b3, b2):
    for subtree in b1:
        parent, child, b7 = fonk6(subtree, b3, b2)
        if parent and child:
            fonk7(b1, subtree, parent, child, b7)
    return b1
def fonk6(subtree, b3, b2):
    b7 = float('inf')
    b8 = b10 = None
    for b4 in subtree:
        b6 = b2[b4]
        for neighbor, weight in b6.b5.items():
            b9 = b3[neighbor]
            if b9 not in subtree and weight < b7:
                b7 = weight
                b8 = b4
                b10 = b9
    return b8, b10, b7
def fonk7(b1, subtree, parent, child, weight):
    b11 = next(sub for sub in b1 if child in sub)
    parent.b5[child] = weight
    child.b5[parent] = weight
    b11.extend(subtree)
    b1.remove(subtree)