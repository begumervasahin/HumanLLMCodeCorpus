class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
        self.b3 = 'white'
        self.b4 = None
        self.a1 = 0
        self.a2 = 0
    def fonk2(self, neighbor, b5 = 0):
        self.b2[neighbor] = b5
    def fonk3(self, b3):
        self.b3 = b3
    def fonk4(self, b4):
        self.b4 = b4
    def fonk5(self, a4):
        self.a1 = a4
    def fonk6(self, a4):
        self.a2 = a4
    def fonk7(self):
        return self.b2.keys()
    def fonk8(self):
        return self.b3
    def fonk9(self):
        return self.b4
    def fonk10(self):
        return self.a1
    def fonk11(self):
        return self.a2
    def fonk12(self):
        return self.b1
    def fonk13(self, neighbor):
        return self.b2[neighbor]
    def fonk14(self):
        return f"{self.b1} connected to: {[x.b1 for x in self.b2]}"
class class2:
    def fonk15(self):
        self.b6 = {}
        self.a3 = 0
    def fonk16(self, key):
        self.a3 += 1
        b7 = class1(key)
        self.b6[key] = b7
        return b7
    def fonk17(self, key):
        return self.b6.get(key)
    def fonk18(self, key):
        return key in self.b6
    def fonk19(self, from_vertex, to_vertex, b5 = 0):
        if from_vertex not in self.b6:
            self.fonk16(from_vertex)
        if to_vertex not in self.b6:
            self.fonk16(to_vertex)
        self.b6[from_vertex].fonk2(self.b6[to_vertex], b5)
    def fonk20(self):
        return self.b6.keys()
    def fonk21(self):
        return iter(self.b6.values())
class class3(class2):
    def fonk22(self):
        super().fonk22()
        self.a4 = 0
    def fonk23(self):
        for vertex in self:
            vertex.fonk3('white')
            vertex.fonk4(None)
        for vertex in self:
            if vertex.fonk8() == 'white':
                self.fonk24(vertex)
    def fonk24(self, vertex):
        vertex.fonk3('gray')
        self.a4 += 1
        vertex.fonk5(self.a4)
        for next_vertex in vertex.fonk7():
            if next_vertex.fonk8() == 'white':
                next_vertex.fonk4(vertex)
                self.fonk24(next_vertex)
        vertex.fonk3('black')
        self.a4 += 1
        vertex.fonk6(self.a4)
if b8 = = "__main__":
    b9 = class3()
    b9.fonk19('A', 'B')
    b9.fonk19('A', 'C')
    b9.fonk19('B', 'D')
    b9.fonk19('B', 'E')
    b9.fonk19('C', 'F')
    b9.fonk19('C', 'G')
    b9.fonk23()
    for vertex in b9:
        print(f"class1 {vertex.fonk12()}: discovery a4 = {vertex.fonk10()}, finish a4 = {vertex.fonk11()}")