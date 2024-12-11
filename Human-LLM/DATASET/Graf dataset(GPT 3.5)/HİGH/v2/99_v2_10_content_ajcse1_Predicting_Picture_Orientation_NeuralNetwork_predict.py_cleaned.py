import time
import math
import random
def fonk1(I, J, b1 = 0.0):
    b2 = []
    for i in range(I):
        b2.append([b1] * J)
    return b2
class class1:
    def fonk2(self, ni, nh, no, lr):
        self.b3 = int(ni)
        self.b4 = int(nh)
        self.b5 = int(no)
        self.b6 = float(lr)
        self.b7 = [1.0] * self.b3
        self.b8 = [1.0] * self.b4
        self.b9 = [1.0] * self.b5
        self.b10 = fonk1(self.b3, self.b4)
        self.b11 = fonk1(self.b4, self.b5)
        self.a1 = 1.0
        for i in range(self.b3):
            for j in range(self.b4):
                self.b10[i][j] = random.uniform(0, 1)
        for j in range(self.b4):
            for a5 in range(self.b5):
                self.b11[j][a5] = random.uniform(0, 1)
    def fonk3(self, b22):
        for i in range(self.b3):
            self.b7[i] = float(b22[i]) / float(255)
        for j in range(self.b4):
            a2 = 0.0
            for i in range(self.b3):
                a2 += (self.b7[i] * self.b10[i][j])
            a2 += self.a1
            self.b8[j] = a2
        b12 = max(self.b8)
        b13 = min(self.b8)
        for i in range(self.b4):
            self.b8[i] = (self.b8[i] - b13) / (b12 - b13)
            self.b8[i] = 1 / (1 + math.exp(-self.b8[i]))
        for a5 in range(self.b5):
            a2 = 0.0
            for j in range(self.b4):
                a2 += (self.b8[j] * self.b11[j][a5])
            self.b9[a5] = a2 + self.a1
        b12 = max(self.b9)
        for i in range(self.b5):
            self.b9[i] = self.b9[i] / b12
            self.b9[i] = 1 / (1 + math.exp(-self.b9[i]))
        return self.b9.index(b12) * 90
    def fonk4(self, b21, b6):
        b14 = [0.0] * self.b5
        for a5 in range(self.b5):
            b15 = b21[a5] - self.b9[a5]
            b14[a5] = b15 * self.b9[a5] * (1 - self.b9[a5])
        for j in range(self.b4):
            for a5 in range(self.b5):
                b16 = b14[a5] * self.b8[j]
                self.b11[j][a5] += b6 * b16
        b17 = [0.0] * self.b4
        for j in range(self.b4):
            b15 = 0.0
            for a5 in range(self.b5):
                b15 += b14[a5] * self.b11[j][a5]
            b17[j] = b15 * self.b8[j] * (1 - self.b8[j])
        for i in range(self.b3):
            for j in range(self.b4):
                b16 = b17[j] * self.b7[i]
                self.b10[i][j] += b6 * b16
    def fonk5(self, patterns, b19):
        b12 = self.fonk3(patterns)
        if b12 = = b19:
            return b19
        else:
            return -1
    def fonk6(self, b34):
        for i in range(len(b34)
            b18 = list(map(int, b34[i][2:]))
            b19 = int(b34[i][1])
            b20 = [b18, [b19]]
            b21 = [0] * 4
            b22 = b20[0]
            b21[b19
            self.fonk3(b22)
            self.fonk4(b21, self.b6)
    def fonk7(self, b35):
        a3 = 0
        b23 = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as fl:
            for i in range(len(b35)):
                b18 = list(map(int, b35[i][2:]))
                b19 = int(b35[i][1])
                b20 = [b18, [b19]]
                b22 = b20[0]
                b12 = self.fonk5(b22, b19)
                b23[b19
                b24 = b35[i][0] + " " + b35[i][1] + "\n"
                fl.write(b24)
                if b12 = = b19:
                    a3 += 1
        b25 = float(a3) / float(len(b35)) * 100
        print("Percentage of Accuracy:", b25)
        print("Confusion Matrix:")
        for row in b23:
            print(row)
    def fonk8(self, b34, b35, a5):
        b26 = [float('inf') for _ in range(int(a5))]
        b27 = [None] * int(a5)
        b28 = list(b35[2:])
        for j in range(len(b34)
            a4 = 0
            b29 = list(b34[j][2:])
            for a5 in range(192):
                a4 += abs(float(b28[a5]) - float(b29[a5]))
            b12 = max(b26)
            if a4 < b12:
                b30 = b26.index(b12)
                b26[b30] = float(a4)
                b27[b30] = j
        b31 = []
        for kindl in range(len(b27)):
            b31.append(b34[b27[kindl]][1])
        b32 = {}
        for word in b31:
            if word in b32:
                b32[word] += 1
            else:
                b32[word] = 1
        return max(b32, b33 = b32.get)
    def fonk9(self, b34, b35, a5):
        a3 = 0
        b23 = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as fl:
            for i in range(len(b35)):
                b12 = list(b35[i])
                b24 = self.fonk8(b34, b12, a5)
                if b24 = = b12[1]:
                    a3 += 1
                b23[int(b12[1])
                b24 = b12[0] + " " + b24 + "\n"
                fl.write(b24)
        b25 = float(a3) / float(len(b35)) * 100
        print("Percentage of Accuracy:", b25)
        print("Confusion Matrix:")
        for row in b23:
            print(row)
def fonk10():
    b20 = class1(192, 100, 4, 0.1)
    b34 = [[random.randint(0, 255) for _ in range(194)] for _ in range(100)]
    b35 = [[random.randint(0, 255) for _ in range(194)] for _ in range(20)]
    b20.fonk6(b34)
    b20.fonk7(b35)
    a5 = 5
    b20.fonk9(b34, b35, a5)
if b36 = = "__main__":
    fonk10()