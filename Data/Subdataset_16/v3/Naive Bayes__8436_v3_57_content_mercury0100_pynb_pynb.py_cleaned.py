
import numpy as np
def fonk1(b4, b5):
    b1 = {}
    for i, (b7, y) in enumerate(zip(b4, b5)):
        if y not in b1:
            b1[y] = []
        b1[y].append(b7)
    return b1
def fonk2(b4):
    return [(np.mean(b4[:, i]), np.std(b4[:, i])) for i in range(b4.shape[1])]
def fonk3(dataset, b5):
    b1 = fonk1(dataset, b5)
    b2 = {classification: fonk2(np.array(instances)) for classification, instances in b1.items()}
    return b2, b1
def fonk4(b7, mean, stdev):
    b3 = np.exp(-(np.power(b7 - mean, 2) / (2 * np.power(stdev + 1e-9, 2))))
    return (1 / (np.sqrt(2 * np.pi) * (stdev + 1e-9))) * b3
class class1:
    def fonk5(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
        self.b2, self.b1 = fonk3(b4, b5)
    def fonk6(self, input):
        b6 = {}
        for class_value, class_summaries in self.b2.items():
            b6[class_value] = 0
            for i, (mean, stdev) in enumerate(class_summaries):
                b7 = input[i]
                b6[class_value] += np.log(fonk4(b7, mean, stdev))
        return b6
    def fonk7(self, input):
        b6 = self.fonk6(input)
        b9, b8 = None, -np.inf
        for class_value, probability in b6.items():
            if b9 is None or probability > b8:
                b8 = probability
                b9 = class_value
        return b9
    def fonk8(self, b13):
        return [self.fonk7(test_instance) for test_instance in b13]
if b10 = = "__main__":
    b11 = np.array([[1.0, 20.0], [2.0, 21.0], [3.0, 22.0], [4.0, 23.0], [5.0, 24.0]])
    b12 = np.array([0, 1, 0, 1, 0])
    b13 = np.array([[1.5, 20.5], [3.5, 22.5]])
    b14 = class1(b11, b12)
    b15 = b14.fonk8(b13)
    print("Predictions:", b15)