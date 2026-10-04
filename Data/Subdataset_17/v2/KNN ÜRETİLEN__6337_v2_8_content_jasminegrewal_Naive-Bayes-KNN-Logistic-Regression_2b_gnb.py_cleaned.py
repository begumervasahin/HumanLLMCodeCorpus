import csv
import random
import math
def divide(data):
    label = {}
    for element in data:
        if element[-1] not in label:
            label[element[-1]] = []
        label[element[-1]].append(element)
    return label
def mean(numbers):
    return sum(numbers) / float(len(numbers))
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)
def calcparams(data):
    params = [(mean(feature), stdev(feature)) for feature in zip(*data)]
    del params[-1]
    return params
def divbylabel(data):
    classes = divide(data)
    params = {}
    for class_label, instances in classes.items():
        params[class_label] = calcparams(instances)
    return params
def calcProb(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent
def calcClssProb(parameters, sample):
    probs = {}
    for class_label, params in parameters.items():
        probs[class_label] = 1
        for i in range(len(params)):
            mean, stdev = params[i]
            x = sample[i]
            prob_density = calcProb(x, mean, stdev)
            probs[class_label] *= prob_density
    return probs
def predict(parameters, sample):
    probabilities = calcClssProb(parameters, sample)
    best_label, best_prob = None, -1
    for class_label, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_label
    return best_label
def getPredictions(parameters, test_set):
    return [predict(parameters, sample) for sample in test_set]
def main():
    data = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        raw_data = list(reader)
        for row in raw_data:
            for i in range(4):
                if i == 3:
                    row[i] = 1 if row[i] == 'M' else 2
                row[i] = float(row[i])
            data.append(row)
    parameters = divbylabel(data)
    print('Summary by class value:', parameters)
    test_set = [[5.1, 3.5, 1.4, 0.2]]
    predictions = getPredictions(parameters, test_set)
    for prediction in predictions:
        print('M' if prediction == 1 else 'W')
if __name__ == "__main__":
    main()