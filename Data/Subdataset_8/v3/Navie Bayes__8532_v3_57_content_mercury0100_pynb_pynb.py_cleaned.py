import numpy as np
def separate_classes(data, label):
    '''
    Separates data into corresponding classes
    Returns a dictionary with classes as keys
    '''
    separated = {}
    for i in range(len(data)):
        x = data[i]
        y = label[i]
        if y not in separated:
            separated[y] = []
        separated[y].append(x)
    return separated
def compute_summaries(data):
    '''
    Computes column-wise mean and standard deviation of a dataset
    Returns a list of tuples containing mean and std
    '''
    summaries = [(np.mean(data[:, i]), np.std(data[:, i])) for i in range(data.shape[1]-1)]
    return summaries
def compute_class_summaries(dataset, label):
    '''
    Computes summaries of classes, i.e., a dictionary with each class' feature means and standard deviations
    '''
    separated = separate_classes(dataset, label)
    summaries = {}
    for classification, instances in separated.items():
        summaries[classification] = compute_summaries(np.array(instances))
    return summaries, separated
def gaussian(x, mean, stdev):
    '''
    Computes the Gaussian probability density function
    '''
    exponent = np.exp(-(np.power(x-mean, 2)/(2*np.power(stdev+1e-9, 2))))
    return (1/(np.sqrt(2*np.pi)*(stdev+1e-9)))*exponent
class NaiveBayes:
    '''
    Implementation of the Naive Bayes algorithm
    '''
    def __init__(self, data, label):
        self.data = data
        self.label = label
        self.class_summaries, self.separated_data = compute_class_summaries(data, label)
    def compute_class_log_prob(self, input):
        '''
        Computes the log probabilities for each class
        '''
        class_log_probabilities = {}
        for cat, summary in self.class_summaries.items():
            class_log_probabilities[cat] = 0
            for i in range(len(summary)-1):
                mean, stdev = summary[i]
                x = input[i]
                proba = np.log(gaussian(x, mean, stdev))
                class_log_probabilities[cat] += proba
        return class_log_probabilities
    def predict_class(self, input):
        '''
        Predicts the class label for a given input
        '''
        class_log_probabilities = self.compute_class_log_prob(input)
        best_label, best_prob = None, -np.inf
        for cat, log_probability in class_log_probabilities.items():
            if best_label is None or log_probability > best_prob:
                best_prob = log_probability
                best_label = cat
        return best_label
    def get_predictions(self, test_data):
        '''
        Generates predictions for a given test dataset
        '''
        predictions = []
        for i in range(len(test_data)):
            result = self.predict_class(test_data[i])
            predictions.append(result)
        return predictions
