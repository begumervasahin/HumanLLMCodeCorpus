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
    def fonk4(self, node):
        if node < self.a1:
            b4 = node
            b2 = self.fonk2(node)
            b3 = self.fonk3(node)
            if b2 is not None and self.b1[b2] > self.b1[b4]:
                b4 = b2
            if b3 is not None and self.b1[b3] > self.b1[b4]:
                b4 = b3
            if b4 != node:
                self.b1[node], self.b1[b4] = self.b1[b4], self.b1[node]
                self.fonk4(b4)
    def fonk5(self, a):
        self.a1 = len(a)
        self.b1 = list(a)
        for i in range(self.a1
            self.fonk4(i)
    def fonk6(self):
        if self.a1 >= 1:
            b5 = self.b1[0]
            self.b1[0], self.b1[self.a1 - 1] = self.b1[self.a1 - 1], self.b1[0]
            self.a1 -= 1
            self.fonk4(0)
            return b5
        return None
    def fonk7(self):
        b6 = self.a1
        while self.a1 > 1:
            self.b1[0], self.b1[self.a1 - 1] = self.b1[self.a1 - 1], self.b1[0]
            self.a1 -= 1
            self.fonk4(0)
        self.a1 = b6
    def fonk8(self, data):
        self.b1.append(data)
        self.a1 += 1
        b7 = self.a1 - 1
        b8 = (b7 - 1)
        while b7 > 0 and self.b1[b7] > self.b1[b8]:
            self.b1[b7], self.b1[b8] = self.b1[b8], self.b1[b7]
            b7 = b8
            b8 = (b7 - 1)
    def fonk9(self):
        print(self.b1)
def fonk10():
    print("=== class1 (max) - A specialized tree-based data structure that satisfies the max-heap property.")
    b9 = input("[STR] What is your b9? ").split()
    b1 = class1()
    b1.fonk5(b9)
    b1.fonk7()
    b1.fonk9()
if b10 = = '__main__':
    fonk10()