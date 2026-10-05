class class1:
    def fonk1(self):
        self.b1 = []
        self.a1 = 0
    def fonk2(self, i):
        b2 = 2 * i + 1
        return b2 if b2 < self.a1 else None
    def fonk3(self, i):
        b3 = 2 * i + 2
        return b3 if b3 < self.a1 else None
    def fonk4(self, i):
        b4 = i
        b2 = self.fonk2(i)
        b3 = self.fonk3(i)
        if b2 is not None and self.b1[b2] > self.b1[b4]:
            b4 = b2
        if b3 is not None and self.b1[b3] > self.b1[b4]:
            b4 = b3
        if b4 != i:
            self.b1[i], self.b1[b4] = self.b1[b4], self.b1[i]
            self.fonk4(b4)
    def fonk5(self, array):
        self.b1 = list(array)
        self.a1 = len(array)
        for i in range(self.a1
            self.fonk4(i)
    def fonk6(self):
        for i in range(self.a1 - 1, 0, -1):
            self.b1[0], self.b1[i] = self.b1[i], self.b1[0]
            self.a1 -= 1
            self.fonk4(0)
        self.a1 = len(self.b1)
    def fonk7(self, data):
        self.b1.append(data)
        self.a1 += 1
        b5 = self.a1 - 1
        while b5 > 0 and self.b1[b5] > self.b1[b5
            self.b1[b5], self.b1[b5
            b5
    def fonk8(self):
        print(self.b1)
def fonk9():
    print("=== Max b6 = ==")
    b7 = input("[STR] Enter your b7: ").split()
    b1 = class1()
    b1.fonk5(b7)
    b1.fonk6()
    b1.fonk8()
if b8 = = '__main__':
    fonk9()