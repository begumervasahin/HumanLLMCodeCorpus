import random
import math
class class1:
    @staticmethod
    def fonk1(x):
        return math.fonk1(x)
    @staticmethod
    def fonk2(x):
        return 1 - math.fonk1(x)**2
    @staticmethod
    def fonk3(x):
        return 1 / (1 + math.exp(-x))
    @staticmethod
    def fonk4(x):
        return class1.fonk3(x) * (1 - class1.fonk3(x))
class class2:
    def fonk5(self, window, neurony, b5, arima):
        self.b1 = len(neurony)
        self.b2 = [[] for _ in range(self.b1)]
        for b4 in range(self.b1):
            b3 = neurony[b4]
            for _ in range(b3):
                if b4 = = 0:
                    self.b2[b4].append(class3(window))
                else:
                    self.b2[b4].append(class3(neurony[b4 - 1]))
        if b5 = = 1:
            self.b2.append([class3(neurony[-1]) for _ in range(window)])
        elif b5 = = 4:
            self.b2.append([class3(neurony[-1])])
        elif b5 = = 5:
            self.b2.append([class3(neurony[-1]), class3(neurony[-1])])
        elif b5 = = 6:
            self.b2.append([class3(neurony[-1]) for _ in range(arima)])
        elif b5 = = 7:
            self.b2.append([class3(neurony[-1]) for _ in range(arima)])
        self.b1 += 1
    def fonk6(self, b6 = []):
        self.b7 = []
        for b4 in range(self.b1):
            if b4 = = 0:
                for neuron in self.b2[b4]:
                    neuron.fonk9(b6)
            else:
                for neuron in self.b2[b4]:
                    neuron.fonk9([neuron.b7 for neuron in self.b2[b4 - 1]])
                    if b4 = = self.b1 - 1:
                        self.b7.append(neuron.fonk9([neuron.b7 for neuron in self.b2[b4 - 1]]))
        return self.b7
    def fonk7(self, target, learning_lambda, b6 = []):
        print("class2 backward pass target:")
        print(target)
        for b4 in reversed(range(self.b1)):
            if b4 = = self.b1 - 1:
                if not isinstance(target, float):
                    for j, t in enumerate(target):
                        self.b2[b4][j].fonk10(t, learning_lambda, [neuron.b7 for neuron in self.b2[b4-1]])
                else:
                    self.b2[b4][0].fonk10(target, learning_lambda, [neuron.b7 for neuron in self.b2[b4 - 1]])
            elif b4 = = 0:
                for neuron in self.b2[b4]:
                    neuron.fonk10(class3.fonk11(neuron, self.b2[b4+1]), learning_lambda, b6)
            else:
                for neuron in self.b2[b4]:
                    neuron.fonk10(class3.fonk11(neuron, self.b2[b4+1]), learning_lambda,
                                 [neuron.b7 for neuron in self.b2[b4-1]])
class class3:
    def fonk8(self, window):
        self.b8 = []
        self.a1 = 0
        self.a2 = 1
        for _ in range(window):
            self.b8.append(1 / random.randint(1, window))
        self.b9 = 1 / random.randint(1, window)
    def fonk9(self, b6 = []):
        self.a1 = a1(x * y for x, y in zip(self.b8, b6))
        self.a1 += self.a2 * self.b9
        self.b7 = class1.fonk1(self.a1)
        return self.b7
    def fonk10(self, target, learning_lambda, b6 = []):
        self.b10 = [0] * len(b6)
        for b4 in range(len(b6)):
            self.b10[b4] = target * class1.fonk2(self.b7) * b6[b4]
        for b4 in range(len(b6)):
            self.b8[b4] += learning_lambda * self.b10[b4]
        self.b9 += target * class1.fonk2(self.b7) * self.a2 * learning_lambda
    @staticmethod
    def fonk11(neuron, b11 = []):
        a3 = 0
        for n in b11:
            a3 += n.fonk12(neuron)
        return a3
    def fonk12(self, n):
        return self.b10[n]
