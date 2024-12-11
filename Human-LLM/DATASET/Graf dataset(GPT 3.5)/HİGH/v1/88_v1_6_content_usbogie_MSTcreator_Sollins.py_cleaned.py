import copy
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
def fonk2(trees):
    b5 = []
    for tree in trees:
        b5.append(fonk3(tree))
    return b5
def fonk3(tree):
    b6 = []
    b7 = {}
    b8 = {}
    for n in tree:
        b9 = []
        b10 = copy.copy(n)
        b10.b4 = {}
        b7[n] = b10
        b8[b10] = n
        b9.append(b10)
        b6.append(b9)
    while len(b6) != 1:
        b6 = fonk4(b6, tree, b7, b8)
    return b6.pop(0)
def fonk4(b6, tree, b7, b8):
    for subtree in b6:
        b11 = class1(0, 0, 0, {})
        a1 = -1
        b12 = class1(0, 0, 0, {})
        for n in subtree:
            b13 = b8[n]
            for p in b13.b4:
                b14 = b7[p]
                if b14 not in subtree and (b13.b4[p] < a1 or a1 = = -1):
                    a1 = b13.b4[p]
                    b11 = b14
                    b12 = n
        fonk5(b6, subtree, b12, b11, a1)
    return b6
def fonk5(b6, subtree, b12, b11, a1):
    b15 = []
    for sub in b6:
        if b11 in sub:
            b15 = sub
    b12.b4[b11] = a1
    b11.b4[b12] = a1
    for b3 in subtree:
        b15.append(b3)
    b6.remove(subtree)
    return b6
if b16 = = "__main__":
    b17 = [class1(1, 0, 0, {2: 10, 3: 15}), class1(2, 0, 0, {1: 10, 3: 5}), class1(3, 0, 0, {1: 15, 2: 5})]
    b18 = [class1(1, 0, 0, {2: 8, 3: 9}), class1(2, 0, 0, {1: 8, 3: 7}), class1(3, 0, 0, {1: 9, 2: 7})]
    b19 = fonk2([b17, b18])
    for idx, mst in enumerate(b19):
        print(f"MST {idx+1}: {[(node.b1, node.b4) for node in mst]}")