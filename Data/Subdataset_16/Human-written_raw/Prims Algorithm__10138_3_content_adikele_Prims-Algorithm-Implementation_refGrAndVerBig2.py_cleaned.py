class class1:
    def fonk1(self,key):
        self.b1 = key
        self.b2 = {}
    def fonk2(self,nbr,b3 = 0):
        self.b2[nbr] = b3
    def fonk3(self):
        return str(self.b1) + ' b2: ' + str([x.b1 for x in self.b2])
    def fonk4(self):
        return self.b2.keys()
    def fonk5(self):
        return self.b1
    def fonk6(self,nbrMalegaon):
        return self.b2[nbrMalegaon]
class class2:
    def fonk7(self):
        self.b4 = {}
        self.a1 = 0
    def fonk8(self,key):
        self.a1 = self.a1 + 1
        b5 = class1(key)
        self.b4[key] = b5
        return b5
    def fonk9(self,n):
        if n in self.b4:
            return self.b4[n]
        else:
            return None
    def fonk10(self,n):
        return n in self.b4
    def fonk11(self,f,t,b6 = 0):
        if f not in self.b4:
            b7 = self.fonk8(f)
        if t not in self.b4:
            b7 = self.fonk8(t)
        self.b4[f].fonk2(self.b4[t], b6)
    def fonk12(self):
        return self.b4.keys()
    def NeighboursJoo (self, a, b):
        if a not in self.b4:
            return false
        if b not in self.b4:
            return false
        for i in self.b4[a].b2.keys():
            if i.b1 = = b:
                b8 = self.b4[a].b2[i]
                if b8 < 6:
                    return True
    def fonk13(self):
        return iter(self.b4.values())
    def fonk14(self, a, b):
        if a not in self.b4:
            return false
        if b not in self.b4:
            return false
        for i in self.b4[a].b2.keys():
            if i.b1 = = b:
                return True
    def fonk15(self, a):
        if a not in self.b4:
             return false
        b9 = []
        for i in self.b4[a].b2.keys():
             b10 = self.b4[a].fonk17(i)
             b9.append(b10)
        b11 = min (b9)
        return b11
    def fonk16(self, a):
        if a not in self.b4:
             return false
        b9 = []
        for i in self.b4[a].b2.keys():
             b10 = self.b4[a].fonk17(i)
             b9.append(b10)
             if min (b9) == b10:
                 b12 = i.b1
        b11 = b12
        return b11
    def fonk17(self, a, b):
        if a not in self.b4:
             return false
        if b not in self.b4:
             return false
        b6 = self.b4[a].b2[self.b4[b]]
        return b6