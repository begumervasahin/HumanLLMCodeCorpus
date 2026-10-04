class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
    def fonk2(self, nbr, b3 = 0):
        self.b2[nbr] = b3
    def fonk3(self):
        return f"{self.b1} b2: {[x.b1 for x in self.b2]}"
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
        self.a1 += 1
        b5 = class1(key)
        self.b4[key] = b5
        return b5
    def fonk9(self, n):
        return self.b4.get(n)
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
        return any(neighbor.b1 = = b and self.b4[a].fonk6(neighbor) < 6 for neighbor in self.b4[a].fonk4())
    def fonk14(self):
        return iter(self.b4.values())
    def fonk15(self, a, b):
        if a not in self.b4 or b not in self.b4:
            return False
        return any(neighbor.b1 = = b for neighbor in self.b4[a].fonk4())
    def fonk16(self, a):
        if a not in self.b4:
            return False
        return min(self.b4[a].fonk6(neighbor) for neighbor in self.b4[a].fonk4())
    def fonk17(self, a):
        if a not in self.b4:
            return False
        b7 = float('inf')
        b8 = None
        for neighbor in self.b4[a].fonk4():
            b6 = self.b4[a].fonk6(neighbor)
            if b6 < b7:
                b7 = b6
                b8 = neighbor.b1
        return b8
    def fonk18(self, a, b):
        if a not in self.b4 or b not in self.b4:
            return False
        return self.b4[a].fonk6(self.b4[b])