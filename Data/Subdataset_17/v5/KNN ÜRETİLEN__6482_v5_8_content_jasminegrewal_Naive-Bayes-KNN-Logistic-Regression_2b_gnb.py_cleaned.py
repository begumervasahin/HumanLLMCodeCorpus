import csv
import random
import math
def divide_by_class(data):
    class_dict = {}
    for element in data:
        class_label = element[-1]
        if class_label not in class_dict:
            class_dict[class_label] = []
        class_dict[class_label].append(element)
    return class_dict
def mean(numbers):
    return sum(numbers) / float(len(numbers))
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)
def calculate_parameters(data):
    params = [(mean(feature), stdev(feature)) for feature in zip(*data)]
    del params[-1]
    return params
def calculate_class_parameters(data):
    classes = divide_by_class(data)
    params = {}
    for class_label, instances in classes.items():
        params[class_label] = calculate_parameters(instances)
    return params
def calculate_probability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent
def calculate_class_probabilities(parameters, sample):
    probabilities = {}
    for class_label, class_params in parameters.items():
        probabilities[class_label] = 1
        for i in range(len(class_params)):
            mean, stdev = class_params[i]
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
def get_prediction(parameters, test_sample):
    return predict(parameters, test_sample)
def main():
    data = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        training_data = list(reader)
        for row in training_data:
            row = [float(item) if i != 3 else (1 if item == 'M' else 2) for i, item in enumerate(row)]
            data.append(row)
    parameters = calculate_class_parameters(data)
    print(f'Summary by class value: {parameters}')
    test_sample = list(map(float, input('Enter data for prediction (space-separated): ').split()))
    prediction = get_prediction(parameters, test_sample)
    print('M' if prediction == 1 else 'W')
if __name__ == "__main__":
    main()