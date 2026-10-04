
import numpy as np
def separate_classes(data, labels):
    separated = {}
    for x, y in zip(data, labels):
        if y not in separated:
            separated[y] = []
        separated[y].append(x)
    return separated
def summarize(data):
    summaries = [(np.mean(data[:, i]), np.std(data[:, i])) for i in range(data.shape[1])]
    return summaries
def summarize_classes(dataset, labels):
    separated = separate_classes(dataset, labels)
    summaries = {cls: summarize(np.array(instances)) for cls, instances in separated.items()}
    return summaries
def gaussian(x, mean, stdev):
    exponent = np.exp(-(np.power(x - mean, 2) / (2 * np.power(stdev + 1e-9, 2))))
    return (1 / (np.sqrt(2 * np.pi) * (stdev + 1e-9))) * exponent
class NaiveBayes:
    def __init__(self, data, labels):
        self.summaries = summarize_classes(data, labels)
    def calculate_class_probabilities(self, input_data):
        probabilities = {}
        for cls, class_summaries in self.summaries.items():
            probabilities[cls] = 0
            for i in range(len(class_summaries)):
                mean, stdev = class_summaries[i]
                x = input_data[i]
                probabilities[cls] += np.log(gaussian(x, mean, stdev))
        return probabilities
    def predict(self, input_data):
        probabilities = self.calculate_class_probabilities(input_data)
        best_label, best_prob = None, -np.inf
        for cls, probability in probabilities.items():
            if best_label is None or probability > best_prob:
                best_prob = probability
                best_label = cls
        return best_label
    def get_predictions(self, test_data):
        return [self.predict(instance) for instance in test_data]
