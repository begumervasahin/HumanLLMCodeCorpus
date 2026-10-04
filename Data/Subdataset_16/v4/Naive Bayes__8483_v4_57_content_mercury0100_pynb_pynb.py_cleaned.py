
import numpy as np
def fonk1(b6, b7):
    b1 = {}
    for i in range(len(b6)):
        b2 = b6[i]
        b3 = b7[i]
        if b3 not in b1:
            b1[b3] = []
        b1[b3].append(b2)
    return b1
def fonk2(b6):
    b4 = [(np.mean(b6[:,i]), np.std(b6[:,i])) for i in range(b6.shape[1])]
    return b4
def fonk3(dataset, b7):
    b1 = fonk1(dataset, b7)
    b4 = {classification: fonk2(np.array(instances)) for classification, instances in b1.items()}
    return b4, b1
def fonk4(b2, mean, b9):
    b5 = np.exp(-(np.power(b2 - mean, 2) / (2 * np.power(b9 + 1e-9, 2))))
    return (1 / (np.sqrt(2 * np.pi) * (b9 + 1e-9))) * b5
class class1:
    def fonk5(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
        self.b4, self.b1 = fonk3(b6, b7)
    def fonk6(self, input):
        b8 = {}
        for cat, summary in self.b4.items():
            b8[cat] = 0
            for i in range(len(summary)):
                mean, b9 = summary[i]
                b2 = input[i]
                b8[cat] += np.log(fonk4(b2, mean, b9))
        return b8
    def fonk7(self, input):
        b8 = self.fonk6(input)
        b11, b10 = None, -np.inf
        for cat, probability in b8.items():
            if b11 is None or probability > b10:
                b10 = probability
                b11 = cat
        return b11
    def fonk8(self, test_data):
        b12 = [self.fonk7(test_data[i]) for i in range(len(test_data))]
        return b12
