import random
import math
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"edge:({self.b1}--{self.b2}) with b3 {self.b3}"
class class2:
    def fonk3(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
        self.b6 = [[] for _ in range(len(b4))]
        for edge in b5:
            self.fonk4(edge)
    def fonk4(self, edge):
        self.b6[edge.b1].append((edge.b2, edge.b3))
        self.b6[edge.b2].append((edge.b1, edge.b3))
    def fonk5(self, edge):
        self.b5.append(edge)
        self.fonk4(edge)
    def fonk6(self):
        b7 = []
        for node, b5 in enumerate(self.b6):
            b8 = " ".join(f"({b2}:{w:.2f})" for b2, w in b5)
            b7.append(f"{node}: {b8}")
        return "\b10".join(b7)
    def fonk7(self, b1, index):
        return self.b6[b1][index]
    def fonk8(self, b1):
        return len(self.b6[b1])
    def fonk9(self):
        return len(self.b4)
    def fonk10(self):
        return self.b5
    def fonk11(self):
        return self.b4
class class3:
    def fonk12(self, b10, b11, b9 = 1, b12=30, b13=100, b14=100, seed=3141):
        self.b10 = b10
        self.b11 = b11
        self.b9 = b9
        self.b12 = b12
        self.b13 = b13
        self.b14 = b14
        random.seed(seed)
    def fonk13(self):
        if self.b9 = = 1:
            return self.fonk14()
        elif self.b9 = = 2:
            return self.fonk15()
        else:
            print("Method not defined")
            return class2([], [])
    def fonk14(self):
        b4 = list(range(self.b10))
        b5 = []
        for i in range(self.b10):
            for j in range(i + 1, self.b10):
                if random.randint(1, 10000) <= self.b11 * 10000:
                    b3 = random.randint(1, self.b12 + 1)
                    b5.append(class1(i, j, b3))
        return class2(b4, b5)
    def fonk15(self):
        b4 = list(range(self.b10))
        b15 = [(random.randint(1, self.b13 + 1), random.randint(1, self.b14 + 1)) for _ in range(self.b10)]
        b5 = []
        for i in range(self.b10):
            for j in range(i + 1, self.b10):
                if random.randint(1, 10000) <= self.b11 * 10000:
                    b3 = math.sqrt((b15[i][0] - b15[j][0]) ** 2 + (b15[i][1] - b15[j][1]) ** 2)
                    b5.append(class1(i, j, b3))
        return class2(b4, b5)
