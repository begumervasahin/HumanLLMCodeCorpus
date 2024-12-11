import random
import math
class class1:
    @staticmethod
    def fonk1(x):
        return math.fonk1(x)
    @staticmethod
    def fonk2(x):
        return 1 - math.fonk1(x) ** 2
    @staticmethod
    def fonk3(x):
        return 1 / (1 + math.exp(-x))
    @staticmethod
    def fonk4(x):
        b1 = class1.fonk3(x)
        return b1 * (1 - b1)
class class2:
    def fonk5(self, window, neurony, b5, arima):
        self.b2 = len(neurony)
        self.b3 = [[] for _ in range(self.b2)]
        for b4, quantity in enumerate(neurony):
            for _ in range(quantity):
                if b4 = = 0:
                    self.b3[b4].append(class3(window))
                else:
                    self.b3[b4].append(class3(neurony[b4 - 1]))
        if b5 = = 1:
            self.b3.append([class3(neurony[-1]) for _ in range(window)])
        elif b5 in [4, 5]:
            self.b3.append([class3(neurony[-1])])
        elif b5 in [6, 7]:
            self.b3.append([class3(neurony[-1]) for _ in range(arima)])
        self.b2 += 1
    def fonk6(self, b6 = []):
        self.b7 = []
        for b4 in range(self.b2):
            if b4 = = 0:
                for neuron in self.b3[b4]:
                    neuron.fonk9(b6)
            else:
                for neuron in self.b3[b4]:
                    neuron.fonk9([neuron.b7 for neuron in self.b3[b4 - 1]])
                    if b4 = = self.b2 - 1:
                        self.b7.append(neuron.fonk9([neuron.b7 for neuron in self.b3[b4 - 1]]))
        return self.b7
    def fonk7(self, target, learning_lambda, b6 = []):
        print("simpleNetwork backward pass target:")
        print(target)
        for b4 in reversed(range(self.b2)):
            if b4 = = self.b2 - 1:
                if not isinstance(target, float):
                    for j, t in enumerate(target):
                        self.b3[b4][j].fonk10(t, learning_lambda, [neuron.b7 for neuron in self.b3[b4 - 1]])
                else:
                    self.b3[b4][0].fonk10(target, learning_lambda, [neuron.b7 for neuron in self.b3[b4 - 1]])
            elif b4 = = 0:
                for neuron in self.b3[b4]:
                    neuron.fonk10(class3.fonk11(neuron, self.b3[b4 + 1]), learning_lambda, b6)
            else:
                for neuron in self.b3[b4]:
                    neuron.fonk10(class3.fonk11(neuron, self.b3[b4 + 1]), learning_lambda,
                                 [neuron.b7 for neuron in self.b3[b4 - 1]])
class class3:
    def fonk8(self, window):
        self.b8 = [1 / random.randint(1, window) for _ in range(window)]
        self.b9 = 1 / random.randint(1, window)
        self.a1 = 0
        self.a2 = 1
        self.b7 = 0
    def fonk9(self, b6 = []):
        self.a1 = a1(x * y for x, y in zip(self.b8, b6)) + self.a2 * self.b9
        self.b7 = class1.fonk1(self.a1)
        return self.b7
    def fonk10(self, target, learning_lambda, b6 = []):
        self.b10 = [target * class1.fonk2(self.b7) * b6[b4] for b4 in range(len(b6))]
        self.b8 = [w + learning_lambda * dw for w, dw in zip(self.b8, self.b10)]
        self.b9 += target * class1.fonk2(self.b7) * self.a2 * learning_lambda
    @staticmethod
    def fonk11(neuron, b11 = []):
        return a1(n.fonk12(neuron) for n in b11)
    def fonk12(self, n):
        return self.b10[n]
