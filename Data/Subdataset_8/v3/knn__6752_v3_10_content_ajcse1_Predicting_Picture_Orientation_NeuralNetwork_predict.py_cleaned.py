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
        self.initialize_weights()
    def initialize_weights(self):
        for i in range(self.ninput):
            for j in range(self.nhidden):
                self.iweight[i][j] = random.uniform(0, 1)
        for j in range(self.nhidden):
            for k in range(self.noutput):
                self.oweight[j][k] = random.uniform(0, 1)
    def update(self, inputs):
        for i in range(self.ninput):
            self.iactive[i] = float(inputs[i]) / float(255)
        self.update_hidden_layer()
        self.update_output_layer()
        return self.oactive.index(max(self.oactive)) * 90
    def update_hidden_layer(self):
        for j in range(self.nhidden):
            sum_input = sum(self.iactive[i] * self.iweight[i][j] for i in range(self.ninput))
            self.hactive[j] = sum_input + self.bias
            self.hactive[j] = (self.hactive[j] - min(self.hactive)) / (max(self.hactive) - min(self.hactive))
            self.hactive[j] = 1 / (1 + math.exp(-self.hactive[j]))
    def update_output_layer(self):
        for k in range(self.noutput):
            sum_hidden = sum(self.hactive[j] * self.oweight[j][k] for j in range(self.nhidden))
            self.oactive[k] = sum_hidden + self.bias
            self.oactive[k] = self.oactive[k] / max(self.oactive)
            self.oactive[k] = 1 / (1 + math.exp(-self.oactive[k]))
    def backpropagate(self, targets):
        odeltas = [0.0] * self.noutput
        for k in range(self.noutput):
            error = targets[k] - self.oactive[k]
            odeltas[k] = error * self.oactive[k] * (1 - self.oactive[k])
            self.update_output_weights(k, odeltas[k])
        hdeltas = [0.0] * self.nhidden
        for j in range(self.nhidden):
            error = sum(odeltas[k] * self.oweight[j][k] for k in range(self.noutput))
            hdeltas[j] = error * self.hactive[j] * (1 - self.hactive[j])
            self.update_hidden_weights(j, hdeltas[j])
    def update_output_weights(self, j, delta):
        for k in range(self.noutput):
            change = delta * self.hactive[j]
            self.oweight[j][k] += self.lrate * change
    def update_hidden_weights(self, i, delta):
        for j in range(self.nhidden):
            change = delta * self.iactive[i]
            self.iweight[i][j] += self.lrate * change
    def test(self, patterns, s):
        t = self.update(patterns)
        if t == s:
            return s
        else:
            return -1
    def train(self, train_data):
        for i in range(len(train_data)
            inputs = list(map(int, train_data[i][2:]))
            target = int(train_data[i][1])
            self.update(inputs)
            self.backpropagate([1 if i == target else 0 for i in range(self.noutput)])
    def tests(self, test_data):
        count = 0
        confusion_matrix = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as fl:
            for i in range(len(test_data)):
                inputs = list(map(int, test_data[i][2:]))
                expected_orientation = int(test_data[i][1])
                predicted_orientation = self.test(inputs, expected_orientation)
                confusion_matrix[expected_orientation
                orientation = test_data[i][0] + " " + str(predicted_orientation) + "\n"
                fl.write(orientation)
                if predicted_orientation == expected_orientation:
                    count += 1
        accuracy = float(count) / float(len(test_data)) * 100
        print("Percentage of Accuracy:", accuracy)
        print("Confusion Matrix:")
        for row in confusion_matrix:
            print(row)
    def knn(self, train_data, test_data, k):
        count = 0
        confusion_matrix = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as fl:
            for i in range(len(test_data)):
                inputs = list(test_data[i])
                expected_orientation = int(inputs[1])
                predicted_orientation = self.knnd(train_data, inputs, k)
                confusion_matrix[expected_orientation
                orientation = inputs[0] + " " + str(predicted_orientation) + "\n"
                fl.write(orientation)
                if predicted_orientation == expected_orientation:
                    count += 1
        accuracy = float(count) / float(len(test_data)) * 100
        print("Percentage of Accuracy:", accuracy)
        print("Confusion Matrix:")
        for row in confusion_matrix:
            print(row)
    def knnd(self, train_data, test_data, k):
        klist = [float('inf') for _ in range(int(k))]
        kind = [None] * int(k)
        idata = list(test_data[2:])
        for j in range(len(train_data)
            jdata = list(train_data[j][2:])
            distance = sum(abs(float(idata[k]) - float(jdata[k])) for k in range(192))
            t = max(klist)
            if distance < t:
                ind = klist.index(t)
                klist[ind] = float(distance)
                kind[ind] = j
        ori = [train_data[kind[k]][1] for k in range(len(kind))]
        word_counter = {}
        for word in ori:
            word_counter[word] = word_counter.get(word, 0) + 1
        return max(word_counter, key=word_counter.get)
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