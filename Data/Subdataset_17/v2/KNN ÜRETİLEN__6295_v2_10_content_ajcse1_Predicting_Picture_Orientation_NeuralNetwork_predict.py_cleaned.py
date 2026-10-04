import time
import math
import random
def create_matrix(I, J, fill=0.0):
    return [[fill] * J for _ in range(I)]
class Predict:
    def __init__(self, ni, nh, no, lr):
        self.ninput = int(ni)
        self.nhidden = int(nh)
        self.noutput = int(no)
        self.lrate = float(lr)
        self.iactive = [1.0] * self.ninput
        self.hactive = [1.0] * self.nhidden
        self.oactive = [1.0] * self.noutput
        self.iweight = create_matrix(self.ninput, self.nhidden)
        self.oweight = create_matrix(self.nhidden, self.noutput)
        self.bias = 1.0
        self._initialize_weights()
    def _initialize_weights(self):
        for i in range(self.ninput):
            for j in range(self.nhidden):
                self.iweight[i][j] = random.uniform(0, 1)
        for j in range(self.nhidden):
            for k in range(self.noutput):
                self.oweight[j][k] = random.uniform(0, 1)
    def update(self, inputs):
        self._activate_input_layer(inputs)
        self._activate_hidden_layer()
        self._activate_output_layer()
        t = max(self.oactive)
        return self.oactive.index(t) * 90
    def _activate_input_layer(self, inputs):
        for i in range(self.ninput):
            self.iactive[i] = float(inputs[i]) / 255.0
    def _activate_hidden_layer(self):
        for j in range(self.nhidden):
            sum_ = sum(self.iactive[i] * self.iweight[i][j] for i in range(self.ninput))
            sum_ += self.bias
            self.hactive[j] = self._sigmoid(sum_)
    def _activate_output_layer(self):
        for k in range(self.noutput):
            sum_ = sum(self.hactive[j] * self.oweight[j][k] for j in range(self.nhidden))
            self.oactive[k] = self._sigmoid(sum_ + self.bias)
    @staticmethod
    def _sigmoid(x):
        return 1 / (1 + math.exp(-x))
    def backpropagate(self, targets, lrate):
        odeltas = self._calculate_output_deltas(targets)
        self._update_output_weights(odeltas, lrate)
        hdeltas = self._calculate_hidden_deltas(odeltas)
        self._update_input_weights(hdeltas, lrate)
    def _calculate_output_deltas(self, targets):
        return [
            (targets[k] - self.oactive[k]) * self.oactive[k] * (1 - self.oactive[k])
            for k in range(self.noutput)
        ]
    def _update_output_weights(self, odeltas, lrate):
        for j in range(self.nhidden):
            for k in range(self.noutput):
                change = odeltas[k] * self.hactive[j]
                self.oweight[j][k] += lrate * change
    def _calculate_hidden_deltas(self, odeltas):
        return [
            sum(odeltas[k] * self.oweight[j][k] for k in range(self.noutput)) * self.hactive[j] * (1 - self.hactive[j])
            for j in range(self.nhidden)
        ]
    def _update_input_weights(self, hdeltas, lrate):
        for i in range(self.ninput):
            for j in range(self.nhidden):
                change = hdeltas[j] * self.iactive[i]
                self.iweight[i][j] += lrate * change
    def test(self, patterns, s):
        t = self.update(patterns)
        return s if t == s else -1
    def train(self, train_data):
        for i in range(len(train_data)
            l = list(map(int, train_data[i][2:]))
            s = int(train_data[i][1])
            targets = [0] * 4
            inputs = l
            targets[s
            self.update(inputs)
            self.backpropagate(targets, self.lrate)
    def tests(self, test_data):
        count = 0
        matrix = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as fl:
            for i in range(len(test_data)):
                l = list(map(int, test_data[i][2:]))
                s = int(test_data[i][1])
                t = self.test(l, s)
                matrix[s
                fl.write(f"{test_data[i][0]} {test_data[i][1]}\n")
                if t == s:
                    count += 1
        print(f"Percentage of Efficiency: {float(count) / float(len(test_data)) * 100}")
        print("Confusion Matrix")
        for row in matrix:
            print(row)
    def knnd(self, train_data, test_data, k):
        klist = [float('inf')] * int(k)
        kind = [None] * int(k)
        idata = list(test_data[2:])
        for j in range(len(train_data)
            distance = sum(abs(float(idata[x]) - float(train_data[j][2 + x])) for x in range(192))
            t = max(klist)
            if distance < t:
                ind = klist.index(t)
                klist[ind] = float(distance)
                kind[ind] = j
        ori = [train_data[kind[idx]][1] for idx in range(len(kind)) if kind[idx] is not None]
        word_counter = {}
        for word in ori:
            word_counter[word] = word_counter.get(word, 0) + 1
        return max(word_counter, key=word_counter.get)
    def knn(self, train_data, test_data, k):
        count = 0
        matrix = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as fl:
            for i in range(len(test_data)):
                t = list(test_data[i])
                orientation = self.knnd(train_data, t, k)
                if orientation == t[1]:
                    count += 1
                matrix[int(t```python
[1])
                fl.write(f"{t[0]} {orientation}\n")
        efficiency = float(count) / float(len(test_data)) * 100
        print(f"Percentage of Efficiency: {efficiency}")
        print("Confusion Matrix")
        for row in matrix:
            print(row)
if __name__ == '__main__':
    train_data = [
        ["id1", "0", "1", "2", "3"],
        ["id2", "90", "4", "5", "6"],
    ]
    test_data = [
        ["id1", "0", "1", "2", "3"],
        ["id2", "90", "4", "5", "6"],
    ]
    ni, nh, no, lr = 192, 5, 4, 0.5
    predict = Predict(ni, nh, no, lr)
    predict.train(train_data)
    predict.tests(test_data)
    predict.knn(train_data, test_data, 3)