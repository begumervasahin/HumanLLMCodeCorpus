import copy
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
def fonk2(b20):
    b5 = list()
    for tree in b20:
        b5.append(fonk3(tree))
    return b5
def fonk3(tree):
    b6 = list()
    b7 = dict()
    b8 = dict()
    for node in tree:
        b9 = copy.copy(node)
        b9.b4 = {}
        b7[node] = b9
        b8[b9] = node
    b10 = b7[list(tree.keys())[0]]
    b6.append(b10)
    b11 = False
    while not b11:
        if len(b6) == len(tree):
            b11 = True
        else:
            b6.append(fonk4(b6, tree, b7, b8))
    return b6
def fonk4(b6, tree, b7, b8):
    b12 = class1(0, 0, 0, {})
    a1 = -1
    b13 = class1(0, 0, 0, {})
    b14 = class1(0, 0, 0, {})
    for node in b6:
        b15 = b8[node]
        for child, weight in b15.b4.items():
            if (weight < a1 or a1 = = -1) and b7[child] not in b6:
                a1 = weight
                b12 = b7[child]
                b14 = child
                b13 = node
    b16 = b8[b13]
    del b16.b4[b14]
    del b14.b4[b16]
    b13.b4[b12] = a1
    b12.b4[b13] = a1
    return b12
if b17 = = "__main__":
    b18 = {
        class1(1, 0, 0, {class1(2, 0, 0, {}): 5, class1(3, 0, 0, {}): 6}),
        class1(2, 0, 0, {class1(1, 0, 0, {}): 5, class1(3, 0, 0, {}): 1}),
        class1(3, 0, 0, {class1(1, 0, 0, {}): 6, class1(2, 0, 0, {}): 1})
    }
    b19 = {
        class1(1, 0, 0, {class1(2, 0, 0, {}): 4, class1(3, 0, 0, {}): 1}),
        class1(2, 0, 0, {class1(1, 0, 0, {}): 4, class1(3, 0, 0, {}): 2}),
        class1(3, 0, 0, {class1(1, 0, 0, {}): 1, class1(2, 0, 0, {}): 2})
    }
    b20 = [b18, b19]
    b21 = fonk2(b20)
    for mst in b21:
        print("Minimum Spanning Tree:")
        for node in mst:
            print("class1:", node.b1, "Adjacent Nodes:", [(adj_node.b1, weight) for adj_node, weight in node.b4.items()])