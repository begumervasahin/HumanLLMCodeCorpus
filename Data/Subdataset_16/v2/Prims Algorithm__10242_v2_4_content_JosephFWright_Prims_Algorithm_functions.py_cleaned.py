
class class1:
    def fonk1(self, filename):
        self.b1 = set()
        self.b2 = {}
        with open(filename, 'r') as file:
            for line in file:
                v1, v2, b3 = line.split()
                b3 = int(b3)
                self.b1.add(v1)
                self.b1.add(v2)
                self.b2[(v1, v2)] = b3
                self.b2[(v2, v1)] = b3
    def fonk2(self):
        return self.b2
    def fonk3(self):
        return set(self.b2.keys())
    def fonk4(self):
        return self.b1
from class1 import class1
def fonk5(edge, b12):
    return b12.fonk2()[edge]
def fonk6(b14, b12):
    b2 = set()
    for vertex in b14[0]:
        for edge in b12.fonk3():
            if vertex in edge:
                b2.add(edge)
    return b2.difference(b14[1])
def fonk7(b14, b12):
    b2 = fonk6(b14, b12)
    b4 = set()
    b5 = set(b14[0])
    b6 = b12.fonk4().difference(b5)
    for edge in b2:
        if edge[0] in b5 and edge[1] in b5:
            b4.add(edge)
    return b2.difference(b4)
def fonk8(b14, b12):
    b2 = fonk7(b14, b12)
    return min(b2, b7 = lambda edge: fonk5(edge, b12))
def fonk9(b14, b12):
    b1, b2 = b14
    b8 = fonk8(b14, b12)
    b9 = b2 + [b8]
    b10 = set(b1).union(b8)
    return (b10, b9)
def fonk10(b14, b12):
    return sum(fonk5(edge, b12) for edge in b14[1])
if b11 = = "__main__":
    b12 = class1('test_graph.txt')
    b13 = 'A'
    b14 = ([b13], [])
    while len(b14[0]) < len(b12.fonk4()):
        b14 = fonk9(b14, b12)
    print("Total cost of MST:", fonk10(b14, b12))
    print("Edges in MST:", b14[1])