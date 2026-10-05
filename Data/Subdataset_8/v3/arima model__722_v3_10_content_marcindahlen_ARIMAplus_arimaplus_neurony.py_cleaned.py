import random
import math
class ArimaplusMath:
    @staticmethod
    def tanh(x):
        return math.tanh(x)
    @staticmethod
    def derivative_tanh(x):
        return 1 - math.tanh(x) ** 2
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    @staticmethod
    def derivative_sigmoid(x):
        sigmoid_x = ArimaplusMath.sigmoid(x)
        return sigmoid_x * (1 - sigmoid_x)
class SimpleNetwork:
    def __init__(self, window, neurony, forecast_type, arima):
        self.layers = len(neurony)
        self.topology = [[] for _ in range(self.layers)]
        for i, quantity in enumerate(neurony):
            for _ in range(quantity):
                if i == 0:
                    self.topology[i].append(SimpleNeuron(window))
                else:
                    self.topology[i].append(SimpleNeuron(neurony[i - 1]))
        if forecast_type == 1:
            self.topology.append([SimpleNeuron(neurony[-1]) for _ in range(window)])
        elif forecast_type in [4, 5]:
            self.topology.append([SimpleNeuron(neurony[-1])])
        elif forecast_type in [6, 7]:
            self.topology.append([SimpleNeuron(neurony[-1]) for _ in range(arima)])
        self.layers += 1
    def forward_pass(self, input=[]):
        self.output = []
        for i in range(self.layers):
            if i == 0:
                for neuron in self.topology[i]:
                    neuron.calculate(input)
            else:
                for neuron in self.topology[i]:
                    neuron.calculate([neuron.output for neuron in self.topology[i - 1]])
                    if i == self.layers - 1:
                        self.output.append(neuron.calculate([neuron.output for neuron in self.topology[i - 1]]))
        return self.output
    def backward_pass(self, target, learning_lambda, input=[]):
        print("simpleNetwork backward pass target:")
        print(target)
        for i in reversed(range(self.layers)):
            if i == self.layers - 1:
                if not isinstance(target, float):
                    for j, t in enumerate(target):
                        self.topology[i][j].learn(t, learning_lambda, [neuron.output for neuron in self.topology[i - 1]])
                else:
                    self.topology[i][0].learn(target, learning_lambda, [neuron.output for neuron in self.topology[i - 1]])
            elif i == 0:
                for neuron in self.topology[i]:
                    neuron.learn(SimpleNeuron.getMomentums(neuron, self.topology[i + 1]), learning_lambda, input)
            else:
                for neuron in self.topology[i]:
                    neuron.learn(SimpleNeuron.getMomentums(neuron, self.topology[i + 1]), learning_lambda,
                                 [neuron.output for neuron in self.topology[i - 1]])
class SimpleNeuron:
    def __init__(self, window):
        self.weights = [1 / random.randint(1, window) for _ in range(window)]
        self.bias_weight = 1 / random.randint(1, window)
        self.sum = 0
        self.bias = 1
        self.output = 0
    def calculate(self, input=[]):
        self.sum = sum(x * y for x, y in zip(self.weights, input)) + self.bias * self.bias_weight
        self.output = ArimaplusMath.tanh(self.sum)
        return self.output
    def learn(self, target, learning_lambda, input=[]):
        self.d_wagi = [target * ArimaplusMath.derivative_tanh(self.output) * input[i] for i in range(len(input))]
        self.weights = [w + learning_lambda * dw for w, dw in zip(self.weights, self.d_wagi)]
        self.bias_weight += target * ArimaplusMath.derivative_tanh(self.output) * self.bias * learning_lambda
    @staticmethod
    def getMomentums(neuron, neurons=[]):
        return sum(n.getWeightMomentum(neuron) for n in neurons)
    def getWeightMomentum(self, n):
        return self.d_wagi[n]
