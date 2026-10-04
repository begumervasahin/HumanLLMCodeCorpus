
class class1:
    def fonk1(self, filename):
        self.b1 = set()
        self.b2 = {}
        self.fonk2(filename)
    def fonk2(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                v1, v2, b3 = line.split()
                b3 = int(b3)
                self.b1.update([v1, v2])
                self.b2[(v1, v2)] = b3
                self.b2[(v2, v1)] = b3
    def fonk3(self):
        return self.b2
    def fonk4(self):
        return set(self.b2.keys())
    def fonk5(self):
        return self.b1
from class1 import class1
def fonk6(edge, b15):
    return b15.fonk3()[edge]
def fonk7(b13, b15):
    b4 = set()
    tree_vertices, b5 = b13
    for vertex in tree_vertices:
        for edge in b15.fonk4():
            if vertex in edge:
                b4.add(edge)
    return b4 - set(b5)
def fonk8(b13, b15):
    b6 = fonk7(b13, b15)
    tree_vertices, b7 = b13
    for edge in b6.copy():
        if edge[0] in tree_vertices and edge[1] in tree_vertices:
            b6.remove(edge)
    return b6
def fonk9(b13, b15):
    b8 = fonk8(b13, b15)
    return min(b8, b9 = lambda edge: fonk6(edge, b15))
def fonk10(b13, b15):
    tree_vertices, b5 = b13
    b10 = fonk9(b13, b15)
    b11 = b5 + [b10]
    b12 = tree_vertices.union(b10)
    return b12, b11
def fonk11(b13, b15):
    return sum(fonk6(edge, b15) for edge in b13[1])
def fonk12(b15, b16):
    b13 = (set([b16]), [])
    while len(b13[0]) < len(b15.fonk5()):
        b13 = fonk10(b13, b15)
    return b13
if b14 = = "__main__":
    b15 = class1('test_graph.txt')
    b16 = 'A'
    b17 = fonk12(b15, b16)
    print("Total cost of MST:", fonk11(b17, b15))
    print("Edges in MST:", b17[1])