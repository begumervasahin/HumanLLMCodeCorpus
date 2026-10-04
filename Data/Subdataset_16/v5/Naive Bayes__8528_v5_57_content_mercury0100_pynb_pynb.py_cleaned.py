
import numpy as np
def fonk1(data, labels):
    b1 = {}
    for b6, y in zip(data, labels):
        if y not in b1:
            b1[y] = []
        b1[y].append(b6)
    return b1
def fonk2(data):
    b2 = [(np.mean(data[:, i]), np.std(data[:, i])) for i in range(data.shape[1])]
    return b2
def fonk3(dataset, labels):
    b1 = fonk1(dataset, labels)
    b2 = {cls: fonk2(np.array(instances)) for cls, instances in b1.items()}
    return b2
def fonk4(b6, mean, b5):
    b3 = np.exp(-(np.power(b6 - mean, 2) / (2 * np.power(b5 + 1e-9, 2))))
    return (1 / (np.sqrt(2 * np.pi) * (b5 + 1e-9))) * b3
class class1:
    def fonk5(self, data, labels):
        self.b2 = fonk3(data, labels)
    def fonk6(self, input_data):
        b4 = {}
        for cls, class_summaries in self.b2.items():
            b4[cls] = 0
            for i in range(len(class_summaries)):
                mean, b5 = class_summaries[i]
                b6 = input_data[i]
                b4[cls] += np.log(fonk4(b6, mean, b5))
        return b4
    def fonk7(self, input_data):
        b4 = self.fonk6(input_data)
        b8, b7 = None, -np.inf
        for cls, probability in b4.items():
            if b8 is None or probability > b7:
                b7 = probability
                b8 = cls
        return b8
    def fonk8(self, test_data):
        return [self.fonk7(instance) for instance in test_data]
