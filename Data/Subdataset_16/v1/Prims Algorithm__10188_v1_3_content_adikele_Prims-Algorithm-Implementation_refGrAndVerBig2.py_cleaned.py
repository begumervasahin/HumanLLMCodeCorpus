class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
    def fonk2(self, nbr, b3 = 0):
        self.b2[nbr] = b3
    def fonk3(self):
        return str(self.b1) + ' b2: ' + str([x.b1 for x in self.b2])
    def fonk4(self):
        return self.b2.keys()
    def fonk5(self):
        return self.b1
    def fonk6(self, nbr):
        return self.b2[nbr]
class class2:
    def fonk7(self):
        self.b4 = {}
        self.a1 = 0
    def fonk8(self, key):
        self.a1 = self.a1 + 1
        b5 = class1(key)
        self.b4[key] = b5
        return b5
    def fonk9(self, n):
        if n in self.b4:
            return self.b4[n]
        else:
            return None
    def fonk10(self, n):
        return n in self.b4
    def fonk11(self, f, t, b6 = 0):
        if f not in self.b4:
            self.fonk8(f)
        if t not in self.b4:
            self.fonk8(t)
        self.b4[f].fonk2(self.b4[t], b6)
    def fonk12(self):
        return self.b4.keys()
    def fonk13(self, a, b):
        if a not in self.b4 or b not in self.b4:
            return False
        for i in self.b4[a].b2.keys():
            if i.b1 = = b:
                b7 = self.b4[a].b2[i]
                if b7 < 6:
                    return True
        return False
    def fonk14(self):
        return iter(self.b4.values())
    def fonk15(self, a, b):
        if a not in self.b4 or b not in self.b4:
            return False
        for i in self.b4[a].b2.keys():
            if i.b1 = = b:
                return True
        return False
    def fonk16(self, a):
        if a not in self.b4:
            return False
        b8 = [self.b4[a].fonk18(i) for i in self.b4[a].b2.keys()]
        if b8:
            return min(b8)
        return None
    def fonk17(self, a):
        if a not in self.b4:
            return False
        b9 = float('inf')
        b10 = None
        for i in self.b4[a].b2.keys():
            b11 = self.b4[a].fonk18(i)
            if b11 < b9:
                b9 = b11
                b10 = i.b1
        return b10
    def fonk18(self, a, b):
        if a not in self.b4 or b not in self.b4:
            return False
        return self.b4[a].fonk18(self.b4[b])
if b12 = = "__main__":
    b13 = class2()
    b13.fonk8(1)
    b13.fonk8(2)
    b13.fonk8(3)
    b13.fonk11(1, 2, 5)
    b13.fonk11(1, 3, 3)
    print(b13.fonk16(1))
    print(b13.fonk17(1))
    print(b13.fonk18(1, 3))
    print(b13.fonk15(1, 3))
    print(b13.fonk13(1, 2))
