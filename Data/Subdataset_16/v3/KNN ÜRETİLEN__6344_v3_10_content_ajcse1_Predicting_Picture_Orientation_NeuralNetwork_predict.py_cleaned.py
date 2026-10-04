import math
import random
def fonk1(rows, cols, b1 = 0.0):
    return [[b1] * cols for _ in range(rows)]
class class1:
    def fonk2(self, b2, b3, b4, b5):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.a1 = 1.0
        self.b6 = [1.0] * b2
        self.b7 = [1.0] * b3
        self.b8 = [1.0] * b4
        self.b9 = fonk1(b2, b3)
        self.b10 = fonk1(b3, b4)
        self.fonk3()
    def fonk3(self):
        for i in range(self.b2):
            for j in range(self.b3):
                self.b9[i][j] = random.uniform(0, 1)
        for j in range(self.b3):
            for k in range(self.b4):
                self.b10[j][k] = random.uniform(0, 1)
    def fonk4(self, b17):
        self.fonk5(b17)
        self.fonk6()
        self.fonk7()
        b11 = max(self.b8)
        return self.b8.index(b11) * 90
    def fonk5(self, b17):
        self.b6 = [float(b17[i]) / 255.0 for i in range(self.b2)]
    def fonk6(self):
        for j in range(self.b3):
            b12 = sum(self.b6[i] * self.b9[i][j] for i in range(self.b2))
            b12 += self.a1
            self.b7[j] = self.fonk8(b12)
    def fonk7(self):
        for k in range(self.b4):
            b12 = sum(self.b7[j] * self.b10[j][k] for j in range(self.b3))
            b12 += self.a1
            self.b8[k] = self.fonk8(b12)
    @staticmethod
    def fonk8(x):
        return 1 / (1 + math.exp(-x))
    def fonk9(self, b19):
        b13 = self.fonk10(b19)
        self.fonk11(b13)
        b14 = self.fonk12(b13)
        self.fonk13(b14)
    def fonk10(self, b19):
        return [
            (b19[k] - self.b8[k]) * self.b8[k] * (1 - self.b8[k])
            for k in range(self.b4)
        ]
    def fonk11(self, b13):
        for j in range(self.b3):
            for k in range(self.b4):
                b15 = b13[k] * self.b7[j]
                self.b10[j][k] += self.b5 * b15
    def fonk12(self, b13):
        return [
            sum(b13[k] * self.b10[j][k] for k in range(self.b4)) * self.b7[j] * (1 - self.b7[j])
            for j in range(self.b3)
        ]
    def fonk13(self, b14):
        for i in range(self.b2):
            for j in range(self.b3):
                b15 = b14[j] * self.b6[i]
                self.b9[i][j] += self.b5 * b15
    def fonk14(self, patterns, expected):
        b16 = self.fonk4(patterns)
        return expected if b16 = = expected else -1
    def fonk15(self, b34):
        for data in b34:
            b17 = list(map(int, data[2:]))
            b18 = int(data[1])
            b19 = [0] * self.b4
            b19[b18
            self.fonk4(b17)
            self.fonk9(b19)
    def fonk16(self, b35):
        a2 = 0
        b20 = fonk1(4, 4, 0)
        with open("nnet_output.txt", 'w') as file:
            for data in b35:
                b17 = list(map(int, data[2:]))
                b21 = int(data[1])
                b22 = self.fonk14(b17, b21)
                b20[b21
                file.write(f"{data[0]} {b22}\n")
                if b22 = = b21:
                    a2 += 1
        b23 = float(a2) / float(len(b35)) * 100
        print(f"Percentage of Efficiency: {b23}")
        print("Confusion Matrix")
        for row in b20:
            print(row)
    def fonk17(self, b34, b35, k):
        b24 = [float('inf')] * k
        b25 = [None] * k
        b26 = list(map(float, b35[2:]))
        for i, train_sample in enumerate(b34):
            b27 = list(map(float, train_sample[2:]))
            b28 = sum(abs(b26[x] - b27[x]) for x in range(len(b26)))
            b29 = max(b24)
            if b28 < b29:
                b30 = b24.index(b29)
                b24[b30] = b28
                b25[b30] = i
        b31 = [b34[idx][1] for idx in b25 if idx is not None]
        b32 = max(set(b31), key=b31.count)
        return b32
    def fonk18(self, b34, b35, k):
        a2 = 0
        b20 = fonk1(4, 4, 0)
        with open("knn_output.txt", 'w') as file:
            for data in b35:
                b22 = self.fonk17(b34, data, k)
                b21 = data[1]
                b20[int(b21)
                file.write(f"{data[0]} {b22}\n")
                if b22 = = b21:
                    a2 += 1
        b23 = float(correct```python
count) / float(len(b35)) * 100
        print(f"Percentage of Efficiency: {b23}")
        print("Confusion Matrix")
        for row in b20:
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
    b37.fonk15(b34)
    b37.fonk16(b35)
    b37.fonk18(b34, b35, 3)