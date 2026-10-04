import random
import math
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = [[] for _ in b1]
        for edge in b2:
            self.b3[edge.b5].append((edge.b6, edge.b7))
            self.b3[edge.b6].append((edge.b5, edge.b7))
    def fonk2(self, edge):
        self.b2.append(edge)
        self.b3[edge.b5].append((edge.b6, edge.b7))
        self.b3[edge.b6].append((edge.b5, edge.b7))
    def fonk3(self):
        for node, neighbors in enumerate(self.b3):
            print(f"{node}:", b4 = '')
            for neighbor in neighbors:
                print(f" ({neighbor[0]}:{neighbor[1]:0.2f})", b4 = '')
            print('')
    def fonk4(self, b5, index):
        return self.b3[b5][index]
    def fonk5(self, b5):
        return len(self.b3[b5])
    def fonk6(self):
        return len(self.b1)
    def fonk7(self):
        return self.b2
    def fonk8(self):
        return self.b1
class class2:
    def fonk9(self, b5, b6, b7):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk10(self):
        print(f"edge:({self.b5}--{self.b6}) with b7 {self.b7}")
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
            return class1([], [])
    def fonk13(self):
        b1 = list(range(self.b9))
        b2 = []
        for i in range(self.b9):
            for j in range(i + 1, self.b9):
                if random.randint(1, 10001) <= self.b10 * 10000:
                    b7 = random.randint(1, self.b11 + 1)
                    b2.append(class2(i, j, b7))
        return class1(b1, b2)
    def fonk14(self):
        b1 = list(range(self.b9))
        b14 = [(random.randint(1, self.b12 + 1), random.randint(1, self.b13 + 1)) for _ in range(self.b9)]
        b2 = []
        for i in range(self.b9):
            for j in range(i + 1, self.b9):
                if random.randint(1, 10001) <= self.b10 * 10000:
                    x1, b15 = b14[i]
                    x2, b16 = b14[j]
                    b7 = math.sqrt((x1 - x2) ** 2 + (b15 - b16) ** 2)
                    b2.append(class2(i, j, b7))
        return class1(b1, b2)
if b17 = = "__main__":
    b9 = 10
    b10 = 0.2
    b8 = 1
    b18 = class3(b9, b10, b8)
    b19 = b18.fonk12()
    b19.fonk3()