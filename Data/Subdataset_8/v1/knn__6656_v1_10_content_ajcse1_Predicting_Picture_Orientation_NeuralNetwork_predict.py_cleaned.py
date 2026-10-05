import time
import math
import random
def createMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m
class Predict:
    def __init__(self, ni, nh, no, lr):
        self.ninput = int(ni)
        self.nhidden = int(nh)
        self.noutput = int(no)
        self.lrate = float(lr)
        self.iactive = [1.0] * self.ninput
        self.hactive = [1.0] * self.nhidden
        self.oactive = [1.0] * self.noutput
        self.iweight = createMatrix(self.ninput, self.nhidden)
        self.oweight = createMatrix(self.nhidden, self.noutput)
        self.bias = 1.0
        for i in range(self.ninput):
            for j in range(self.nhidden):
                self.iweight[i][j] = random.uniform(0, 1)
        for j in range(self.nhidden):
            for k in range(self.noutput):
                self.oweight[j][k] = random.uniform(0, 1)
    def update(self, inputs):
        for i in range(self.ninput):
            self.iactive[i] = float(inputs[i]) / float(255)
        for j in range(self.nhidden):
            sum = 0.0
            for i in range(self.ninput):
                sum += (self.iactive[i] * self.iweight[i][j])
            sum += self.bias
            self.hactive[j] = sum
        t = max(self.hactive, key=float)
        r = min(self.hactive, key=float)
        for i in range(self.nhidden):
            self.hactive[i] = (self.hactive[i] - r) / (t - r)
            self.hactive[i] = 1 / (1 + math.exp(-self.hactive[i]))
        for k in range(self.noutput):
            sum = 0.0
            for j in range(self.nhidden):
                sum += (self.hactive[j] * self.oweight[j][k])
            self.oactive[k] = sum + self.bias
        t = max(self.oactive, key=float)
        for i in range(self.noutput):
            self.oactive[i] = self.oactive[i] / t
            self.oactive[i] = 1 / (1 + math.exp(-self.oactive[i]))
        return self.oactive.index(t) * 90
    def backpropagate(self, targets, lrate):
        odeltas = [0.0] * self.noutput
        for k in range(self.noutput):
            error = targets[k] - self.oactive[k]
            odeltas[k] = error * self.oactive[k] * (1 - self.oactive[k])
        for j in range(self.nhidden):
            for k in range(self.noutput):
                change = odeltas[k] * self.hactive[j]
                self.oweight[j][k] += lrate * change
        hdeltas = [0.0] * self.nhidden
        for j in range(self.nhidden):
            error = 0.0
            for k in range(self.noutput):
                error += odeltas[k] * self.oweight[j][k]
            hdeltas[j] = error * self.hactive[j] * (1 - self.hactive[j])
        for i in range(self.ninput):
            for j in range(self.nhidden):
                change = hdeltas[j] * self.iactive[i]
                self.iweight[i][j] += lrate * change
    def test(self, patterns, s):
        t = self.update(patterns)
        if t == s:
            return s
        else:
            return -1
    def train(self, train_data):
        for i in range(len(train_data)
            l = list(map(int, train_data[i][2:]))
            s = int(train_data[i][1])
            p = [l, [s]]
            targets = [0] * 4
            inputs = p[0]
            targets[s
            self.update(inputs)
            self.backpropagate(targets, self.lrate)
    def tests(self, test_data):
        count = 0
        Matrix = [[0 for x in range(4)] for x in range(4)]
        fl = open("nnet_output.txt", 'w')
        for i in range(len(test_data)):
            l = list(map(int, test_data[i][2:]))
            s = int(test_data[i][1])
            p = [l, [s]]
            inputs = p[0]
            t = self.test(inputs, s)
            Matrix[s
            orientation = test_data[i][0] + " " + test_data[i][1] + "\n"
            fl.write(orientation)
            if t == s:
                count += 1
        print("Percentage of Efficiency", float(count) / float(len(test_data)) * 100)
        print("Confusion Matrix")
        for i in range(4):
            print(Matrix[i])
    def knnd(self, train_data, test_data, k):
        klist = [float(100000000000000000) for x in range(int(k))]
        kind = [None] * int(k)
        idata = list(test_data[2:])
        for j in range(len(train_data)
            distance = 0
            jdata = list(train_data[j][2:])
            for k in range(192):
                distance += abs(float(idata[k]) - float(jdata[k]))
            t = max(klist, key=float)
            if distance < t:
                ind = klist.index(t)
                klist[ind] = float(distance)
                kind[ind] = j
        ori = []
        for kindl in range(len(kind)):
            ori.append(train_data[kind[kindl]][1])
        olist = ['0', '90', '180', '270']
        word_counter = {}
        for word in ori:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        return max(word_counter, key=word_counter.get)
    def knn(self, train_data, test_data, k):
        count = 0
        Matrix = [[0 for x in range(4)] for x in range(4)]
        fl = open("knn_output.txt", 'w')
        for i in range(len(test_data)):
            t = list(test_data[i])
            orientation = self.knnd(train_data, t, k)
            if orientation == t[1]:
                count += 1
            Matrix[int(t[1])
            orientation = t[0] + " " + orientation + "\n"
            fl.write(orientation)
        o = float(count) / float(len(test_data))
        print("Percentage of Efficiency", o * float(100))
        print("Confusion Matrix")
        for i in range(4):
            print(Matrix[i])
def example_usage():
    p = Predict(192, 100, 4, 0.1)
    train_data = [[random.randint(0, 255) for _ in range(194)] for _ in range(100)]
    test_data = [[random.randint(0, 255) for _ in range(194)] for _ in range(20)]
    p.train(train_data)
    p.tests(test_data)
    k = 5
    p.knn(train_data, test_data, k)
if __name__ == "__main__":
    example_usage()