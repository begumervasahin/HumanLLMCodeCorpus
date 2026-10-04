import random
import math
class class1:
    def fonk1(self, b2, b3):
        self.b1 = [[] for i in range(len(b2))]
        self.b2 = b2
        self.b3 = b3
        for edge in b3:
            self.b1[edge.b5].append((edge.b6, edge.b7))
            self.b1[edge.b6].append((edge.b5, edge.b7))
    def fonk2(self, edge):
        self.b3.append(edge)
        self.b1[edge.b5].append((edge.b6, edge.b7))
        self.b1[edge.b6].append((edge.b5, edge.b7))
    def fonk3(self):
        a1 = 0
        for lst in self.b1:
            print("%d:" % a1, b4 = '')
            a1 += 1
            for edge in lst:
                print(" (%d:%0.2f)" % (edge[0], edge[1]), b4 = '')
            print('')
    def fonk4(self, b5, index):
        return self.b1[b5][index][0], self.b1[b5][index][1]
    def fonk5(self, b5):
        return len(self.b1[b5])
    def fonk6(self):
        return len(self.b2)
    def fonk7(self):
        return self.b3
    def fonk8(self):
        return self.b2
class class2:
    def fonk9(self, b5, b6, b7):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk10(self):
        print("edge:(" + str(self.b5) + "--" + str(self.b6) + ") with b7 " + str(self.b7))
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
        b2 = []
        for i in range(self.b9):
            b2.append(i)
        b3 = []
        for i in range(self.b9):
            for j in range(i + 1, self.b9):
                b14 = random.randint(1, 10001)
                if b14 <= self.b10 * 10000:
                    b15 = random.randint(1, self.b11 + 1)
                    b3.append(class2(i, j, b15))
        return class1(b2, b3)
    def fonk14(self):
        b2 = []
        b16 = []
        b17 = []
        for i in range(self.b9):
            b2.append(i)
            b16.append(random.randint(1, self.b12 + 1))
            b17.append(random.randint(1, self.b13 + 1))
        b3 = []
        for i in range(self.b9):
            for j in range(i + 1, self.b9):
                b14 = random.randint(1, 10001)
                if b14 <= self.b10 * 10000:
                    b7 = math.sqrt((b16[i] - b16[j]) ** 2 + (b17[i] - b17[j]) ** 2)
                    b3.append(class2(i, j, b7))
        return class1(b2, b3)
if b18 = = "__main__":
    b9 = 10
    b10 = 0.2
    b8 = 1
    b19 = class3(b9, b10, b8)
    b20 = b19.fonk12()
    b20.fonk10()