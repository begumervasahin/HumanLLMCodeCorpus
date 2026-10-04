import time
import math
import random
def fonk1(I, J, b1 = 0.0):
    return [[b1] * J for _ in range(I)]
class class1:
    def fonk2(self, ni, nh, no, b34):
        self.b2 = int(ni)
        self.b3 = int(nh)
        self.b4 = int(no)
        self.b5 = float(b34)
        self.b6 = [1.0] * self.b2
        self.b7 = [1.0] * self.b3
        self.b8 = [1.0] * self.b4
        self.b9 = fonk1(self.b2, self.b3)
        self.b10 = fonk1(self.b3, self.b4)
        self.a1 = 1.0
        self.fonk3()
    def fonk3(self):
        for i in range(self.b2):
            for j in range(self.b3):
                self.b9[i][j] = random.uniform(0, 1)
        for j in range(self.b3):
            for k in range(self.b4):
                self.b10[j][k] = random.uniform(0, 1)
    def fonk4(self, b19):
        self.fonk5(b19)
        self.fonk6()
        self.fonk7()
        b11 = max(self.b8)
        return self.b8.index(b11) * 90
    def fonk5(self, b19):
        for i in range(self.b2):
            self.b6[i] = float(b19[i]) / 255.0
    def fonk6(self):
        for j in range(self.b3):
            b12 = sum(self.b6[i] * self.b9[i][j] for i in range(self.b2))
            b12 += self.a1
            self.b7[j] = self.fonk8(b12)
    def fonk7(self):
        for k in range(self.b4):
            b12 = sum(self.b7[j] * self.b10[j][k] for j in range(self.b3))
            self.b8[k] = self.fonk8(b12 + self.a1)
    @staticmethod
    def fonk8(x):
        return 1 / (1 + math.exp(-x))
    def fonk9(self, b18, b5):
        b13 = self.fonk10(b18)
        self.fonk11(b13, b5)
        b14 = self.fonk12(b13)
        self.fonk13(b14, b5)
    def fonk10(self, b18):
        return [
            (b18[k] - self.b8[k]) * self.b8[k] * (1 - self.b8[k])
            for k in range(self.b4)
        ]
    def fonk11(self, b13, b5):
        for j in range(self.b3):
            for k in range(self.b4):
                b15 = b13[k] * self.b7[j]
                self.b10[j][k] += b5 * b15
    def fonk12(self, b13):
        return [
            sum(b13[k] * self.b10[j][k] for k in range(self.b4)) * self.b7[j] * (1 - self.b7[j])
            for j in range(self.b3)
        ]
    def fonk13(self, b14, b5):
        for i in range(self.b2):
            for j in range(self.b3):
                b15 = b14[j] * self.b6[i]
                self.b9[i][j] += b5 * b15
    def fonk14(self, patterns, b17):
        b11 = self.fonk4(patterns)
        return b17 if b11 = = b17 else -1
    def fonk15(self, b32):
        for i in range(len(b32)
            b16 = list(map(int, b32[i][2:]))
            b17 = int(b32[i][1])
            b18 = [0] * 4
            b19 = b16
            b18[b17
            self.fonk4(b19)
            self.fonk9(b18, self.b5)
    def fonk16(self, b33):
        a2 = 0
        b20 = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as fl:
            for i in range(len(b33)):
                b16 = list(map(int, b33[i][2:]))
                b17 = int(b33[i][1])
                b11 = self.fonk14(b16, b17)
                b20[b17
                fl.write(f"{b33[i][0]} {b33[i][1]}\n")
                if b11 = = b17:
                    a2 += 1
        print(f"Percentage of Efficiency: {float(a2) / float(len(b33)) * 100}")
        print("Confusion Matrix")
        for row in b20:
            print(row)
    def fonk17(self, b32, b33, k):
        b21 = [float('inf')] * int(k)
        b22 = [None] * int(k)
        b23 = list(b33[2:])
        for j in range(len(b32)
            b24 = sum(abs(float(b23[x]) - float(b32[j][2 + x])) for x in range(192))
            b11 = max(b21)
            if b24 < b11:
                b25 = b21.index(b11)
                b21[b25] = float(b24)
                b22[b25] = j
        b26 = [b32[b22[idx]][1] for idx in range(len(b22)) if b22[idx] is not None]
        b27 = {}
        for word in b26:
            b27[word] = b27.get(word, 0) + 1
        return max(b27, b28 = b27.get)
    def fonk18(self, b32, b33, k):
        a2 = 0
        b20 = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as fl:
            for i in range(len(b33)):
                b11 = list(b33[i])
                b29 = self.fonk17(b32, b11, k)
                if b29 = = b11[1]:
                    a2 += 1
                b20[int(b11```python
[1])
                fl.write(f"{b11[0]} {b29}\n")
        b30 = float(a2) / float(len(b33)) * 100
        print(f"Percentage of Efficiency: {b30}")
        print("Confusion Matrix")
        for row in b20:
            print(row)
if b31 = = '__main__':
    b32 = [
        ["id1", "0", "1", "2", "3"],
        ["id2", "90", "4", "5", "6"],
    ]
    b33 = [
        ["id1", "0", "1", "2", "3"],
        ["id2", "90", "4", "5", "6"],
    ]
    ni, nh, no, b34 = 192, 5, 4, 0.5
    b35 = class1(ni, nh, no, b34)
    b35.fonk15(b32)
    b35.fonk16(b33)
    b35.fonk18(b32, b33, 3)