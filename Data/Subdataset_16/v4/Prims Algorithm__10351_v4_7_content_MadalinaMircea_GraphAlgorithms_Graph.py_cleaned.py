class class1:
    def fonk1(self, n):
        self.b1 = n
        self.a1 = 0
        self.b2 = {i: [] for i in range(n)}
    def fonk2(self, x):
        return x in self.b2
    def fonk3(self):
        return list(self.b2.keys())
    def fonk4(self, x):
        if self.fonk2(x):
            return self.b2[x]
        return False
    def fonk5(self, x, y):
        if self.fonk2(x):
            return y in self.b2[x]
        return False
    def fonk6(self, x, y):
        if not self.fonk5(x, y):
            self.b2[x].append(y)
            self.b2[y].append(x)
            self.a1 += 1
            return True
        return False
    def fonk7(self):
        return self.b1
    def fonk8(self):
        return self.a1
    def fonk9(self, x):
        if self.fonk2(x):
            return len(self.b2[x])
        return False