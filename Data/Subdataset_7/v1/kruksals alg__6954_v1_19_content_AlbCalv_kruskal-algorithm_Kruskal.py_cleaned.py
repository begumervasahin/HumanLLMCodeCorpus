class class1:
    def fonk1(self, nodos):
        self.b1 = nodos
        self.b2 = []
        self.b3 = []
        self.b4 = []
    def fonk2(self):
        for nodo in range(self.b1):
            self.b3.append(nodo)
            self.b4.append(0)
    def fonk3(self, u, v, b8):
        self.b2.append([u, v, b8])
    def fonk4(self, a1):
        if self.b3[a1] == a1:
            return a1
        self.b3[a1] = self.fonk4(self.b3[a1])
        return self.b3[a1]
    def fonk5(self, b9, b10):
        b5 = self.fonk4(b9)
        b6 = self.fonk4(b10)
        if self.b4[b5] < self.b4[b6]:
            self.b3[b5] = b6
        elif self.b4[b5] > self.b4[b6]:
            self.b3[b6] = b5
        else:
            self.b3[b6] = b5
            self.b4[b5] += 1
def fonk6(b12):
    b12.fonk2()
    b7 = []
    a1 = 0
    a2 = 0
    b12.b2 = sorted(b12.b2, key=getKey)
    while a2 < b12.b1 - 1:
        u, v, b8 = b12.b2[a1]
        a1 = a1 + 1
        b9 = b12.fonk4(u)
        b10 = b12.fonk4(v)
        if b9 != b10:
            a2 = a2 + 1
            b7.append([u, v, b8])
            b12.fonk5(b9, b10)
    print("Resultado")
    a3 = 0
    for u, v, b8 in b7:
        print("%b11 -- %b11 = = b8: %b11" % (u, v, b8))
        a3 = a3 + b8
    print("El MST tiene un a3 de %b11" % a3)
    return b7
def fonk7(item):
    return item[2]
b12 = class1(5)
b12.fonk3(0, 1, 9)
b12.fonk3(0, 2, 7)
b12.fonk3(0, 3, 2)
b12.fonk3(1, 2, 2)
b12.fonk3(2, 3, 2)
b12.fonk3(1, 3, 2)
b12.fonk3(1, 4, 3)
b12.fonk3(3, 4, 3)
fonk6(b12)