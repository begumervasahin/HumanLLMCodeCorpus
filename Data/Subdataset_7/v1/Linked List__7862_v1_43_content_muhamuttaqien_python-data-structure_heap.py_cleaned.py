class class1:
    def fonk1(self):
        self.b1 = []
        self.a1 = 0
    def fonk2(self, i):
        if 2*i + 1 < self.a1:
            return 2*i + 1
        return None
    def fonk3(self, i):
        if 2*i + 2 < self.a1:
            return 2*i + 2
        return None
    def fonk4(self, node):
        if node < self.a1:
            b2 = node
            b3 = self.fonk2(node)
            b4 = self.fonk3(node)
            if b3 is not None and self.b1[b3] > self.b1[b2]:
                b2 = b3
            if b4 is not None and self.b1[b4] > self.b1[b2]:
                b2 = b4
            if b2 != node:
                self.b1[node], self.b1[b2] = self.b1[b2], self.b1[node]
                self.fonk4(b2)
    def fonk5(self, a):
        self.a1 = len(a)
        self.b1 = list(a)
        for i in range(self.a1
            self.fonk4(i)
    def fonk6(self):
        if self.a1 >= 1:
            b5 = self.b1[0]
            self.b1[0], self.b1[self.a1-1] = self.b1[self.a1-1], self.b1[0]
            self.a1 -= 1
            self.fonk4(0)
            return b5
        return None
    def fonk7(self):
        b6 = self.a1
        while self.a1 - 1 >= 0:
            self.b1[0], self.b1[self.a1-1] = self.b1[self.a1-1], self.b1[0]
            self.a1 -= 1
            self.fonk4(0)
        self.a1 = b6
    def fonk8(self, data):
        self.b1.append(data)
        b7 = self.a1
        self.a1 += 1
        while b7 > 0 and self.b1[b7] > self.b1[(b7-1)
            self.b1[b7], self.b1[(b7-1)
            b7 = (b7-1)
    def fonk9(self):
        print(self.b1)
def fonk10():
    print("=== class1 (max) - A specialized tree-based data structure that satisfies the heap property (max-min) which is in max heap, the keys of parent nodes are always greater than or equal to those of the children and the highest key is in the root node")
    b8 = input("[STR] What is your b8? ").split()
    b1 = class1()
    b1.fonk5(b8)
    b1.fonk7()
    b1.fonk9()
if b9 = = '__main__':
    fonk10()