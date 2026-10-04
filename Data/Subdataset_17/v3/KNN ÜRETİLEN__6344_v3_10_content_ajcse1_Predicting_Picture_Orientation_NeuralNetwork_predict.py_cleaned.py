import math
import random
def create_matrix(rows, cols, fill=0.0):
    return [[fill] * cols for _ in range(rows)]
class Predict:
    def __init__(self, num_inputs, num_hidden, num_outputs, learning_rate):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs
        self.learning_rate = learning_rate
        self.bias = 1.0
        self.input_activations = [1.0] * num_inputs
        self.hidden_activations = [1.0] * num_hidden
        self.output_activations = [1.0] * num_outputs
        self.input_weights = create_matrix(num_inputs, num_hidden)
        self.output_weights = create_matrix(num_hidden, num_outputs)
        self._initialize_weights()
    def _initialize_weights(self):
        for i in range(self.num_inputs):
            for j in range(self.num_hidden):
                self.input_weights[i][j] = random.uniform(0, 1)
        for j in range(self.num_hidden):
            for k in range(self.num_outputs):
                self.output_weights[j][k] = random.uniform(0, 1)
    def update(self, inputs):
        self._activate_input_layer(inputs)
        self._activate_hidden_layer()
        self._activate_output_layer()
        max_output = max(self.output_activations)
        return self.output_activations.index(max_output) * 90
    def _activate_input_layer(self, inputs):
        self.input_activations = [float(inputs[i]) / 255.0 for i in range(self.num_inputs)]
    def _activate_hidden_layer(self):
        for j in range(self.num_hidden):
            total = sum(self.input_activations[i] * self.input_weights[i][j] for i in range(self.num_inputs))
            total += self.bias
            self.hidden_activations[j] = self._sigmoid(total)
    def _activate_output_layer(self):
        for k in range(self.num_outputs):
            total = sum(self.hidden_activations[j] * self.output_weights[j][k] for j in range(self.num_hidden))
            total += self.bias
            self.output_activations[k] = self._sigmoid(total)
    @staticmethod
    def _sigmoid(x):
        return 1 / (1 + math.exp(-x))
    def backpropagate(self, targets):
        output_deltas = self._calculate_output_deltas(targets)
        self._update_output_weights(output_deltas)
        hidden_deltas = self._calculate_hidden_deltas(output_deltas)
        self._update_input_weights(hidden_deltas)
    def _calculate_output_deltas(self, targets):
        return [
            (targets[k] - self.output_activations[k]) * self.output_activations[k] * (1 - self.output_activations[k])
            for k in range(self.num_outputs)
        ]
    def _update_output_weights(self, output_deltas):
        for j in range(self.num_hidden):
            for k in range(self.num_outputs):
                change = output_deltas[k] * self.hidden_activations[j]
                self.output_weights[j][k] += self.learning_rate * change
    def _calculate_hidden_deltas(self, output_deltas):
        return [
            sum(output_deltas[k] * self.output_weights[j][k] for k in range(self.num_outputs)) * self.hidden_activations[j] * (1 - self.hidden_activations[j])
            for j in range(self.num_hidden)
        ]
    def _update_input_weights(self, hidden_deltas):
        for i in range(self.num_inputs):
            for j in range(self.num_hidden):
                change = hidden_deltas[j] * self.input_activations[i]
                self.input_weights[i][j] += self.learning_rate * change
    def test(self, patterns, expected):
        predicted = self.update(patterns)
        return expected if predicted == expected else -1
    def train(self, train_data):
        for data in train_data:
            inputs = list(map(int, data[2:]))
            target_class = int(data[1])
            targets = [0] * self.num_outputs
            targets[target_class
            self.update(inputs)
            self.backpropagate(targets)
    def tests(self, test_data):
        correct_count = 0
        confusion_matrix = create_matrix(4, 4, 0)
        with open("nnet_output.txt", 'w') as file:
            for data in test_data:
                inputs = list(map(int, data[2:]))
                expected_class = int(data[1])
                predicted_class = self.test(inputs, expected_class)
                confusion_matrix[expected_class
                file.write(f"{data[0]} {predicted_class}\n")
                if predicted_class == expected_class:
                    correct_count += 1
        efficiency = float(correct_count) / float(len(test_data)) * 100
        print(f"Percentage of Efficiency: {efficiency}")
        print("Confusion Matrix")
        for row in confusion_matrix:
            print(row)
    def knnd(self, train_data, test_data, k):
        k_distances = [float('inf')] * k
        k_indexes = [None] * k
        test_inputs = list(map(float, test_data[2:]))
        for i, train_sample in enumerate(train_data):
            train_inputs = list(map(float, train_sample[2:]))
            distance = sum(abs(test_inputs[x] - train_inputs[x]) for x in range(len(test_inputs)))
            max_distance = max(k_distances)
            if distance < max_distance:
                max_index = k_distances.index(max_distance)
                k_distances[max_index] = distance
                k_indexes[max_index] = i
        predictions = [train_data[idx][1] for idx in k_indexes if idx is not None]
        most_common = max(set(predictions), key=predictions.count)
        return most_common
    def knn(self, train_data, test_data, k):
        correct_count = 0
        confusion_matrix = create_matrix(4, 4, 0)
        with open("knn_output.txt", 'w') as file:
            for data in test_data:
                predicted_class = self.knnd(train_data, data, k)
                expected_class = data[1]
                confusion_matrix[int(expected_class)
                file.write(f"{data[0]} {predicted_class}\n")
                if predicted_class == expected_class:
                    correct_count += 1
        efficiency = float(correct```python
count) / float(len(test_data)) * 100
        print(f"Percentage of Efficiency: {efficiency}")
        print("Confusion Matrix")
        for row in confusion_matrix:
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