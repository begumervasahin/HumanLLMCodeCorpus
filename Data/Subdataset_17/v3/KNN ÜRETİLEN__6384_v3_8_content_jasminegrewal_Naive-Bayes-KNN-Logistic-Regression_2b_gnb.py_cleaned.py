import csv
import random
import math
def divide(data):
    label_dict = {}
    for element in data:
        class_label = element[-1]
        if class_label not in label_dict:
            label_dict[class_label] = []
        label_dict[class_label].append(element)
    return label_dict
def mean(numbers):
    return sum(numbers) / float(len(numbers))
def stdev(numbers):
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)
def calculate_params(data):
    params = [(mean(feature), stdev(feature)) for feature in zip(*data)]
    del params[-1]
    return params
def calculate_class_params(data):
    divided_data = divide(data)
    class_params = {}
    for class_label, instances in divided_data.items():
        class_params[class_label] = calculate_params(instances)
    return class_params
def calculate_probability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent
def calculate_class_probabilities(parameters, sample):
    probabilities = {}
    for class_label, params in parameters.items():
        probabilities[class_label] = 1
        for i in range(len(params)):
            mean, stdev = params[i]
            x = sample[i]
            probabilities[class_label] *= calculate_probability(x, mean, stdev)
    return probabilities
def predict(parameters, sample):
    probabilities = calculate_class_probabilities(parameters, sample)
    best_label, best_prob = None, -1
    for class_label, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_label
    return best_label
def get_predictions(parameters, test_set):
    return [predict(parameters, sample) for sample in test_set]
def main():
    data = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(4):
                if i == 3:
                    row[i] = 1 if row[i] == 'M' else 2
                row[i] = float(row[i])
            data.append(row)
    parameters = calculate_class_params(data)
    print('Summary by class value:', parameters)
    test_set = [[5.1, 3.5, 1.4, 0.2]]
    predictions = get_predictions(parameters, test_set)
    for prediction in predictions:
        print('M' if prediction == 1 else 'W')
if __name__ == "__main__":
    main()