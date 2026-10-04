import time
import math
import random
def fonk1(rows, cols, b1 = 0.0):
    return [[b1] * cols for _ in range(rows)]
class class1:
    def fonk2(self, ni, nh, no, lr):
        self.b2 = int(ni)
        self.b3 = int(nh)
        self.b4 = int(no)
        self.b5 = float(lr)
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
    def fonk3(self, b17):
        for i in range(self.b2):
            self.b6[i] = float(b17[i]) / 255
        for j in range(self.b3):
            b11 = b11(self.b6[i] * self.b9[i][j] for i in range(self.b2))
            self.b7[j] = b11 + self.a1
        self.fonk10(self.b7)
        for k in range(self.b4):
            b11 = b11(self.b7[j] * self.b10[j][k] for j in range(self.b3))
            self.b8[k] = b11 + self.a1
        self.fonk10(self.b8)
        return self.b8.index(max(self.b8)) * 90
    def fonk4(self, b19, b5):
        b12 = [0.0] * self.b4
        for k in range(self.b4):
            b13 = b19[k] - self.b8[k]
            b12[k] = b13 * self.b8[k] * (1 - self.b8[k])
        for j in range(self.b3):
            for k in range(self.b4):
                b14 = b12[k] * self.b7[j]
                self.b10[j][k] += b5 * b14
        b15 = [0.0] * self.b3
        for j in range(self.b3):
            b13 = b11(b12[k] * self.b10[j][k] for k in range(self.b4))
            b15[j] = b13 * self.b7[j] * (1 - self.b7[j])
        for i in range(self.b2):
            for j in range(self.b3):
                b14 = b15[j] * self.b6[i]
                self.b9[i][j] += b5 * b14
    def fonk5(self, patterns, s):
        b16 = self.fonk3(patterns)
        return s if b16 = = s else -1
    def fonk6(self, train_data):
        for i in range(len(train_data)
            b17 = list(map(int, train_data[i][2:]))
            b18 = int(train_data[i][1])
            b19 = [0] * 4
            b19[b18
            self.fonk3(b17)
            self.fonk4(b19, self.b5)
    def fonk7(self, test_data):
        a2 = 0
        b20 = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as output_file:
            for i in range(len(test_data)):
                b17 = list(map(int, test_data[i][2:]))
                b21 = int(test_data[i][1])
                b22 = self.fonk5(b17, b21)
                b20[b21
                b23 = f"{test_data[i][0]} {test_data[i][1]}\n"
                output_file.write(b23)
                if b22 = = b21:
                    a2 += 1
        b24 = (a2 / float(len(test_data))) * 100
        print("Percentage of Efficiency:", b24)
        print("Confusion Matrix")
        for row in b20:
            print(row)
    def fonk8(self, train_data, test_data, k):
        b25 = [float('inf')] * k
        b26 = [None] * k
        b27 = list(test_data[2:])
        for j in range(len(train_data)
            b28 = b11(abs(float(b27[i]) - float(train_data[j][i + 2])) for i in range(192))
            b29 = max(b25)
            if b28 < b29:
                b30 = b25.index(b29)
                b25[b30] = float(b28)
                b26[b30] = j
        b31 = [train_data[n][1] for n in b26 if n is not None]
        b32 = {b23: b31.count(b23) for b23 in set(b31)}
        return max(b32, b33 = b32.get)
    def fonk9(self, train_data, test_data, k):
        a2 = 0
        b20 = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as output_file:
            for test_instance in test_data:
                b21 = int(test_instance[1])
                b22 = int(self.fonk8(train_data, test_instance, k))
                b20[b21
                b23 = f"{test_instance[0]} {b22}\n"
                output_file.write(b23)
                if b22 = = b21:
                    a2 += 1
        b24 = (a2 / float(len(test_data))) * 100
        print("Percentage of Efficiency:", b24)
        print("Confusion Matrix")
        for row in b20:
            print(row)
    def fonk10(self, values):
        b34 = max(values)
        b35 = min(values)
        for i in range(len(values)):
            values[i] = (values[i] - b35) / (b34 - b35)
            values[i] = 1 / (1 + math.exp(-values[i]))