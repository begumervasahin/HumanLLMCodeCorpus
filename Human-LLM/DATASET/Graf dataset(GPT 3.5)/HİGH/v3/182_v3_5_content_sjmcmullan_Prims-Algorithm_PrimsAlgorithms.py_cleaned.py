import sys
class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
        self.b3 = sys.maxsize
        self.b4 = None
    def fonk2(self, neighbor, b5 = 0):
        self.b2[neighbor] = b5
    def fonk3(self):
        return self.b2.keys()
    def fonk4(self):
        return self.b1
    def fonk5(self, neighbor):
        return self.b2[neighbor]
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
        for item in alist:
            self.b6.append(item)
        b7 = len(alist)
        while b7 > 0:
            self.fonk12(b7)
            b7 -= 1
    def fonk12(self, b9):
        while (b9 * 2) <= self.a1:
            b8 = self.fonk13(b9)
            if self.b6[b9][0] > self.b6[b8][0]:
                self.fonk19(b9, b8)
            b9 = b8
    def fonk13(self, b9):
        if b9 * 2 + 1 > self.a1:
            return b9 * 2
        else:
            if self.b6[b9 * 2][0] < self.b6[b9 * 2 + 1][0]:
                return b9 * 2
            else:
                return b9 * 2 + 1
    def fonk14(self, item):
        self.b6.append(item)
        self.a1 += 1
        self.fonk15(self.a1)
    def fonk15(self, b9):
        while b9
            if self.b6[b9][0] < self.b6[b9
                self.fonk19(b9, b9
            b9
    def fonk16(self):
        b10 = self.b6[1]
        self.b6[1] = self.b6[self.a1]
        self.a1 -= 1
        self.b6.pop()
        self.fonk12(1)
        return b10
    def fonk17(self):
        return self.a1 = = 0
    def fonk18(self, vertex, new_dist):
        for b9 in range(1, len(self.b6)):
            if self.b6[b9][1] == vertex:
                self.b6[b9] = (new_dist, vertex)
                self.fonk15(b9)
                break
    def fonk19(self, b9, j):
        self.b6[b9], self.b6[j] = self.b6[j], self.b6[b9]
def fonk20(G, start):
    b11 = class2()
    for v in G:
        v.fonk6(sys.maxsize)
        v.fonk8(None)
    start.fonk6(0)
    b11.fonk11([(v.fonk7(), v) for v in G])
    while not b11.fonk17():
        b12 = b11.fonk16()
        for next_vert in b12[1].fonk3():
            b13 = b12[1].fonk5(next_vert)
            if b13 < next_vert.fonk7():
                next_vert.fonk8(b12[1])
                next_vert.fonk6(b13)
                b11.fonk18(next_vert, b13)
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
fonk20(b19, b14)
for vertex in b19:
    print("class1:", vertex.fonk4())
    print("Distance:", vertex.fonk7())
    if vertex.fonk9():
        print("Predecessor:", vertex.fonk9().fonk4())
    else:
        print("Predecessor: None")
    print()