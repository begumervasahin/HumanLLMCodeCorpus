import numpy as np
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b6, self.b3 = self.fonk4(b1, b2)
    def fonk2(self):
        '''
        Separates b1 into corresponding classes
        Returns a dictionary with classes as keys
        '''
        b3 = {}
        for i in range(len(self.b1)):
            b4 = self.b1[i]
            b5 = self.b2[i]
            if b5 not in b3:
                b3[b5] = []
            b3[b5].append(b4)
        return b3
    def fonk3(self, b1):
        '''
        Returns column-wise mean and standard deviation of a dataset as a list
        '''
        b6 = [(np.mean(b1[:, i]), np.std(b1[:, i])) for i in range(b1.shape[1] - 1)]
        return b6
    def fonk4(self, dataset, b2):
        '''
        Returns "b6" of classes, i.e., a dictionary with each class' feature means and standard deviations
        '''
        b3 = self.fonk2()
        b6 = {}
        for classification, instances in b3.items():
            b6[classification] = self.fonk3(np.array(instances))
        return b6, b3
    def fonk5(self, b4, mean, b9):
        '''
        Gaussian probability density function
        '''
        b7 = np.exp(-(np.power(b4 - mean, 2) / (2 * np.power(b9 + 1e-9, 2))))
        return (1 / (np.sqrt(2 * np.pi) * (b9 + 1e-9))) * b7
    def fonk6(self, input):
        '''
        Calculates class b8 for a given input
        '''
        b8 = {}
        for cat, summary in self.b6.items():
            b8[cat] = 0
            for i in range(len(summary) - 1):
                mean, b9 = summary[i]
                b4 = input[i]
                b10 = np.log(self.fonk5(b4, mean, b9))
                b8[cat] += b10
        return b8
    def fonk7(self, input):
        '''
        Predicts the class b2 for a given input
        '''
        b8 = self.fonk6(input)
        b12, b11 = None, -np.inf
        for cat, probability in b8.items():
            if b12 is None or probability > b11:
                b11 = probability
                b12 = cat
        return b12
    def fonk8(self, test_data):
        '''
        Generates b13 for a given set of test b1
        '''
        b13 = []
        for i in range(len(test_data)):
            b14 = self.fonk7(test_data[i])
            b13.append(b14)
        return b13