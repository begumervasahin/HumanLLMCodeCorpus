'''
Name: pynb
By: CDoyle
Implementation of a Gaussian Naive Bayes algorithm
'''
import numpy as np
def fonk1(b6, b7):
    '''
    Separates b6 into corresponding classes
    returns a dict with classes for keys
    '''
    b1 = {}
    for i in range(len(b6)):
        b2 = b6[i]
        b3 = b7[i]
        if b3 not in b1:
            b1[b3] = []
        b1[b3].append(b2)
    return b1
def fonk2(b6):
    '''
    returns columnwise mean and std of a dataset as list
    '''
    b4 = [(np.mean(b6[:,i]), np.std(b6[:,i])) for i in range(b6.shape[1])]
    return b4
def fonk3(dataset, b7):
    '''
    returns "b4" of classes, i.e. a dict with each class'
    feature means and standard deviations
    '''
    b1 = fonk1(dataset, b7)
    b4 = {}
    for classification, instances in b1.items():
        b4[classification] = fonk2(np.array(instances))
    return b4, b1
def fonk4(b2, mean, b9):
    b5 = np.exp(-(np.power(b2 - mean, 2) / (2 * np.power(b9 + 1e-9, 2))))
    return (1 / (np.sqrt(2 * np.pi) * (b9 + 1e-9))) * b5
class class1:
    '''
    Implementation of the Naive Bayes algorithm
    '''
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
                b10 = np.log(fonk4(b2, mean, b9))
                b8[cat] += b10
        return b8
    def fonk7(self, input):
        b8 = self.fonk6(input)
        b12, b11 = None, -np.inf
        for cat, probability in b8.items():
            if b12 is None or probability > b11:
                b11 = probability
                b12 = cat
        return b12
    def fonk8(self, b18):
        b13 = []
        for i in range(len(b18)):
            b14 = self.fonk7(b18[i])
            b13.append(b14)
        return b13
if b15 = = "__main__":
    b16 = np.array([[1.0, 20.0], [2.0, 21.0], [3.0, 22.0], [4.0, 23.0], [5.0, 24.0]])
    b17 = np.array([0, 1, 0, 1, 0])
    b18 = np.array([[1.5, 20.5], [3.5, 22.5]])
    b19 = class1(b16, b17)
    b13 = b19.fonk8(b18)
    print("Predictions:", b13)