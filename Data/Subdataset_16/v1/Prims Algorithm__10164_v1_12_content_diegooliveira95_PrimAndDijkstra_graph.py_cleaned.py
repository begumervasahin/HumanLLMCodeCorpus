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
        return str(self.b1) + ' b2: ' + str([x.b1 for x in self.b2])
class class2:
    def fonk11(self):
        self.b7 = {}
        self.a1 = 0
    def fonk12(self):
        return iter(self.b7.values())
    def fonk13(self, node):
        self.a1 += 1
        b8 = class1(node)
        self.b7[node] = b8
        return b8
    def fonk14(self, node):
        if node in self.b7:
            return self.b7[node]
        else:
            return None
    def fonk15(self, from_node, to_node, b9 = 0):
        if from_node not in self.b7:
            return 'from_node not in graph'
        if to_node not in self.b7:
            return 'to_node not in graph'
        self.b7[from_node].fonk2(self.b7[to_node], b9)
        self.b7[to_node].fonk2(self.b7[from_node], b9)
    def fonk16(self):
        return self.b7.keys()
    def fonk17(self, current):
        self.b5 = current
    def fonk18(self, current):
        return self.b5
if b10 = = "__main__":
    b11 = class2()
    b11.fonk13('a')
    b11.fonk13('b')
    b11.fonk13('c')
    b11.fonk15('a', 'b', 1)
    b11.fonk15('b', 'c', 2)
    b11.fonk15('a', 'c', 4)
    for v in b11:
        print(f"class1 {v.fonk4()}")
        print(f"Distance: {v.fonk7()}")
        print(f"Connections: {[x.fonk4() for x in v.fonk3()]}")
        print('-----')