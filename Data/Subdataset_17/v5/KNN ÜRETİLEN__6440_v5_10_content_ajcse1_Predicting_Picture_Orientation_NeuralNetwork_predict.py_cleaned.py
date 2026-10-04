import time
import math
import random
def create_matrix(rows, cols, fill=0.0):
    return [[fill] * cols for _ in range(rows)]
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
        self._set_input_activation(inputs)
        self._set_hidden_activation()
        self._set_output_activation()
        return self.oactive.index(max(self.oactive)) * 90
    def _set_input_activation(self, inputs):
        for i in range(self.ninput):
            self.iactive[i] = float(inputs[i]) / 255
    def _set_hidden_activation(self):
        for j in range(self.nhidden):
            sum_input = sum(self.iactive[i] * self.iweight[i][j] for i in range(self.ninput))
            self.hactive[j] = sum_input + self.bias
        self._normalize_and_activate(self.hactive)
    def _set_output_activation(self):
        for k in range(self.noutput):
            sum_hidden = sum(self.hactive[j] * self.oweight[j][k] for j in range(self.nhidden))
            self.oactive[k] = sum_hidden + self.bias
        self._normalize_and_activate(self.oactive)
    def backpropagate(self, targets, lrate):
        odeltas = self._calculate_output_deltas(targets)
        self._update_output_weights(odeltas, lrate)
        hdeltas = self._calculate_hidden_deltas(odeltas)
        self._update_input_weights(hdeltas, lrate)
    def _calculate_output_deltas(self, targets):
        odeltas = [0.0] * self.noutput
        for k in range(self.noutput):
            error = targets[k] - self.oactive[k]
            odeltas[k] = error * self.oactive[k] * (1 - self.oactive[k])
        return odeltas
    def _update_output_weights(self, odeltas, lrate):
        for j in range(self.nhidden):
            for k in range(self.noutput):
                change = odeltas[k] * self.hactive[j]
                self.oweight[j][k] += lrate * change
    def _calculate_hidden_deltas(self, odeltas):
        hdeltas = [0.0] * self.nhidden
        for j in range(self.nhidden):
            error = sum(odeltas[k] * self.oweight[j][k] for k in range(self.noutput))
            hdeltas[j] = error * self.hactive[j] * (1 - self.hactive[j])
        return hdeltas
    def _update_input_weights(self, hdeltas, lrate):
        for i in range(self.ninput):
            for j in range(self.nhidden):
                change = hdeltas[j] * self.iactive[i]
                self.iweight[i][j] += lrate * change
    def test(self, patterns, expected_class):
        prediction = self.update(patterns)
        return expected_class if prediction == expected_class else -1
    def train(self, train_data):
        for i in range(len(train_data)
            inputs = list(map(int, train_data[i][2:]))
            target_class = int(train_data[i][1])
            targets = [0] * 4
            targets[target_class
            self.update(inputs)
            self.backpropagate(targets, self.lrate)
    def tests(self, test_data):
        correct_count = 0
        confusion_matrix = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as output_file:
            for i in range(len(test_data)):
                inputs = list(map(int, test_data[i][2:]))
                expected_class = int(test_data[i][1])
                predicted_class = self.test(inputs, expected_class)
                confusion_matrix[expected_class
                orientation = f"{test_data[i][0]} {test_data[i][1]}\n"
                output_file.write(orientation)
                if predicted_class == expected_class:
                    correct_count += 1
        accuracy = (correct_count / float(len(test_data))) * 100
        print("Percentage of Efficiency:", accuracy)
        print("Confusion Matrix")
        for row in confusion_matrix:
            print(row)
    def knnd(self, train_data, test_data, k):
        distances = [float('inf')] * k
        nearest_neighbors = [None] * k
        test_inputs = list(test_data[2:])
        for j in range(len(train_data)
            distance = sum(abs(float(test_inputs[i]) - float(train_data[j][i + 2])) for i in range(192))
            max_distance = max(distances)
            if distance < max_distance:
                max_index = distances.index(max_distance)
                distances[max_index] = float(distance)
                nearest_neighbors[max_index] = j
        orientations = [train_data[n][1] for n in nearest_neighbors if n is not None]
        orientation_count = {orientation: orientations.count(orientation) for orientation in set(orientations)}
        return max(orientation_count, key=orientation_count.get)
    def knn(self, train_data, test_data, k):
        correct_count = 0
        confusion_matrix = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as output_file:
            for test_instance in test_data:
                expected_class = int(test_instance[1])
                predicted_class = int(self.knnd(train_data, test_instance, k))
                confusion_matrix[expected_class
                orientation = f"{test_instance[0]} {predicted_class}\n"
                output_file.write(orientation)
                if predicted_class == expected_class:
                    correct_count += 1
        accuracy = (correct_count / float(len(test_data))) * 100
        print("Percentage of Efficiency:", accuracy)
        print("Confusion Matrix")
        for row in confusion_matrix:
            print(row)
    def _normalize_and_activate(self, values):
        max_val = max(values)
        min_val = min(values)
        for i in range(len(values)):
            values[i] = (values[i] - min_val)```python
            values[i] = (values[i] - min_val) / (max_val - min_val)
            values[i] = 1 / (1 + math.exp(-values[i]))
if __name__ == '__main__':
    ni = 192
    nh = 16
    no = 4
    lr = 0.01
    model = Predict(ni, nh, no, lr)
    train_data = [
    ]
    test_data = [
    ]
    model.train(train_data)
    model.tests(test_data)
    k = 5
    model.knn(train_data, test_data, k)