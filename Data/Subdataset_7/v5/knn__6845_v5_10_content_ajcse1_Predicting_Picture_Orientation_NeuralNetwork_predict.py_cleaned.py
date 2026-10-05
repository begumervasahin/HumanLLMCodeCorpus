import random
import math
class class1:
    def fonk1(self, input_nodes, hidden_nodes, output_nodes, b4):
        self.b1 = int(input_nodes)
        self.b2 = int(hidden_nodes)
        self.b3 = int(output_nodes)
        self.b4 = float(b4)
        self.b5 = [1.0] * self.b1
        self.b6 = [1.0] * self.b2
        self.b7 = [1.0] * self.b3
        self.b8 = self.fonk2(self.b1, self.b2)
        self.b9 = self.fonk2(self.b2, self.b3)
        self.a1 = 1.0
    def fonk2(self, rows, cols):
        return [[random.uniform(0, 1) for _ in range(cols)] for _ in range(rows)]
    def fonk3(self, x):
        return 1 / (1 + math.exp(-x))
    def fonk4(self):
        for j in range(self.b2):
            b10 = sum(self.b5[i] * self.b8[i][j] for i in range(self.b1))
            b10 += self.a1
            self.b6[j] = b10
            self.b6[j] = self.fonk3(self.b6[j])
        for k in range(self.b3):
            b10 = sum(self.b6[j] * self.b9[j][k] for j in range(self.b2))
            self.b7[k] = b10 + self.a1
    def fonk5(self, b14):
        b11 = [(b14[k] - self.b7[k]) * self.b7[k] * (1 - self.b7[k]) for k in range(self.b3)]
        for j in range(self.b2):
            for k in range(self.b3):
                self.b9[j][k] += self.b4 * b11[k] * self.b6[j]
        b12 = [sum(b11[k] * self.b9[j][k] for k in range(self.b3)) * self.b6[j] * (1 - self.b6[j]) for j in range(self.b2)]
        for i in range(self.b1):
            for j in range(self.b2):
                self.b8[i][j] += self.b4 * b12[j] * self.b5[i]
    def fonk6(self, train_data):
        for data in train_data:
            b13 = map(int, data[2:])
            b14 = [0] * self.b3
            b14[int(data[1])
            self.b5 = [float(i) / 255 for i in b13]
            self.fonk4()
            self.fonk5(b14)
    def fonk7(self, b13):
        self.b5 = [float(i) / 255 for i in b13]
        self.fonk4()
        return self.b7.index(max(self.b7)) * 90
    def fonk8(self, test_data):
        a2 = 0
        b15 = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as f_out:
            for data in test_data:
                b13 = map(int, data[2:])
                b16 = self.fonk7(b13)
                b17 = int(data[1])
                f_out.write(data[0] + " " + str(b16) + "\n")
                if b16 = = b17:
                    a2 += 1
                b15[b17
        b18 = float(a2) / float(len(test_data)) * 100
        print("Percentage of Efficiency:", b18)
        print("Confusion Matrix:")
        for row in b15:
            print(row)
    def fonk9(self, train_data, test_data, k):
        a2 = 0
        b15 = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as f_out:
            for data in test_data:
                b13 = list(map(int, data))
                b16 = self.fonk10(train_data, b13, k)
                b17 = b13[1]
                f_out.write(data[0] + " " + str(b16) + "\n")
                if b16 = = b17:
                    a2 += 1
                b15[b17
        b18 = float(a2) / float(len(test_data)) * 100
        print("Percentage of Efficiency:", b18)
        print("Confusion Matrix:")
        for row in b15:
            print(row)
    def fonk10(self, train_data, test_instance, k):
        b19 = []
        for train_instance in train_data:
            b20 = self.fonk11(train_instance[2:], test_instance[2:])
            b19.append((train_instance[1], b20))
        b19.sort(b21 = lambda x: x[1])
        b22 = b19[:k]
        b23 = {90: 0, 180: 0, 270: 0, 360: 0}
        for neighbor in b22:
            b23[neighbor[0]] += 1
        return max(b23.items(), b21 = lambda x: x[1])[0]
    @staticmethod
    def fonk11(instance1, instance2):
        return math.sqrt(sum((float(instance1[i]) - float(instance2[i])) ** 2 for i in range(len(instance1))))
def fonk12(rows, cols, b24 = 0.0):
    return [[b24] * cols for _ in range(rows)]
def fonk13():
    pass
if b25 = = "__main__":
    fonk13()