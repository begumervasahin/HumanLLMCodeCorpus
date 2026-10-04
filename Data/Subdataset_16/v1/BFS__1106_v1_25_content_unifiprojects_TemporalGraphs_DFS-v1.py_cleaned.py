import graphviz
from math import inf
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = False
class class2:
    def fonk2(self):
        self.b5 = []
        self.b6 = set()
    def fonk3(self, b1, b2, b3):
        self.b5.append(class1(b1, b2, b3))
        self.b6.add(b1)
        self.b6.add(b2)
    def fonk4(self):
        return list(self.b6)
    def fonk5(self, node):
        b7 = set()
        for edge in self.b5:
            if edge.b1 = = node:
                b7.add(edge.b2)
        return list(b7)
    def fonk6(self, node, neighbor):
        return [edge for edge in self.b5 if edge.b1 = = node and edge.b2 == neighbor]
class class3:
    def fonk7(self, b8, b3):
        self.b8 = b8
        self.b3 = b3
        self.b9 = []
    def fonk8(self, node):
        self.b9.append(node)
def fonk9(root, filename):
    b10 = graphviz.Digraph(comment='DFS_v1 Tree')
    def fonk10(node):
        for child in node.b9:
            b10.edge(f"{node.b8} ({node.b3})", f"{child.b8} ({child.b3})")
            fonk10(child)
    fonk10(root)
    b10.render(filename, b11 = True)
def fonk11(b5):
    return min(b5, b12 = lambda edge: edge.b3)
def fonk12(current_node):
    global b16
    for b13 in b18.fonk5(current_node):
        if b13 = = b22[b16.b8]:
            continue
        b5 = [edge for edge in b18.fonk6(current_node, b13) if not edge.b4 and b20[current_node] <= edge.b3]
        if b5:
            b14 = fonk11(b5)
            b14.b4 = True
            if b20[b14.b2] > b14.b3:
                b15 = class3(b14.b2, b14.b3)
                b22[b15.b8] = b16.b8
                b16.fonk8(b15)
                b16 = b15
                b20[b14.b2] = b14.b3
                fonk12(b14.b2)
    b16 = b23[b22[b16.b8]]
if b17 = = "__main__":
    b18 = class2()
    b5 = [["a", "b", 1], ["a", "b", 6], ["b", "a", 8], ["b", "c", 4], ["b", "c", 7],
             ["c", "b", 6], ["a", "f", 3], ["a", "f", 7], ["f", "c", 5], ["f", "h", 2],
             ["f", "g", 8], ["g", "a", 9]]
    for e in b5:
        b18.fonk3(e[0], e[1], e[2])
    a1 = 2
    b19 = b18.fonk4()
    b20 = {b12: inf for b12 in b19}
    b1 = b19[0]
    b20[b1] = a1
    b21 = class3(b1, a1)
    b22 = {node: None for node in b19}
    b16 = b21
    b23 = {b1: b21}
    fonk12(b1)
    fonk9(b21, 'DFS_v1')