import random
import math
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        print(f"edge:({self.b1}--{self.b2}) with b3 {self.b3}")
class class2:
    def fonk3(self, b5, b6):
        self.b4 = [[] for _ in range(len(b5))]
        self.b5 = b5
        self.b6 = b6
        for edge in b6:
            self.b4[edge.b1].append((edge.b2, edge.b3))
            self.b4[edge.b2].append((edge.b1, edge.b3))
    def fonk4(self, edge):
        self.b6.append(edge)
        self.b4[edge.b1].append((edge.b2, edge.b3))
        self.b4[edge.b2].append((edge.b1, edge.b3))
    def fonk5(self):
        for node, b6 in enumerate(self.b4):
            b7 = " ".join(f"({b2}:{w:.2f})" for b2, w in b6)
            print(f"{node}: {b7}")
    def fonk6(self, b1, index):
        return self.b4[b1][index]
    def fonk7(self, b1):
        return len(self.b4[b1])
    def fonk8(self):
        return len(self.b5)
    def fonk9(self):
        return self.b6
    def fonk10(self):
        return self.b5
class class3:
    def fonk11(self, b9, b10, b8 = 1, b11=30, b12=100, b13=100, seed=3141):
        self.b9 = b9
        self.b10 = b10
        self.b8 = b8
        self.b11 = b11
        self.b12 = b12
        self.b13 = b13
        random.seed(seed)
    def fonk12(self):
        if self.b8 = = 1:
            return self.fonk13()
        elif self.b8 = = 2:
            return self.fonk14()
        else:
            print("Method not defined")
            return class2([], [])
    def fonk13(self):
        b5 = list(range(self.b9))
        b6 = []
        for i in range(self.b9):
            for j in range(i + 1, self.b9):
                if random.randint(1, 10000) <= self.b10 * 10000:
                    b3 = random.randint(1, self.b11 + 1)
                    b6.append(class1(i, j, b3))
        return class2(b5, b6)
    def fonk14(self):
        b5 = list(range(self.b9))
        b14 = [(random.randint(1, self.b12 + 1), random.randint(1, self.b13 + 1)) for _ in range(self.b9)]
        b6 = []
        for i in range(self.b9):
            for j in range(i + 1, self.b9):
                if random.randint(1, 10000) <= self.b10 * 10000:
                    b3 = math.sqrt((b14[i][0] - b14[j][0]) ** 2 + (b14[i][1] - b14[j][1]) ** 2)
                    b6.append(class1(i, j, b3))
        return class2(b5, b6)
