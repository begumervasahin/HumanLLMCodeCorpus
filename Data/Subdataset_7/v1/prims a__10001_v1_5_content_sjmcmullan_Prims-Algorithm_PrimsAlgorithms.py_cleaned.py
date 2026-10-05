import sys
class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
        self.b3 = sys.maxsize
        self.b4 = None
    def fonk2(self, nbr, b5 = 0):
        self.b2[nbr] = b5
    def fonk3(self):
        return self.b2.keys()
    def fonk4(self):
        return self.b1
    def fonk5(self, nbr):
        return self.b2[nbr]
    def fonk6(self, dist):
        self.b3 = dist
    def fonk7(self):
        return self.b3
    def fonk8(self, b4):
        self.b4 = b4
    def fonk9(self):
        return self.b4
class class2:
    def fonk10(self):
        self.b6 = [(0, None)]
        self.a1 = 0
    def fonk11(self, alist):
        self.a1 = len(alist)
        self.b6 = [(0, None)]
        for b7 in alist:
            self.b6.append(b7)
        b7 = len(alist)
        while b7 > 0:
            self.fonk12(b7)
            b7 = b7 - 1
    def fonk12(self, b7):
        while (b7 * 2) <= self.a1:
            b8 = self.fonk13(b7)
            if self.b6[b7][0] > self.b6[b8][0]:
                b9 = self.b6[b7]
                self.b6[b7] = self.b6[b8]
                self.b6[b8] = b9
            b7 = b8
    def fonk13(self, b7):
        if b7 * 2 + 1 > self.a1:
            return b7 * 2
        else:
            if self.b6[b7 * 2][0] < self.b6[b7 * 2 + 1][0]:
                return b7 * 2
            else:
                return b7 * 2 + 1
    def fonk14(self, k):
        self.b6.append(k)
        self.a1 = self.a1 + 1
        self.fonk15(self.a1)
    def fonk15(self, b7):
        while b7
            if self.b6[b7][0] < self.b6[b7
                b9 = self.b6[b7
                self.b6[b7
                self.b6[b7] = b9
            b7 = b7
    def fonk16(self):
        b10 = self.b6[1]
        self.b6[1] = self.b6[self.a1]
        self.a1 = self.a1 - 1
        self.b6.pop()
        self.fonk12(1)
        return b10
    def fonk17(self):
        return self.a1 = = 0
    def fonk18(self, vertex, newDist):
        for b7 in range(1, len(self.b6)):
            if self.b6[b7][1] == vertex:
                self.b6[b7] = (newDist, vertex)
                self.fonk15(b7)
                break
def fonk19(G, start):
    b11 = class2()
    for v in G:
        v.fonk6(sys.maxsize)
        v.fonk8(None)
    start.fonk6(0)
    b11.fonk11([(v.fonk7(), v) for v in G])
    while not b11.fonk17():
        b12 = b11.fonk16()
        for nextVert in b12[1].fonk3():
            b13 = b12[1].fonk5(nextVert)
            if b13 < nextVert.fonk7():
                nextVert.fonk8(b12[1])
                nextVert.fonk6(b13)
                b11.fonk18(nextVert, b13)
b14 = class1('A')
b15 = class1('B')
b16 = class1('C')
b17 = class1('D')
b18 = class1('E')
b14.fonk2(b15, 2)
b14.fonk2(b16, 3)
b15.fonk2(b16, 1)
b15.fonk2(b17, 1)
b16.fonk2(b17, 2)
b16.fonk2(b18, 1)
b17.fonk2(b18, 3)
b19 = [b14, b15, b16, b17, b18]
fonk19(b19, b14)
for vertex in b19:
    print("class1:", vertex.fonk4())
    print("Distance:", vertex.fonk7())
    if vertex.fonk9():
        print("Predecessor:", vertex.fonk9().fonk4())
    else:
        print("Predecessor: None")
    print()