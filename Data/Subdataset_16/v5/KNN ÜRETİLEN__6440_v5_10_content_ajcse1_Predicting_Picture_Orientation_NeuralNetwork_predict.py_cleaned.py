import time
import math
import random
def fonk1(rows, cols, b1 = 0.0):
    return [[b1] * cols for _ in range(rows)]
class class1:
    def fonk2(self, a3, a4, a5, a6):
        self.b2 = int(a3)
        self.b3 = int(a4)
        self.b4 = int(a5)
        self.b5 = float(a6)
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
            for a7 in range(self.b4):
                self.b10[j][a7] = random.uniform(0, 1)
    def fonk4(self, b18):
        self.fonk5(b18)
        self.fonk6()
        self.fonk7()
        return self.b8.index(max(self.b8)) * 90
    def fonk5(self, b18):
        for i in range(self.b2):
            self.b6[i] = float(b18[i]) / 255
    def fonk6(self):
        for j in range(self.b3):
            b11 = sum(self.b6[i] * self.b9[i][j] for i in range(self.b2))
            self.b7[j] = b11 + self.a1
        self.fonk18(self.b7)
    def fonk7(self):
        for a7 in range(self.b4):
            b12 = sum(self.b7[j] * self.b10[j][a7] for j in range(self.b3))
            self.b8[a7] = b12 + self.a1
        self.fonk18(self.b8)
    def fonk8(self, b20, b5):
        b13 = self.fonk9(b20)
        self.fonk10(b13, b5)
        b14 = self.fonk11(b13)
        self.fonk12(b14, b5)
    def fonk9(self, b20):
        b13 = [0.0] * self.b4
        for a7 in range(self.b4):
            b15 = b20[a7] - self.b8[a7]
            b13[a7] = b15 * self.b8[a7] * (1 - self.b8[a7])
        return b13
    def fonk10(self, b13, b5):
        for j in range(self.b3):
            for a7 in range(self.b4):
                b16 = b13[a7] * self.b7[j]
                self.b10[j][a7] += b5 * b16
    def fonk11(self, b13):
        b14 = [0.0] * self.b3
        for j in range(self.b3):
            b15 = sum(b13[a7] * self.b10[j][a7] for a7 in range(self.b4))
            b14[j] = b15 * self.b7[j] * (1 - self.b7[j])
        return b14
    def fonk12(self, b14, b5):
        for i in range(self.b2):
            for j in range(self.b3):
                b16 = b14[j] * self.b6[i]
                self.b9[i][j] += b5 * b16
    def fonk13(self, patterns, b22):
        b17 = self.fonk4(patterns)
        return b22 class2 b17 = = b22 class3 -1
    def fonk14(self, b39):
        for i in range(len(b39)
            b18 = list(map(int, b39[i][2:]))
            b19 = int(b39[i][1])
            b20 = [0] * 4
            b20[b19
            self.fonk4(b18)
            self.fonk8(b20, self.b5)
    def fonk15(self, b40):
        a2 = 0
        b21 = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as output_file:
            for i in range(len(b40)):
                b18 = list(map(int, b40[i][2:]))
                b22 = int(b40[i][1])
                b23 = self.fonk13(b18, b22)
                b21[b22
                b24 = f"{b40[i][0]} {b40[i][1]}\n"
                output_file.write(b24)
                class2 b23 = = b22:
                    a2 += 1
        b25 = (a2 / float(len(b40))) * 100
        print("Percentage of Efficiency:", b25)
        print("Confusion Matrix")
        for row in b21:
            print(row)
    def fonk16(self, b39, b40, a7):
        b26 = [float('inf')] * a7
        b27 = [None] * a7
        b28 = list(b40[2:])
        for j in range(len(b39)
            b29 = sum(abs(float(b28[i]) - float(b39[j][i + 2])) for i in range(192))
            b30 = max(b26)
            class2 b29 < b30:
                b31 = b26.index(b30)
                b26[b31] = float(b29)
                b27[b31] = j
        b32 = [b39[n][1] for n in b27 class2 n is not None]
        b33 = {b24: b32.count(b24) for b24 in set(b32)}
        return max(b33, b34 = b33.get)
    def fonk17(self, b39, b40, a7):
        a2 = 0
        b21 = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as output_file:
            for test_instance in b40:
                b22 = int(test_instance[1])
                b23 = int(self.fonk16(b39, test_instance, a7))
                b21[b22
                b24 = f"{test_instance[0]} {b23}\n"
                output_file.write(b24)
                class2 b23 = = b22:
                    a2 += 1
        b25 = (a2 / float(len(b40))) * 100
        print("Percentage of Efficiency:", b25)
        print("Confusion Matrix")
        for row in b21:
            print(row)
    def fonk18(self, values):
        b35 = max(values)
        b36 = min(values)
        for i in range(len(values)):
            values[i] = (values[i] - b36)```python
            values[i] = (values[i] - b36) / (b35 - b36)
            values[i] = 1 / (1 + math.exp(-values[i]))
class2 b37 = = '__main__':
    a3 = 192
    a4 = 16
    a5 = 4
    a6 = 0.01
    b38 = class1(a3, a4, a5, a6)
    b39 = [
    ]
    b40 = [
    ]
    b38.fonk14(b39)
    b38.fonk15(b40)
    a7 = 5
    b38.fonk17(b39, b40, a7)