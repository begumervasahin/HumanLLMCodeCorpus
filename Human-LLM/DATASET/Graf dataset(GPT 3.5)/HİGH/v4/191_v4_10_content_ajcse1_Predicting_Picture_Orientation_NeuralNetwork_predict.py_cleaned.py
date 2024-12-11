import time
import math
import random
def fonk1(rows, cols, b1 = 0.0):
    b2 = []
    for i in range(rows):
        b2.append([b1] * cols)
    return b2
class class1:
    def fonk2(self, input_nodes, hidden_nodes, output_nodes, b6):
        self.b3 = int(input_nodes)
        self.b4 = int(hidden_nodes)
        self.b5 = int(output_nodes)
        self.b6 = float(b6)
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
            for k in range(self.b5):
                self.b11[j][k] = random.uniform(0, 1)
    def fonk3(self, b23):
        for i in range(self.b3):
            self.b7[i] = float(b23[i]) / float(255)
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
        for k in range(self.b5):
            a2 = 0.0
            for j in range(self.b4):
                a2 += (self.b8[j] * self.b11[j][k])
            self.b9[k] = a2 + self.a1
        b12 = max(self.b9)
        return self.b9.index(b12) * 90
    def fonk4(self, b22):
        b14 = [0.0] * self.b5
        for k in range(self.b5):
            b15 = b22[k] - self.b9[k]
            b14[k] = b15 * self.b9[k] * (1 - self.b9[k])
        for j in range(self.b4):
            for k in range(self.b5):
                b16 = b14[k] * self.b8[j]
                self.b11[j][k] += self.b6 * b16
        b17 = [0.0] * self.b4
        for j in range(self.b4):
            b15 = 0.0
            for k in range(self.b5):
                b15 += b14[k] * self.b11[j][k]
            b17[j] = b15 * self.b8[j] * (1 - self.b8[j])
        for i in range(self.b3):
            for j in range(self.b4):
                b16 = b17[j] * self.b7[i]
                self.b10[i][j] += self.b6 * b16
    def fonk5(self, patterns, b20):
        b18 = self.fonk3(patterns)
        if b18 = = b20:
            return b20
        else:
            return -1
    def fonk6(self, train_data):
        for i in range(0, len(train_data) / 2):
            b19 = map(int, train_data[i][2:])
            b20 = int(train_data[i][1])
            b21 = [b19, [b20]]
            b22 = [0] * 4
            b23 = b21[0]
            b22[b20 / 90] = 1
            self.fonk3(b23)
            self.fonk4(b22)
    def fonk7(self, test_data):
        a3 = 0
        b2 = [[0 for x in range(4)] for x in range(4)]
        b24 = open("nnet_output.txt", 'w')
        for i in range(0, len(test_data)):
            b19 = map(int, test_data[i][2:])
            b20 = int(test_data[i][1])
            b21 = [b19, [b20]]
            b23 = b21[0]
            b18 = self.fonk5(b23, b20)
            b2[b20 / 90][b18 / 90] += 1
            b25 = test_data[i][0] + " " + test_data[i][1] + "\n"
            b24.write(b25)
            if b18 = = b20:
                a3 += 1
        print "Percentage of Efficiency", float(a3) / float(len(test_data)) * 100
        print "Confusion Matrix"
        for i in range(0, 4):
            print b2[i]
    def fonk8(self, train_data, test_data, k):
        a3 = 0
        b2 = [[0 for x in range(4)] for x in range(4)]
        b24 = open("knn_output.txt", 'w')
        for i in range(0, len(test_data)):
            b18 = list(test_data[i])
            b25 = self.knnd(train_data, b18, k)
            if b25 = = b18[1]:
                a3 += 1
            b2[int(b18[1]) / 90][int(b25) / 90] += 1
            b25 = b18[0] + " " + b25 + "\n"
            b24.write(b25)
        b26 = float(a3) / float(len(test_data)) * 100
        print "Percentage of Efficiency", b26
        print "Confusion Matrix"
        for i in range(0, 4):
            print b2[i]