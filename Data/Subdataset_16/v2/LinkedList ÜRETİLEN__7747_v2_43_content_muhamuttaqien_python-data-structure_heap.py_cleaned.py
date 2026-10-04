class b10:
    def fonk1(self):
        self.b1 = []
        self.a1 = 0
    def fonk2(self, index):
        b2 = 2 * index + 1
        return b2 if b2 < self.a1 else None
    def fonk3(self, index):
        b3 = 2 * index + 2
        return b3 if b3 < self.a1 else None
    def fonk4(self, index):
        b4 = index
        b5 = self.fonk2(index)
        b6 = self.fonk3(index)
        if b5 is not None and self.b1[b5] > self.b1[b4]:
            b4 = b5
        if b6 is not None and self.b1[b6] > self.b1[b4]:
            b4 = b6
        if b4 != index:
            self.b1[index], self.b1[b4] = self.b1[b4], self.b1[index]
            self.fonk4(b4)
    def fonk5(self, array):
        self.a1 = len(array)
        self.b1 = array[:]
        for i in range(self.a1
            self.fonk4(i)
    def fonk6(self):
        if self.a1 = = 0:
            return None
        b7 = self.b1[0]
        self.b1[0] = self.b1[self.a1 - 1]
        self.a1 -= 1
        self.fonk4(0)
        return b7
    def fonk7(self):
        b8 = self.a1
        for i in range(self.a1 - 1, 0, -1):
            self.b1[0], self.b1[i] = self.b1[i], self.b1[0]
            self.a1 -= 1
            self.fonk4(0)
        self.a1 = b8
    def fonk8(self, data):
        self.b1.append(data)
        self.a1 += 1
        b9 = self.a1 - 1
        while b9 > 0 and self.b1[b9] > self.b1[(b9 - 1)
            self.b1[b9], self.b1[(b9 - 1)
            b9 = (b9 - 1)
    def fonk9(self):
        print(self.b1)
def fonk10():
    print("=== b10 = ==")
    b11 = input("Enter a b11: ")
    b12 = b11.split()
    b1 = b10()
    b1.fonk5(b12)
    b1.fonk7()
    b1.fonk9()
if b13 = = '__main__':
    fonk10()