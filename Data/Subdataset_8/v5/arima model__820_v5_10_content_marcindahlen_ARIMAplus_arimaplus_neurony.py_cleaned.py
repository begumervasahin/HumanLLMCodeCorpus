import arimaplus_math
import random
class SimpleNetwork:
    def __init__(self, window, neurons, forecast_type, arima):
        self.layers = len(neurons)
        self.neuron_layers = [[] for _ in range(self.layers)]
        for i in range(self.layers):
            quantity = neurons[i]
            for _ in range(quantity):
                if i == 0:
                    self.neuron_layers[i].append(SimpleNeuron(window))
                else:
                    self.neuron_layers[i].append(SimpleNeuron(neurons[i - 1]))
        if forecast_type in [1, 4, 5, 6, 7]:
            self.neuron_layers.append([SimpleNeuron(neurons[-1]) for _ in range(window if forecast_type == 1 else arima)])
            self.layers += 1
    def forward_pass(self, input=[]):
        self.output = []
        for i in range(self.layers):
            if i == 0:
                for neuron in self.neuron_layers[i]:
                    neuron.calculate(input)
            else:
                for neuron in self.neuron_layers[i]:
                    neuron.calculate([n.output for n in self.neuron_layers[i - 1]])
                    if i == self.layers - 1:
                        self.output.append(neuron.calculate([n.output for n in self.neuron_layers[i - 1]]))
        return self.output
    def backward_pass(self, target, learning_lambda, input=[]):
        for i in reversed(range(self.layers)):
            if i == self.layers - 1:
                for j, target_val in enumerate(target):
                    self.neuron_layers[i][j].learn(target_val, learning_lambda, [n.output for n in self.neuron_layers[i - 1]])
            elif i == 0:
                for neuron in self.neuron_layers[i]:
                    neuron.learn(sum([n.get_momentums(j, self.neuron_layers[i + 1]) for j in range(len(self.neuron_layers[i + 1]))]), learning_lambda, input)
            else:
                for neuron in self.neuron_layers[i]:
                    neuron.learn(sum([n.get_momentums(j, self.neuron_layers[i + 1]) for j in range(len(self.neuron_layers[i + 1]))]), learning_lambda, [n.output for n in self.neuron_layers[i - 1]])
class SimpleNeuron:
    def __init__(self, window):
        self.weights = []
        self.sum = 0
        self.bias = 1
        for _ in range(window):
            self.weights.append(1 / random.randint(1, window))
        self.bias_weight = 1 / random.randint(1, window)
        self.output = 0
    def calculate(self, input=[]):
        self.sum = sum(x * y for x, y in zip(self.weights, input)) + self.bias * self.bias_weight
        self.output = arimaplus_math.tanh(self.sum)
        return self.output
    def learn(self, target, learning_lambda, input=[]):
        self.delta_weights = [0] * len(input)
        for i in range(len(input)):
            self.delta_weights[i] = target * arimaplus_math.derivative_tanh(self.output) * input[i]
            self.weights[i] += learning_lambda * self.delta_weights[i]
        self.bias_weight += target * arimaplus_math.derivative_tanh(self.output) * self.bias * learning_lambda
    def get_momentums(self, which_neuron, neurons=[]):
        momentums = 0
        for n in neurons:
            momentums += n.get_weight_momentum(which_neuron)
        return momentums
    def get_weight_momentum(self, n):
        return self.delta_weights[n]
class LSTMNetwork:
    def __init__(self, window, neurons, forecast_type, arima):
        self.layers = len(neurons)
        self.neuron_layers = [[] for _ in range(self.layers)]
        for i in range(self.layers):
            quantity = neurons[i]
            for _ in range(quantity):
                if i == 0:
                    self.neuron_layers[i].append(LSTMNeuron(window))
                else:
                    self.neuron_layers[i].append(LSTMNeuron(neurons[i - 1]))
        if forecast_type in [1, 4, 5, 6, 7]:
            self.neuron_layers.append([LSTMNeuron(neurons[-1]) for _ in range(window if forecast_type == 1 else arima)])
            self.layers += 1
    def forward_pass(self, input=[]):
        self.output = []
        for i in range(self.layers):
            if i == 0:
                for neuron in self.neuron_layers[i]:
                    neuron.calculate(input)
            else:
                for neuron in self.neuron_layers[i]:
                    neuron.calculate([n.output for n in self.neuron_layers[i - 1]])
                    if i == self.layers - 1:
                        self.output.append(neuron.calculate([n.output for n in self.neuron_layers[i - 1]]))
    def backward_pass(self, target, learning_lambda, input=[]):
        for i in reversed(range(self.layers)):
            if i == self.layers - 1:
                for j, target_val in enumerate(target):
                    self.neuron_layers[i][j].learn(target_val, learning_lambda, [n.output for n in self.neuron_layers[i - 1]])
            elif i == 0:
                for neuron in self.neuron_layers[i]:
                    neuron.learn(sum([n.get_momentums(j, self.neuron_layers[i + 1]) for j in range(len(self.neuron_layers[i + 1]))]), learning_lambda, input)
            else:
                for neuron in self.neuron_layers[i]:
                    neuron.learn(sum([n.get_momentums(j, self.neuron_layers[i + 1]) for j in range(len(self.neuron_layers[i + 1]))]), learning_lambda, [n.output for n in self.neuron_layers[i - 1]])
class LSTMNeuron:
    def __init__(self, window):
        self.weights = [[] for _ in range(4)]
        self.bias_weights = []
        self.sum_in, self.sum_out, self.sum_mem, self.sum_forget = 0, 0, 0, 0
        self.y_in, self.y_forget, self.state, self.y_out = 0, 0, 0, 0
        self.bias_in, self.bias_out, self.bias_forget, self.bias_mem = 1, 1, 1, 1
        self.mem = 0
        self.output = 0
        for _ in range(4):
            for _ in range(window):
                self.weights[_].append(1 / random.randint(1, 4 * window))
            self.bias_weights.append(1 / random.randint(1, 4 * window))
        self.prev_output = 0
        self.prev_weight = 1 / random.randint(1, 4 * window)
    def calculate(self, input=[]):
        self.prev_output = self.output
        self.state = self.mem
        self.sum_in = sum(input[i] * self.weights[0][i] for i in range(len(input))) + self.bias_in * self.bias_weights[0]
        self.y_in = arimaplus_math.sigmoid(self.sum_in)
        self.sum_forget = sum(input[i] * self.weights[1][i] for i in range(len(input))) + self.bias_forget * self.bias_weights[1]
        self.y_forget = arimaplus_math.sigmoid(self.sum_forget)
        self.sum_mem = sum(input[i] * self.weights[2][i] for i in range(len(input))) + self.bias_mem * self.bias_weights[2] + self.prev_output * self.prev_weight
        self.mem = self.y_forget * self.state + self.y_in * arimaplus_math.tanh(self.sum_mem)
        self.sum_out = sum(input[i] * self.weights[3][i] for i in range(len(input))) + self.bias_out * self.bias_weights[3]
        self.y_out = arimaplus_math.sigmoid(self.sum_out)
        self.output = arimaplus_math.tanh(self.mem) * self.y_out
        return self.output
    def learn(self, target, learning_lambda, input=[]):
        self.delta_weights = [[] for _ in range(4)]
        for _ in range(4):
            for _ in range(len(input)):
                self.delta_weights[_].append(0)
        for i in range(len(input)):
            self.delta_weights[0][i] = target * self.y_out * arimaplus_math.derivative_tanh(self.mem) * self.y_forget * arimaplus_math.derivative_tanh(self.sum_mem) * arimaplus_math.derivative_sigmoid(self.sum_in) * input[i]
            self.delta_weights[1][i] = target * self.y_out * arimaplus_math.derivative_tanh(self.mem) * self.y_in * arimaplus_math.derivative_tanh(self.sum_mem) * arimaplus_math.derivative_sigmoid(self.sum_forget) * input[i]
            self.delta_weights[2][i] = target * self.y_out * arimaplus_math.derivative_tanh(self.mem) * self.y_forget * self.y_in * arimaplus_math.derivative_tanh(self.sum_mem) * input[i]
            self.delta_weights[3][i] = target * arimaplus_math.derivative_tanh(self.mem) * arimaplus_math.derivative_sigmoid(self.sum_out) * input[i]
        self.bias_weights[0] += learning_lambda * target * self.y_out * arimaplus_math.derivative_tanh(self.mem) * self.y_forget * arimaplus_math.derivative_tanh(self.sum_mem) * arimaplus_math.derivative_sigmoid(self.sum_in) * self.bias_in
        self.bias_weights[1] += learning_lambda * target * self.y_out * arimaplus_math.derivative_tanh(self.mem) * self.y_in * arimaplus_math.derivative_tanh(self.sum_mem) * arimaplus_math.derivative_sigmoid(self.sum_forget) * self.bias_out
        self.bias_weights[2] += learning_lambda * target * self.y_out * arimaplus_math.derivative_tanh(self.mem) * self.y_forget * self.y_in * arimaplus_math.derivative_tanh(self.sum_mem) * self.bias_mem
        self.bias_weights[3] += learning_lambda * target * arimaplus_math.derivative_tanh(self.mem) * arimaplus_math.derivative_sigmoid(self.sum_out) * self.bias_forget
        self.prev_weight += learning_lambda * target * self.y_out * arimaplus_math.derivative_tanh(self.mem) * self.y_forget * self.y_in * arimaplus_math.derivative_tanh(self.sum_mem) * self.prev_output
        for i in range(len(input)):
            self.weights[0][i] += learning_lambda * self.delta_weights[0][i]
            self.weights[1][i] += learning_lambda * self.delta_weights[1][i]
            self.weights[2][i] += learning_lambda * self.delta_weights[2][i]
            self.weights[3][i] += learning_lambda * self.delta_weights[3][i]
class GRUNetwork:
    def __init__(self, window, neurons, forecast_type, arima):
        self.layers = len(neurons)
        self.neuron_layers = [[] for _ in range(self.layers)]
        for i in range(self.layers):
            quantity = neurons[i]
            for _ in range(quantity):
                if i == 0:
                    self.neuron_layers[i].append(GRUNeuron(window))
                else:
                    self.neuron_layers[i].append(GRUNeuron(neurons[i - 1]))
        if forecast_type in [1, 4, 5, 6, 7]:
            self.neuron_layers.append([GRUNeuron(neurons[-1]) for _ in range(window if forecast_type == 1 else arima)])
            self.layers += 1
    def forward_pass(self, input=[]):
        self.output = []
        for i in range(self.layers):
            if i == 0:
                for neuron in self.neuron_layers[i]:
                    neuron.calculate(input)
            else:
                for neuron in self.neuron_layers[i]:
                    neuron.calculate([n.output for n in self.neuron_layers[i - 1]])
                    if i == self.layers - 1:
                        self.output.append(neuron.calculate([n.output for n in self.neuron_layers[i - 1]]))
    def backward_pass(self, target, learning_lambda, input=[]):
        for i in reversed(range(self.layers)):
            if i == self.layers - 1:
                for j, target_val in enumerate(target):
                    self.neuron_layers[i][j].learn(target_val, learning_lambda, [n.output for n in self.neuron_layers[i - 1]])
            elif i == 0:
                for neuron in self.neuron_layers[i]:
                    neuron.learn(sum([n.get_momentums(j, self.neuron_layers[i + 1]) for j in range(len(self.neuron_layers[i + 1]))]), learning_lambda, input)
            else:
                for neuron in self.neuron_layers[i]:
                    neuron.learn(sum([n.get_momentums(j, self.neuron_layers[i + 1]) for j in range(len(self.neuron_layers[i + 1]))]), learning_lambda, [n.output for n in self.neuron_layers[i - 1]])
class GRUNeuron:
    def __init__(self, window):
        self.weights = [[] for _ in range(3)]
        self.bias_weights = []
        self.sum_zt, self.sum_rt, self.sum_we = 0, 0, 0
        self.y_zt, self.y_rt, self.y_we = 0, 0, 0
        self.bias_zt, self.bias_rt, self.bias_we = 1, 1, 1
        self.output = 0
        self.bias = 1
        for _ in range(3):
            for _ in range(window):
                self.weights[_].append(1 / random.randint(1, 3 * window))
            self.bias_weights.append(1 / random.randint(1, 3 * window))
        self.prev_output = 0
        self.input_weight = 1 / random.randint(1, 4 * window)
    def calculate(self, input=[]):
        self.prev_output = self.output
        self.sum_zt = sum(input[i] * self.weights[0][i] for i in range(len(input))) + self.prev_output * self.input_weight + self.bias_zt * self.bias_weights[0]
        self.y_zt = arimaplus_math.sigmoid(self.sum_zt)
        self.sum_rt = sum(input[i] * self.weights[1][i] for i in range(len(input))) + self.prev_output * self.input_weight + self.bias_rt * self.bias_weights[1]
        self.y_rt = arimaplus_math.sigmoid(self.sum_rt)
        self.sum_we = sum(input[i] * self.weights[2][i] for i in range(len(input))) + self.prev_output * self.input_weight * self.y_rt + self.bias_we * self.bias_weights[2]
        self.y_we = arimaplus_math.tanh(self.sum_we)
        self.output = (1 - self.y_zt) * self.prev_output + self.y_zt * self.y_we
        return self.output
    def learn(self, target, learning_lambda, input=[]):
        self.delta_weights = [[] for _ in range(3)]
        for _ in range(3):
            for _ in range(len(input)):
                self.delta_weights[_].append(0)
        for i in range(len(input)):
            self.delta_weights[0][i] = input[i] * (-1 * arimaplus_math.derivative_sigmoid(self.sum_zt)) * (self.y_we * target + self.prev_output * target)
            self.delta_weights[1][i] = input[i] * arimaplus_math.derivative_sigmoid(self.sum_rt) * arimaplus_math.derivative_tanh(self.sum_we) * target * (1 - self.y_zt)
            self.delta_weights[2][i] = input[i] * arimaplus_math.derivative_tanh(self.sum_we) * target * (1 - self.y_zt)
        self.input_weight += learning_lambda * self.prev_output * (-1 * arimaplus_math.derivative_sigmoid(self.sum_zt)) * (self.y_we * target + self.prev_output * target)
        self.bias_weights[0] += learning_lambda * self.bias_zt * (-1 * arimaplus_math.derivative_sigmoid(self.sum_zt)) * (self.y_we * target + self.prev_output * target)
        self.bias_weights[1] += learning_lambda * self.bias_rt * arimaplus_math.derivative_sigmoid(self.sum_rt) * arimaplus_math.derivative_tanh(self.sum_we) * target * (1 - self.y_zt)
        self.bias_weights[2] += learning_lambda * self.bias_we * arimaplus_math.derivative_tanh(self.sum_we) * target * (1 - self.y_zt)
        for i in range(len(input)):
            self.weights[0][i] += learning_lambda * self.delta_weights[0][i]
            self.weights[1][i] += learning_lambda * self.delta_weights[1][i]
            self.weights[2][i] += learning_lambda * self.delta_weights[2][i]
    def get_momentums(self, which_neuron, neurons=[]):
        momentums = 0
        for n in neurons:
            momentums += n.get_weight_momentum(which_neuron)
        return momentums
    def get_weight_momentum(self, n):
        return self.delta_weights[n]