import numpy as np
from scipy.special import expit as sigmoid
import random
import dill
class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.lr = learning_rate
        self.weight_input_hidden = np.random.rand(self.hidden_nodes, self.input_nodes) - 0.5
        self.weight_hidden_output = np.random.rand(self.output_nodes, self.hidden_nodes) - 0.5
    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        hidden_inputs = np.dot(self.weight_input_hidden, inputs)
        hidden_outputs = sigmoid(hidden_inputs)
        final_inputs = np.dot(self.weight_hidden_output, hidden_outputs)
        final_outputs = sigmoid(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.weight_hidden_output.T, output_errors)
        self.weight_hidden_output += self.lr * np.dot(output_errors * final_outputs * (1.0 - final_outputs),
                                                       np.transpose(hidden_outputs))
        self.weight_input_hidden += self.lr * np.dot(hidden_errors * hidden_outputs * (1.0 - hidden_outputs),
                                                      np.transpose(inputs))
    def predict(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_inputs = np.dot(self.weight_input_hidden, inputs)
        hidden_outputs = sigmoid(hidden_inputs)
        final_inputs = np.dot(self.weight_hidden_output, hidden_outputs)
        final_outputs = sigmoid(final_inputs)
        return final_outputs
def train_neural_net():
    input_nodes = 784
    hidden_nodes = 1500
    output_nodes = 26
    learning_rate = 0.005
    neural_net = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    with open("/Users/Nikita/PycharmProjects/FYPPuzzle/static/trainFinal.csv", 'r') as training_data:
        full_training = training_data.readlines()
        random.shuffle(full_training)
        test_list = full_training[0:8000]
        training_list = full_training[0:]
    for epoch in range(50):
        for record in training_list:
            all_values = record.split(',')
            linew = record.split(",")[0]
            joined = int(linew.split("e0")[1]) - 10
            all_values[0] = joined
            inputs = (np.asfarray(all_values[1:]) / 255 * 0.99) + 0.01
            targets = np.zeros(output_nodes) + 0.01
            targets[joined - 1] = 0.99
            neural_net.train(inputs, targets)
    print("Neural network trained")
    with open('/Users/Nikita/PycharmProjects/FYPPuzzle/static/nn.dill', 'wb') as f:
        dill.dump(neural_net, f)
train_neural_net()