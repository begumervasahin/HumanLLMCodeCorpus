import sys
class class1:
    def fonk1(self, node):
        self.b1 = node
        self.b2 = {}
        self.b3 = sys.maxsize
        self.b4 = False
        self.b5 = None
    def fonk2(self, neighbor, b6 = 0):
        self.b2[neighbor] = b6
    def fonk3(self):
        return self.b2.keys()
    def fonk4(self):
        return self.b1
    def fonk5(self, neighbor):
        return self.b2[neighbor]
    def fonk6(self, b3):
        self.b3 = b3
    def fonk7(self):
        return self.b3
    def fonk8(self, b5):
        self.b5 = b5
    def fonk9(self):
        self.b4 = True
    def fonk10(self):
        b7 = ', '.join([x.b1 for x in self.b2])
        return f"{self.b1} b2: {b7}"
class class2:
    def fonk11(self):
        self.b8 = {}
        self.a1 = 0
    def fonk12(self):
        return iter(self.b8.values())
    def fonk13(self, node):
        self.a1 += 1
        b9 = class1(node)
        self.b8[node] = b9
        return b9
    def fonk14(self, node):
        return self.b8.get(node)
    def fonk15(self, from_node, to_node, b10 = 0):
        if from_node not in self.b8:
            raise ValueError(f"class1 '{from_node}' not in graph")
        if to_node not in self.b8:
            raise ValueError(f"class1 '{to_node}' not in graph")
        self.b8[from_node].fonk2(self.b8[to_node], b10)
        self.b8[to_node].fonk2(self.b8[from_node], b10)
    def fonk16(self):
        return self.b8.keys()
if b11 = = "__main__":
    b12 = class2()
    b12.fonk13('a')
    b12.fonk13('b')
    b12.fonk13('c')
    b12.fonk15('a', 'b', 1)
    b12.fonk15('b', 'c', 2)
    b12.fonk15('a', 'c', 4)
    for vertex in b12:
        print(f"class1 {vertex.fonk4()}")
        print(f"Distance: {vertex.fonk7()}")
        print(f"Connections: {[x.fonk4() for x in vertex.fonk3()]}")
        print('-----')