from __future__ import division
import numpy
import scipy.special
import random
import dill
class neuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.lr = learning_rate
        self.weight_input_hidden = (numpy.random.rand(self.hidden_nodes, self.input_nodes) - 0.5)
        self.weight_hidden_output = (numpy.random.rand(self.output_nodes, self.hidden_nodes) - 0.5)
        self.activation_function = lambda x: scipy.special.expit(x)
    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.weight_input_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.weight_hidden_output, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.weight_hidden_output.T, output_errors)
        self.weight_hidden_output += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                                         numpy.transpose(hidden_outputs))
        self.weight_input_hidden += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                                        numpy.transpose(inputs))
    def predict(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.weight_input_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.weight_hidden_output, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
def trainNeuralNet():
    input_nodes = 784
    hidden_nodes = 1500
    output_nodes = 26
    learning_rate = 0.005
    neural = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    training_data = open("/Users/Nikita/PycharmProjects/FYPPuzzle/static/trainFinal.csv", 'r')
    full_training = training_data.readlines()
    random.shuffle(full_training)
    test_list = full_training[0:8000]
    training_list = full_training[0:]
    training_data.close()
    for epoch in range(50):
        for record in training_list:
            all_values = record.split(',')
            linew = record.split(",")[0]
            joined = int(linew.split("e0")[1]) - 10
            all_values[0] = joined
            inputs = (numpy.asfarray(all_values[1:]) / 255 * 0.99) + 0.01
            targets = numpy.zeros(output_nodes) + 0.01
            targets[joined - 1] = 0.99
            neural.train(inputs, targets)
    print("trained")
    with open('/Users/Nikita/PycharmProjects/FYPPuzzle/static/nn.dill', 'wb') as f:
        dill.dump(neural, f)
trainNeuralNet()