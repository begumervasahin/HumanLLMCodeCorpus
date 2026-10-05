import time
import math
import random
def create_matrix(rows, cols, fill=0.0):
    matrix = []
    for i in range(rows):
        matrix.append([fill] * cols)
    return matrix
class Predict:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.n_input = int(input_nodes)
        self.n_hidden = int(hidden_nodes)
        self.n_output = int(output_nodes)
        self.learning_rate = float(learning_rate)
        self.i_active = [1.0] * self.n_input
        self.h_active = [1.0] * self.n_hidden
        self.o_active = [1.0] * self.n_output
        self.i_weight = create_matrix(self.n_input, self.n_hidden)
        self.o_weight = create_matrix(self.n_hidden, self.n_output)
        self.bias = 1.0
        for i in range(self.n_input):
            for j in range(self.n_hidden):
                self.i_weight[i][j] = random.uniform(0, 1)
        for j in range(self.n_hidden):
            for k in range(self.n_output):
                self.o_weight[j][k] = random.uniform(0, 1)
    def update(self, inputs):
        for i in range(self.n_input):
            self.i_active[i] = float(inputs[i]) / float(255)
        for j in range(self.n_hidden):
            sum_ = 0.0
            for i in range(self.n_input):
                sum_ += (self.i_active[i] * self.i_weight[i][j])
            sum_ += self.bias
            self.h_active[j] = sum_
        max_value = max(self.h_active)
        min_value = min(self.h_active)
        for i in range(self.n_hidden):
            self.h_active[i] = (self.h_active[i] - min_value) / (max_value - min_value)
            self.h_active[i] = 1 / (1 + math.exp(-self.h_active[i]))
        for k in range(self.n_output):
            sum_ = 0.0
            for j in range(self.n_hidden):
                sum_ += (self.h_active[j] * self.o_weight[j][k])
            self.o_active[k] = sum_ + self.bias
        max_value = max(self.o_active)
        return self.o_active.index(max_value) * 90
    def backpropagate(self, targets):
        o_deltas = [0.0] * self.n_output
        for k in range(self.n_output):
            error = targets[k] - self.o_active[k]
            o_deltas[k] = error * self.o_active[k] * (1 - self.o_active[k])
        for j in range(self.n_hidden):
            for k in range(self.n_output):
                change = o_deltas[k] * self.h_active[j]
                self.o_weight[j][k] += self.learning_rate * change
        h_deltas = [0.0] * self.n_hidden
        for j in range(self.n_hidden):
            error = 0.0
            for k in range(self.n_output):
                error += o_deltas[k] * self.o_weight[j][k]
            h_deltas[j] = error * self.h_active[j] * (1 - self.h_active[j])
        for i in range(self.n_input):
            for j in range(self.n_hidden):
                change = h_deltas[j] * self.i_active[i]
                self.i_weight[i][j] += self.learning_rate * change
    def test(self, patterns, s):
        t = self.update(patterns)
        if t == s:
            return s
        else:
            return -1
    def train(self, train_data):
        for i in range(0, len(train_data) / 2):
            l = map(int, train_data[i][2:])
            s = int(train_data[i][1])
            p = [l, [s]]
            targets = [0] * 4
            inputs = p[0]
            targets[s / 90] = 1
            self.update(inputs)
            self.backpropagate(targets)
    def tests(self, test_data):
        count = 0
        matrix = [[0 for x in range(4)] for x in range(4)]
        fl = open("nnet_output.txt", 'w')
        for i in range(0, len(test_data)):
            l = map(int, test_data[i][2:])
            s = int(test_data[i][1])
            p = [l, [s]]
            inputs = p[0]
            t = self.test(inputs, s)
            matrix[s / 90][t / 90] += 1
            orientation = test_data[i][0] + " " + test_data[i][1] + "\n"
            fl.write(orientation)
            if t == s:
                count += 1
        print "Percentage of Efficiency", float(count) / float(len(test_data)) * 100
        print "Confusion Matrix"
        for i in range(0, 4):
            print matrix[i]
    def knn(self, train_data, test_data, k):
        count = 0
        matrix = [[0 for x in range(4)] for x in range(4)]
        fl = open("knn_output.txt", 'w')
        for i in range(0, len(test_data)):
            t = list(test_data[i])
            orientation = self.knnd(train_data, t, k)
            if orientation == t[1]:
                count += 1
            matrix[int(t[1]) / 90][int(orientation) / 90] += 1
            orientation = t[0] + " " + orientation + "\n"
            fl.write(orientation)
        efficiency_percentage = float(count) / float(len(test_data)) * 100
        print "Percentage of Efficiency", efficiency_percentage
        print "Confusion Matrix"
        for i in range(0, 4):
            print matrix[i]