class class1:
    def fonk1(self):
        self.b1 = []
        self.a1 = 0
    def fonk2(self, i):
        b2 = 2 * i + 1
        if b2 < self.a1:
            return b2
        return None
    def fonk3(self, i):
        b3 = 2 * i + 2
        if b3 < self.a1:
            return b3
        return None
    def fonk4(self, i):
        b4 = i
        b5 = self.fonk2(i)
        b6 = self.fonk3(i)
        if b5 is not None and self.b1[b5] > self.b1[b4]:
            b4 = b5
        if b6 is not None and self.b1[b6] > self.b1[b4]:
            b4 = b6
        if b4 != i:
            self.b1[i], self.b1[b4] = self.b1[b4], self.b1[i]
            self.fonk4(b4)
    def fonk5(self, array):
        self.a1 = len(array)
        self.b1 = list(array)
        for i in range(self.a1
            self.fonk4(i)
    def fonk6(self):
        if self.a1 >= 1:
            b7 = self.b1[0]
            self.b1[0], self.b1[self.a1 - 1] = self.b1[self.a1 - 1], self.b1[0]
            self.a1 -= 1
            self.fonk4(0)
            return b7
        return None
    def fonk7(self):
        b8 = self.a1
        while self.a1 - 1 >= 0:
            self.b1[0], self.b1[self.a1 - 1] = self.b1[self.a1 - 1], self.b1[0]
            self.a1 -= 1
            self.fonk4(0)
        self.a1 = b8
    def fonk8(self, data):
        self.b1.append(data)
        b9 = self.a1
        self.a1 += 1
        while b9 > 0 and self.b1[b9] > self.b1[(b9 - 1)
            self.b1[b9], self.b1[(b9 - 1)
            b9 = (b9 - 1)
    def fonk9(self):
        print(self.b1)
def fonk10():
    print("=== class1 (max) - A specialized tree-based data structure that satisfies the b11 property (max-min) which is in max b11, the keys of parent nodes are always greater than or equal to those of the children and the highest key is in the root node")
    b10 = input("[STR] What is your b10? ").split()
    b11 = class1()
    b11.fonk5(b10)
    b11.fonk7()
    b11.fonk9()
if b12 = = '__main__':
    fonk10()