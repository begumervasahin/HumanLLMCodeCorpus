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
    for n in tree:
        b5 = []
        b6 = copy.copy(n)
        b6.b7 = {}
        b3[n] = b6
        b4[b6] = n
        b5.append(b6)
        b2.append(b5)
    while len(b2) > 1:
        b2 = fonk3(b2, tree, b3, b4)
    return b2.pop(0)
def fonk3(b2, tree, b3, b4):
    for subtree in b2:
        b8 = None
        b9 = float('inf')
        b10 = None
        for n in subtree:
            b11 = b4[n]
            for neighbor, weight in b11.b7.items():
                b12 = b3[neighbor]
                if b12 not in subtree and weight < b9:
                    b9 = weight
                    b8 = b12
                    b10 = n
        if b10 and b8:
            fonk4(b2, subtree, b10, b8, b9)
    return b2
def fonk4(b2, subtree, b10, b8, b9):
    b13 = next((sub for sub in b2 if b8 in sub), None)
    if b13:
        b10.b7[b8] = b9
        b8.b7[b10] = b9
        for node in subtree:
            b13.append(node)
        b2.remove(subtree)
    return b2