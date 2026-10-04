
import numpy as np
def separate_classes(data, label):
    separated = {}
    for i in range(len(data)):
        x = data[i]
        y = label[i]
        if y not in separated:
            separated[y] = []
        separated[y].append(x)
    return separated
def summarise(data):
    summaries = [(np.mean(data[:,i]), np.std(data[:,i])) for i in range(data.shape[1])]
    return summaries
def summarise_classes(dataset, label):
    separated = separate_classes(dataset, label)
    summaries = {classification: summarise(np.array(instances)) for classification, instances in separated.items()}
    return summaries, separated
def gaussian(x, mean, stdev):
    exponent = np.exp(-(np.power(x - mean, 2) / (2 * np.power(stdev + 1e-9, 2))))
    return (1 / (np.sqrt(2 * np.pi) * (stdev + 1e-9))) * exponent
class NaiveBayes:
    def __init__(self, data, label):
        self.data = data
        self.label = label
        self.summaries, self.separated = summarise_classes(data, label)
    def class_prob(self, input):
        probabilities = {}
        for cat, summary in self.summaries.items():
            probabilities[cat] = 0
            for i in range(len(summary)):
                mean, stdev = summary[i]
                x = input[i]
                probabilities[cat] += np.log(gaussian(x, mean, stdev))
        return probabilities
    def predict(self, input):
        probabilities = self.class_prob(input)
        best_label, best_prob = None, -np.inf
        for cat, probability in probabilities.items():
            if best_label is None or probability > best_prob:
                best_prob = probability
                best_label = cat
        return best_label
    def get_predictions(self, test_data):
        predictions = [self.predict(test_data[i]) for i in range(len(test_data))]
        return predictions
