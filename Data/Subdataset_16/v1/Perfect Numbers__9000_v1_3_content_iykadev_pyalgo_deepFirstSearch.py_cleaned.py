class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
        self.b3 = 'white'
        self.b4 = None
        self.a1 = 0
        self.a2 = 0
    def fonk2(self, nbr, b5 = 0):
        self.b2[nbr] = b5
    def fonk3(self, b3):
        self.b3 = b3
    def fonk4(self, p):
        self.b4 = p
    def fonk5(self, dtime):
        self.a1 = dtime
    def fonk6(self, ftime):
        self.a2 = ftime
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
    def fonk13(self, nbr):
        return self.b2[nbr]
    def fonk14(self):
        return str(self.b1) + ' b2: ' + str([x.b1 for x in self.b2])
class class2:
    def fonk15(self):
        self.b6 = {}
        self.a3 = 0
    def fonk16(self, key):
        self.a3 = self.a3 + 1
        b7 = class1(key)
        self.b6[key] = b7
        return b7
    def fonk17(self, n):
        if n in self.b6:
            return self.b6[n]
        else:
            return None
    def fonk18(self, n):
        return n in self.b6
    def fonk19(self, f, t, b8 = 0):
        if f not in self.b6:
            b9 = self.fonk16(f)
        if t not in self.b6:
            b9 = self.fonk16(t)
        self.b6[f].fonk2(self.b6[t], b8)
    def fonk20(self):
        return self.b6.keys()
    def fonk21(self):
        return iter(self.b6.values())
class class3(class2):
    def fonk22(self):
        super().fonk22()
        self.a4 = 0
    def fonk23(self):
        for aVertex in self:
            aVertex.fonk3('white')
            aVertex.fonk4(-1)
        for aVertex in self:
            if aVertex.fonk8() == 'white':
                self.fonk24(aVertex)
    def fonk24(self, startVertex):
        startVertex.fonk3('gray')
        self.a4 += 1
        startVertex.fonk5(self.a4)
        for nextVertex in startVertex.fonk7():
            if nextVertex.fonk8() == 'white':
                nextVertex.fonk4(startVertex)
                self.fonk24(nextVertex)
        startVertex.fonk3('black')
        self.a4 += 1
        startVertex.fonk6(self.a4)
if b10 = = "__main__":
    b11 = class3()
    b11.fonk19('A', 'B')
    b11.fonk19('A', 'C')
    b11.fonk19('B', 'D')
    b11.fonk19('B', 'E')
    b11.fonk19('C', 'F')
    b11.fonk19('C', 'G')
    b11.fonk23()
    for vertex in b11:
        print(f"class1 {vertex.fonk12()}: discovery a4 = {vertex.fonk10()}, finish a4 = {vertex.fonk11()}")