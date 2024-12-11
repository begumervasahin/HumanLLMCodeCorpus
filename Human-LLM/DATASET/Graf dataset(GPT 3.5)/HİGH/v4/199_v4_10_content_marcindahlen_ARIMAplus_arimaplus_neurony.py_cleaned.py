import arimaplus_math
import random
class class1:
    def fonk1(self, window, b11, b5, arima):
        self.b1 = len(b11)
        self.b2 = [[] for _ in range(self.b1)]
        for b4 in range(self.b1):
            b3 = b11[b4]
            for _ in range(b3):
                if b4 = = 0:
                    self.b2[b4].append(class2(window))
                else:
                    self.b2[b4].append(class2(b11[b4 - 1]))
        if b5 in [1, 4, 5, 6, 7]:
            self.b2.append([class2(b11[-1]) for _ in range(window if b5 = = 1 else arima)])
        self.b1 += 1
    def fonk2(self, b6 = []):
        self.b7 = []
        for b4 in range(self.b1):
            if b4 = = 0:
                for neuron in self.b2[b4]:
                    neuron.fonk19(b6)
            else:
                for neuron in self.b2[b4]:
                    neuron.fonk19([neuron.b7 for neuron in self.b2[b4 - 1]])
                    if b4 = = self.b1 - 1:
                        self.b7.append(neuron.fonk19([neuron.b7 for neuron in self.b2[b4 - 1]]))
        return self.b7
    def fonk3(self, target, learning_lambda, b6 = []):
        for b4 in reversed(range(self.b1)):
            if b4 = = self.b1 - 1:
                for j, target_val in enumerate(target):
                    self.b2[b4][j].fonk20(target_val, learning_lambda, [neuron.b7 for neuron in self.b2[b4 - 1]])
            elif b4 = = 0:
                for neuron in self.b2[b4]:
                    neuron.fonk20(a1([neuron.fonk21(j, self.b2[b4 + 1]) for j in range(len(self.b2[b4 + 1]))]), learning_lambda, b6)
            else:
                for neuron in self.b2[b4]:
                    neuron.fonk20(a1([neuron.fonk21(j, self.b2[b4 + 1]) for j in range(len(self.b2[b4 + 1]))]), learning_lambda, [neuron.b7 for neuron in self.b2[b4 - 1]])
class class2:
    def fonk4(self, window):
        self.b8 = []
        self.a1 = 0
        self.a2 = 1
        for _ in range(window):
            self.b8.append(1 / random.randint(1, window))
        self.b9 = 1 / random.randint(1, window)
        self.b7 = 0
    def fonk5(self, b6 = []):
        self.a1 = a1(x * y for x, y in zip(self.b8, b6)) + self.a2 * self.b9
        self.b7 = arimaplus_math.tanh(self.a1)
        return self.b7
    def fonk6(self, target, learning_lambda, b6 = []):
        self.b10 = [0] * len(b6)
        for b4 in range(len(b6)):
            self.b10[b4] = target * arimaplus_math.derivative_tanh(self.b7) * b6[b4]
            self.b8[b4] += learning_lambda * self.b10[b4]
        self.b9 += target * arimaplus_math.derivative_tanh(self.b7) * self.a2 * learning_lambda
    def fonk7(self, which_neuron, b11 = []):
        a3 = 0
        for neuron in b11:
            a3 += neuron.fonk22(which_neuron)
        return a3
    def fonk8(self, n):
        return self.b10[n]
class class3:
    def fonk9(self, window, b11, b5, arima):
        self.b1 = len(b11)
        self.b2 = [[] for _ in range(self.b1)]
        for b4 in range(self.b1):
            b3 = b11[b4]
            for _ in range(b3):
                if b4 = = 0:
                    self.b2[b4].append(class4(window))
                else:
                    self.b2[b4].append(class4(b11[b4 - 1]))
        if b5 in [1, 4, 5, 6, 7]:
            self.b2.append([class4(b11[-1]) for _ in range(window if b5 = = 1 else arima)])
        self.b1 += 1
    def fonk10(self, b6 = []):
        self.b7 = []
        for b4 in range(self.b1):
            if b4 = = 0:
                for neuron in self.b2[b4]:
                    neuron.fonk19(b6)
            else:
                for neuron in self.b2[b4]:
                    neuron.fonk19([neuron.b7 for neuron in self.b2[b4 - 1]])
                    if b4 = = self.b1 - 1:
                        self.b7.append(neuron.fonk19([neuron.b7 for neuron in self.b2[b4 - 1]]))
    def fonk11(self, target, learning_lambda, b6 = []):
        for b4 in reversed(range(self.b1)):
            if b4 = = self.b1 - 1:
                for j, target_val in enumerate(target):
                    self.b2[b4][j].fonk20(target_val, learning_lambda, [neuron.b7 for neuron in self.b2[b4 - 1]])
            elif b4 = = 0:
                for neuron in self.b2[b4]:
                    neuron.fonk20(a1([neuron.fonk21(j, self.b2[b4 + 1]) for j in range(len(self.b2[b4 + 1]))]), learning_lambda, b6)
            else:
                for neuron in self.b2[b4]:
                    neuron.fonk20(a1([neuron.fonk21(j, self.b2[b4 + 1]) for j in range(len(self.b2[b4 + 1]))]), learning_lambda, [neuron.b7 for neuron in self.b2[b4 - 1]])
class class4:
    def fonk12(self, window):
        self.b8 = [[] for _ in range(4)]
        self.b12 = []
        self.b18, self.b22, self.b21, self.b13 = 0, 0, 0, 0
        self.b19, self.b20, self.b17, self.b14 = 0, 0, 0, 0
        self.bias_in, self.bias_out, self.bias_forget, self.b15 = 1, 1, 1, 1
        self.a4 = 0
        self.b7 = 0
        for _ in range(4):
            for _ in range(window):
                self.b8[_].append(1 / random.randint(1, 4 * window))
            self.b12.append(1 / random.randint(1, 4 * window))
        self.a5 = 0
        self.b16 = 1 / random.randint(1, 4 * window)
    def fonk13(self, b6 = []):
        self.a5 = self.b7
        self.b17 = self.a4
        self.b18 = a1(b6[b4] * self.b8[0][b4] for b4 in range(len(b6))) + self.bias_in * self.b12[0]
        self.b19 = arimaplus_math.sigmoid(self.b18)
        self.b13 = a1(b6[b4] * self.b8[1][b4] for b4 in range(len(b6))) + self.bias_forget * self.b12[1]
        self.b20 = arimaplus_math.sigmoid(self.b13)
        self.b21 = a1(b6[b4] * self.b8[2][b4] for b4 in range(len(b6))) + self.b15 * self.b12[2] + self.a5 * self.b16
        self.a4 = self.b20 * self.b17 + self.b19 * arimaplus_math.tanh(self.b21)
        self.b22 = a1(b6[b4] * self.b8[3][b4] for b4 in range(len(b6))) + self.bias_out * self.b12[3]
        self.b14 = arimaplus_math.sigmoid(self.b22)
        self.b7 = arimaplus_math.tanh(self.a4) * self.b14
        return self.b7
    def fonk14(self, target, learning_lambda, b6 = []):
        self.b10 = [[] for _ in range(4)]
        for _ in range(4):
            for _ in range(len(b6)):
                self.b10[_].append(0)
        for b4 in range(len(b6)):
            self.b10[0][b4] = target * self.b14 * arimaplus_math.derivative_tanh(self.a4) * self.b20 * arimaplus_math.derivative_tanh(self.b21) * arimaplus_math.derivative_sigmoid(self.b18) * b6[b4]
            self.b10[1][b4] = target * self.b14 * arimaplus_math.derivative_tanh(self.a4) * self.b19 * arimaplus_math.derivative_tanh(self.b21) * arimaplus_math.derivative_sigmoid(self.b13) * b6[b4]
            self.b10[2][b4] = target * self.b14 * arimaplus_math.derivative_tanh(self.a4) * self.b20 * self.b19 * arimaplus_math.derivative_tanh(self.b21) * b6[b4]
            self.b10[3][b4] = target * arimaplus_math.derivative_tanh(self.a4) * arimaplus_math.derivative_sigmoid(self.b22) * b6[b4]
        self.b12[0] += learning_lambda * target * self.b14 * arimaplus_math.derivative_tanh(self.a4) * self.b20 * arimaplus_math.derivative_tanh(self.b21) * arimaplus_math.derivative_sigmoid(self.b18) * self.bias_in
        self.b12[1] += learning_lambda * target * self.b14 * arimaplus_math.derivative_tanh(self.a4) * self.b19 * arimaplus_math.derivative_tanh(self.b21) * arimaplus_math.derivative_sigmoid(self.b13) * self.bias_out
        self.b12[2] += learning_lambda * target * self.b14 * arimaplus_math.derivative_tanh(self.a4) * self.b20 * self.b19 * arimaplus_math.derivative_tanh(self.b21) * self.b15
        self.b12[3] += learning_lambda * target * arimaplus_math.derivative_tanh(self.a4) * arimaplus_math.derivative_sigmoid(self.b22) * self.bias_forget
        self.b16 += learning_lambda * target * self.b14 * arimaplus_math.derivative_tanh(self.a4) * self.b20 * self.b19 * arimaplus_math.derivative_tanh(self.b21) * self.a5
        for b4 in range(len(b6)):
            self.b8[0][b4] += learning_lambda * self.b10[0][b4]
            self.b8[1][b4] += learning_lambda * self.b10[1][b4]
            self.b8[2][b4] += learning_lambda * self.b10[2][b4]
            self.b8[3][b4] += learning_lambda * self.b10[3][b4]
class class5:
    def fonk15(self, window, b11, b5, arima):
        self.b1 = len(b11)
        self.b2 = [[] for _ in range(self.b1)]
        for b4 in range(self.b1):
            b3 = b11[b4]
            for _ in range(b3):
                if b4 = = 0:
                    self.b2[b4].append(class6(window))
                else:
                    self.b2[b4].append(class6(b11[b4 - 1]))
        if b5 in [1, 4, 5, 6, 7]:
            self.b2.append([class6(b11[-1]) for _ in range(window if b5 = = 1 else arima)])
        self.b1 += 1
    def fonk16(self, b6 = []):
        self.b7 = []
        for b4 in range(self.b1):
            if b4 = = 0:
                for neuron in self.b2[b4]:
                    neuron.fonk19(b6)
            else:
                for neuron in self.b2[b4]:
                    neuron.fonk19([neuron.b7 for neuron in self.b2[b4 - 1]])
                    if b4 = = self.b1 - 1:
                        self.b7.append(neuron.fonk19([neuron.b7 for neuron in self.b2[b4 - 1]]))
    def fonk17(self, target, learning_lambda, b6 = []):
        for b4 in reversed(range(self.b1)):
            if b4 = = self.b1 - 1:
                for j, target_val in enumerate(target):
                    self.b2[b4][j].fonk20(target_val, learning_lambda, [neuron.b7 for neuron in self.b2[b4 - 1]])
            elif b4 = = 0:
                for neuron in self.b2[b4]:
                    neuron.fonk20(a1([neuron.fonk21(j, self.b2[b4 + 1]) for j in range(len(self.b2[b4 + 1]))]), learning_lambda, b6)
            else:
                for neuron in self.b2[b4]:
                    neuron.fonk20(a1([neuron.fonk21(j, self.b2[b4 + 1]) for j in range(len(self.b2[b4 + 1]))]), learning_lambda, [neuron.b7 for neuron in self.b2[b4 - 1]])
class class6:
    def fonk18(self, window):
        self.b8 = [[] for _ in range(3)]
        self.b9 = []
        self.b27, self.b29, self.b23 = 0, 0, 0
        self.b28, self.b30, self.b24 = 0, 0, 0
        self.bias_zt, self.bias_rt, self.b25 = 1, 1, 1
        self.b7 = 0
        self.a2 = 1
        for _ in range(3):
            for _ in range(window):
                self.b8[_].append(1 / random.randint(1, 3 * window))
            self.b9.append(1 / random.randint(1, 3 * window))
        self.a5 = 0
        self.b26 = 1 / random.randint(1, 4 * window)
    def fonk19(self, b6 = []):
        self.a5 = self.b7
        self.b27 = a1(b6[b4] * self.b8[0][b4] for b4 in range(len(b6))) + self.a5 * self.b26 + self.bias_zt * self.b9[0]
        self.b28 = arimaplus_math.sigmoid(self.b27)
        self.b29 = a1(b6[b4] * self.b8[1][b4] for b4 in range(len(b6))) + self.a5 * self.b26 + self.bias_rt * self.b9[1]
        self.b30 = arimaplus_math.sigmoid(self.b29)
        self.b23 = a1(b6[b4] * self.b8[2][b4] for b4 in range(len(b6))) + self.a5 * self.b26 * self.b30 + self.b25 * self.b9[2]
        self.b24 = arimaplus_math.tanh(self.b23)
        self.b7 = (1 - self.b28) * self.a5 + self.b28 * self.b24
        return self.b7
    def fonk20(self, target, learning_lambda, b6 = []):
        self.b10 = [[] for _ in range(3)]
        for _ in range(3):
            for _ in range(len(b6)):
                self.b10[_].append(0)
        for b4 in range(len(b6)):
            self.b10[0][b4] = b6[b4] * (-1 * arimaplus_math.derivative_sigmoid(self.b27)) * (self.b24 * target + self.a5 * target)
            self.b10[1][b4] = b6[b4] * arimaplus_math.derivative_sigmoid(self.b29) * arimaplus_math.derivative_tanh(self.b23) * target * (1 - self.b28)
            self.b10[2][b4] = b6[b4] * arimaplus_math.derivative_tanh(self.b23) * target * (1 - self.b28)
        self.b26 += learning_lambda * self.a5 * (-1 * arimaplus_math.derivative_sigmoid(self.b27)) * (self.b24 * target + self.a5 * target)
        self.b9[0] += learning_lambda * self.bias_zt * (-1 * arimaplus_math.derivative_sigmoid(self.b27)) * (self.b24 * target + self.a5 * target)
        self.b9[1] += learning_lambda * self.bias_rt * arimaplus_math.derivative_sigmoid(self.b29) * arimaplus_math.derivative_tanh(self.b23) * target * (1 - self.b28)
        self.b9[2] += learning_lambda * self.b25 * arimaplus_math.derivative_tanh(self.b23) * target * (1 - self.b28)
        for b4 in range(len(b6)):
            self.b8[0][b4] += learning_lambda * self.b10[0][b4]
            self.b8[1][b4] += learning_lambda * self.b10[1][b4]
            self.b8[2][b4] += learning_lambda * self.b10[2][b4]
    def fonk21(self, which_neuron, b11 = []):
        a3 = 0
        for neuron in b11:
            a3 += neuron.fonk22(which_neuron)
        return a3
    def fonk22(self, n):
        return self.b10[n]