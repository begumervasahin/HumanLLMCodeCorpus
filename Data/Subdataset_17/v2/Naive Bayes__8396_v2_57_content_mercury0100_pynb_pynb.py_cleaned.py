'''
Name: pynb
By: CDoyle
Implementation of a Gaussian Naive Bayes algorithm
'''
import numpy as np
def separate_classes(data, labels):
    '''
    Separates data into corresponding classes and returns a dictionary with classes as keys.
    '''
    separated = {}
    for i in range(len(data)):
        x = data[i]
        y = labels[i]
        if y not in separated:
            separated[y] = []
        separated[y].append(x)
    return separated
def summarize(data):
    '''
    Returns column-wise mean and standard deviation of a dataset as a list.
    '''
    summaries = [(np.mean(data[:, i]), np.std(data[:, i])) for i in range(data.shape[1])]
    return summaries
def summarize_classes(dataset, labels):
    '''
    Returns summaries of classes, i.e., a dictionary with each class's feature means and standard deviations.
    '''
    separated = separate_classes(dataset, labels)
    summaries = {}
    for classification, instances in separated.items():
        summaries[classification] = summarize(np.array(instances))
    return summaries, separated
def gaussian(x, mean, stdev):
    '''
    Computes the Gaussian probability distribution function for x.
    '''
    exponent = np.exp(-(np.power(x - mean, 2) / (2 * np.power(stdev + 1e-9, 2))))
    return (1 / (np.sqrt(2 * np.pi) * (stdev + 1e-9))) * exponent
class NaiveBayes:
    '''
    Implementation of the Naive Bayes algorithm.
    '''
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.summaries, self.separated = summarize_classes(data, labels)
    def class_probabilities(self, input):
        '''
        Computes the class probabilities for a given input.
        '''
        probabilities = {}
        for class_value, class_summaries in self.summaries.items():
            probabilities[class_value] = 0
            for i in range(len(class_summaries)):
                mean, stdev = class_summaries[i]
                x = input[i]
                prob = np.log(gaussian(x, mean, stdev))
                probabilities[class_value] += prob
        return probabilities
    def predict(self, input):
        '''
        Predicts the class for a given input.
        '''
        probabilities = self.class_probabilities(input)
        best_label, best_prob = None, -np.inf
        for class_value, probability in probabilities.items():
            if best_label is None or probability > best_prob:
                best_prob = probability
                best_label = class_value
        return best_label
    def get_predictions(self, test_data):
        '''
        Predicts the class for each instance in the test data.
        '''
        predictions = [self.predict(test_instance) for test_instance in test_data]
        return predictions
if __name__ == "__main__":
    train_data = np.array([[1.0, 20.0], [2.0, 21.0], [3.0, 22.0], [4.0, 23.0], [5.0, 24.0]])
    train_labels = np.array([0, 1, 0, 1, 0])
    test_data = np.array([[1.5, 20.5], [3.5, 22.5]])
    nb = NaiveBayes(train_data, train_labels)
    predictions = nb.get_predictions(test_data)
    print("Predictions:", predictions)