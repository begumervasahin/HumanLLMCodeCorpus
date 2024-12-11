import numpy as np
def fonk1(b6, b7):
    '''
    Separates b6 into corresponding classes
    Returns a dictionary with classes as keys
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
    Computes column-wise mean and standard deviation of a dataset
    Returns a list of tuples containing mean and std
    '''
    b4 = [(np.mean(b6[:, i]), np.std(b6[:, i])) for i in range(b6.shape[1]-1)]
    return b4
def fonk3(dataset, b7):
    '''
    Computes b4 of classes, i.e., a dictionary with each class' feature means and standard deviations
    '''
    b1 = fonk1(dataset, b7)
    b4 = {}
    for classification, instances in b1.items():
        b4[classification] = fonk2(np.array(instances))
    return b4, b1
def fonk4(b2, mean, b10):
    '''
    Computes the Gaussian probability density function
    '''
    b5 = np.exp(-(np.power(b2-mean, 2)/(2*np.power(b10+1e-9, 2))))
    return (1/(np.sqrt(2*np.pi)*(b10+1e-9)))*b5
class class1:
    '''
    Implementation of the Naive Bayes algorithm
    '''
    def fonk5(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
        self.class_summaries, self.b8 = fonk3(b6, b7)
    def fonk6(self, input):
        '''
        Computes the log probabilities for each class
        '''
        b9 = {}
        for cat, summary in self.class_summaries.items():
            b9[cat] = 0
            for i in range(len(summary)-1):
                mean, b10 = summary[i]
                b2 = input[i]
                b11 = np.log(fonk4(b2, mean, b10))
                b9[cat] += b11
        return b9
    def fonk7(self, input):
        '''
        Predicts the class b7 for a given input
        '''
        b9 = self.fonk6(input)
        b13, b12 = None, -np.inf
        for cat, log_probability in b9.items():
            if b13 is None or log_probability > b12:
                b12 = log_probability
                b13 = cat
        return b13
    def fonk8(self, test_data):
        '''
        Generates b14 for a given test dataset
        '''
        b14 = []
        for i in range(len(test_data)):
            b15 = self.fonk7(test_data[i])
            b14.append(b15)
        return b14
