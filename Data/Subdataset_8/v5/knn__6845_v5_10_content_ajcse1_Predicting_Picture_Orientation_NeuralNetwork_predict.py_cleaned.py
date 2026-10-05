import random
import math
class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.n_input = int(input_nodes)
        self.n_hidden = int(hidden_nodes)
        self.n_output = int(output_nodes)
        self.learning_rate = float(learning_rate)
        self.i_active = [1.0] * self.n_input
        self.h_active = [1.0] * self.n_hidden
        self.o_active = [1.0] * self.n_output
        self.i_weight = self._initialize_weights(self.n_input, self.n_hidden)
        self.o_weight = self._initialize_weights(self.n_hidden, self.n_output)
        self.bias = 1.0
    def _initialize_weights(self, rows, cols):
        return [[random.uniform(0, 1) for _ in range(cols)] for _ in range(rows)]
    def _sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    def _forward_propagation(self):
        for j in range(self.n_hidden):
            sum_ = sum(self.i_active[i] * self.i_weight[i][j] for i in range(self.n_input))
            sum_ += self.bias
            self.h_active[j] = sum_
            self.h_active[j] = self._sigmoid(self.h_active[j])
        for k in range(self.n_output):
            sum_ = sum(self.h_active[j] * self.o_weight[j][k] for j in range(self.n_hidden))
            self.o_active[k] = sum_ + self.bias
    def _backward_propagation(self, targets):
        o_deltas = [(targets[k] - self.o_active[k]) * self.o_active[k] * (1 - self.o_active[k]) for k in range(self.n_output)]
        for j in range(self.n_hidden):
            for k in range(self.n_output):
                self.o_weight[j][k] += self.learning_rate * o_deltas[k] * self.h_active[j]
        h_deltas = [sum(o_deltas[k] * self.o_weight[j][k] for k in range(self.n_output)) * self.h_active[j] * (1 - self.h_active[j]) for j in range(self.n_hidden)]
        for i in range(self.n_input):
            for j in range(self.n_hidden):
                self.i_weight[i][j] += self.learning_rate * h_deltas[j] * self.i_active[i]
    def train(self, train_data):
        for data in train_data:
            inputs = map(int, data[2:])
            targets = [0] * self.n_output
            targets[int(data[1])
            self.i_active = [float(i) / 255 for i in inputs]
            self._forward_propagation()
            self._backward_propagation(targets)
    def _predict_orientation(self, inputs):
        self.i_active = [float(i) / 255 for i in inputs]
        self._forward_propagation()
        return self.o_active.index(max(self.o_active)) * 90
    def test(self, test_data):
        count = 0
        confusion_matrix = [[0 for _ in range(4)] for _ in range(4)]
        with open("nnet_output.txt", 'w') as f_out:
            for data in test_data:
                inputs = map(int, data[2:])
                predicted_orientation = self._predict_orientation(inputs)
                actual_orientation = int(data[1])
                f_out.write(data[0] + " " + str(predicted_orientation) + "\n")
                if predicted_orientation == actual_orientation:
                    count += 1
                confusion_matrix[actual_orientation
        efficiency_percentage = float(count) / float(len(test_data)) * 100
        print("Percentage of Efficiency:", efficiency_percentage)
        print("Confusion Matrix:")
        for row in confusion_matrix:
            print(row)
    def knn(self, train_data, test_data, k):
        count = 0
        confusion_matrix = [[0 for _ in range(4)] for _ in range(4)]
        with open("knn_output.txt", 'w') as f_out:
            for data in test_data:
                inputs = list(map(int, data))
                predicted_orientation = self._knn(train_data, inputs, k)
                actual_orientation = inputs[1]
                f_out.write(data[0] + " " + str(predicted_orientation) + "\n")
                if predicted_orientation == actual_orientation:
                    count += 1
                confusion_matrix[actual_orientation
        efficiency_percentage = float(count) / float(len(test_data)) * 100
        print("Percentage of Efficiency:", efficiency_percentage)
        print("Confusion Matrix:")
        for row in confusion_matrix:
            print(row)
    def _knn(self, train_data, test_instance, k):
        distances = []
        for train_instance in train_data:
            dist = self._euclidean_distance(train_instance[2:], test_instance[2:])
            distances.append((train_instance[1], dist))
        distances.sort(key=lambda x: x[1])
        neighbors = distances[:k]
        class_votes = {90: 0, 180: 0, 270: 0, 360: 0}
        for neighbor in neighbors:
            class_votes[neighbor[0]] += 1
        return max(class_votes.items(), key=lambda x: x[1])[0]
    @staticmethod
    def _euclidean_distance(instance1, instance2):
        return math.sqrt(sum((float(instance1[i]) - float(instance2[i])) ** 2 for i in range(len(instance1))))
def create_matrix(rows, cols, fill=0.0):
    return [[fill] * cols for _ in range(rows)]
def main():
    pass
if __name__ == "__main__":
    main()