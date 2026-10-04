import time
import math
import random
def fonk1(I, J, b1 = 0.0):
    return [[b1]*J for _ in range(I)]
class class1:
    def fonk2(self, ni, nh, no, b36):
        self.b2 = int(ni)
        self.b3 = int(nh)
        self.b4 = int(no)
        self.b5 = float(b36)
        self.b6 = [1.0] * self.b2
        self.b7 = [1.0] * self.b3
        self.b8 = [1.0] * self.b4
        self.b9 = fonk1(self.b2, self.b3)
        self.b10 = fonk1(self.b3, self.b4)
        self.a1 = 1.0
        for i in range(self.b2):
            for j in range(self.b3):
                self.b9[i][j] = random.uniform(0, 1)
        for j in range(self.b3):
            for k in range(self.b4):
                self.b10[j][k] = random.uniform(0, 1)
    def fonk3(self, b20):
        for i in range(self.b2):
            self.b6[i] = float(b20[i]) / 255.0
        for j in range(self.b3):
            a2 = 0.0
            for i in range(self.b2):
                a2 += self.b6[i] * self.b9[i][j]
            a2 += self.a1
            self.b7[j] = a2
        b11 = max(self.b7)
        b12 = min(self.b7)
        for i in range(self.b3):
            self.b7[i] = (self.b7[i] - b12) / (b11 - b12)
            self.b7[i] = 1 / (1 + math.exp(-self.b7[i]))
        for k in range(self.b4):
            a2 = 0.0
            for j in range(self.b3):
                a2 += self.b7[j] * self.b10[j][k]
            self.b8[k] = a2 + self.a1
        b11 = max(self.b8)
        b12 = min(self.b8)
        for i in range(self.b4):
            self.b8[i] = (self.b8[i] - b12) / (b11 - b12)
            self.b8[i] = 1 / (1 + math.exp(-self.b8[i]))
        b11 = max(self.b8)
        return self.b8.index(b11) * 90
    def fonk4(self, b19, b5):
        b13 = [0.0] * self.b4
        for k in range(self.b4):
            b14 = b19[k] - self.b8[k]
            b13[k] = b14 * self.b8[k] * (1 - self.b8[k])
        for j in range(self.b3):
            for k in range(self.b4):
                b15 = b13[k] * self.b7[j]
                self.b10[j][k] += b5 * b15
        b16 = [0.0] * self.b3
        for j in range(self.b3):
            b14 = 0.0
            for k in range(self.b4):
                b14 += b13[k] * self.b10[j][k]
            b16[j] = b14 * self.b7[j] * (1 - self.b7[j])
        for i in range(self.b2):
            for j in range(self.b3):
                b15 = b16[j] * self.b6[i]
                self.b9[i][j] += b5 * b15
    def fonk5(self, patterns, b18):
        b11 = self.fonk3(patterns)
        return b18 if b11 = = b18 else -1
    def fonk6(self, b34):
        for i in range(len(b34)
            b17 = list(map(int, b34[i][2:]))
            b18 = int(b34[i][1])
            b19 = [0] * 4
            b20 = b17
            b19[b18
            self.fonk3(b20)
            self.fonk4(b19, self.b5)
    def fonk7(self, b35):
        a3 = 0
        b21 = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as fl:
            for i in range(len(b35)):
                b17 = list(map(int, b35[i][2:]))
                b18 = int(b35[i][1])
                b11 = self.fonk5(b17, b18)
                b21[b18
                b22 = f"{b35[i][0]} {b35[i][1]}\n"
                fl.write(b22)
                if b11 = = b18:
                    a3 += 1
        print("Percentage of Efficiency", float(a3) / float(len(b35)) * 100)
        print("Confusion b21")
        for row in b21:
            print(row)
    def fonk8(self, b34, b35, k):
        b23 = [float('inf')] * int(k)
        b24 = [None] * int(k)
        b25 = list(b35[2:])
        for j in range(len(b34)
            a4 = 0
            b26 = list(b34[j][2:])
            for x in range(192):
                a4 += abs(float(b25[x]) - float(b26[x]))
            b11 = max(b23)
            if a4 < b11:
                b27 = b23.index(b11)
                b23[b27] = float(a4)
                b24[b27] = j
        b28 = [b34[b24[idx]][1] for idx in range(len(b24)) if b24[idx] is not None]
        b29 = {}
        for word in b28:
            if word in b29:
                b29[word] += 1
            else:
                b29[word] = 1
        return max(b29, b30 = b29.get)
    def fonk9(self, b34, b35, k):
        a3 = 0
        b21 = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as fl:
            for i in range(len(b35)):
                b11 = list(b35[i])
                b22 = self.fonk8(b34, b11, k)
                if b22 = = b11[1]:
                    a3 += 1
                b21[int(b11[1])
                b31 = f"{b11[0]} {b22}\n"
                fl.write(b31)
        b32 = float(a3) / float(len(b35))
        print("Percentage of Efficiency", b32 * 100)
        print("Confusion b21")
        for row in b21:
            print(row)
if b33 = = '__main__':
    b34 = [
        ["id1", "0", "1", "2", "3"],
        ["id2", "90", "4", "5", "6"],
    ]
    b35 = [
        ["id1", "0", "1", "2", "3"],
        ["id2", "90", "4", "5", "6"],
    ]
    ni, nh, no, b36 = 192, 5, 4, 0.5
    b37 = class1(ni, nh, no, b36)
    b37.fonk6(b34)
    b37.fonk7(b35)
    b37.fonk9(b34, b35, 3)