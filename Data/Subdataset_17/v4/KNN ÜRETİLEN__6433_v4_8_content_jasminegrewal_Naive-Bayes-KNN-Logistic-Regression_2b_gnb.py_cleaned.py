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
            probs[class_label] *= calcProb(x, mean, stdev)
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
    return predict(parameters, test_set)
def main():
    given_data = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        training_data = list(reader)
        for row in training_data:
            for i in range(len(row)):
                if i == 3:
                    row[i] = 1 if row[i] == 'M' else 2
                row[i] = float(row[i])
            given_data.append(row)
    parameters = divbylabel(given_data)
    print(f'Summary by class value: {parameters}')
    test_set = list(map(float, input('Enter data for prediction: ').split()))
    prediction = getPredictions(parameters, test_set)
    if prediction == 1:
        print('M')
    else:
        print('W')
if __name__ == "__main__":
    main()