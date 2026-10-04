class class1:
    def fonk1(self):
        self.b1 = [(0, 0)]
        self.a1 = 0
    def fonk2(self):
        return self.a1
    def fonk3(self):
        if self.a1 != 0:
            return self.b1[1]
    def fonk4(self):
        b2 = self.fonk3()
        self.b1[1] = self.b1[self.a1]
        self.a1 -= 1
        self.b1.pop()
        self.fonk8(1)
        return b2
    def fonk5(self, elemento):
        self.b1.append(elemento)
        self.a1 += 1
        self.fonk10(self.a1)
    def fonk6(self, b3, valor):
        a2 = 0
        for b6 in self.b1:
            if b3 = = b6[1]:
                self.b1[a2] = (valor, b3)
                self.fonk10(a2)
                break
            a2 += 1
    def fonk7(self, elemento):
        for b4 in self.b1:
            if b4 = = elemento:
                return True
        return False
    def fonk8(self, b6):
        while 2 * b6 <= self.a1:
            b5 = 2 * b6
            if b5 < self.a1 and self.b1[b5][0] > self.b1[b5 + 1][0]:
                b5 += 1
            if self.b1[b6][0] <= self.b1[b5][0]:
                break
            else:
                self.b1[b6], self.b1[b5] = self.b1[b5], self.b1[b6]
                b6 = b5
    def fonk9(self, lista):
        self.b1 = [(0, 0)]
        self.a1 = len(lista)
        self.b1.extend(lista)
        b6 = len(lista)
        while b6 >= 1:
            self.fonk8(b6)
            b6 -= 1
    def fonk10(self, b6):
        while b6 >= 2 and self.b1[b6
            self.b1[b6
            b6