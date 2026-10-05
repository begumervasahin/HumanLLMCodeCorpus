import csv
import math
def divide_by_label(data):
    labels = {}
    for element in data:
        label = element[-1]
        if label not in labels:
            labels[label] = []
        labels[label].append(element)
    return labels
def mean(numbers):
    return sum(numbers) / float(len(numbers))
def stdev(numbers):
    avg = mean(numbers)
    variance = sum(pow(x - avg, 2) for x in numbers) / float(len(numbers) - 1)
    return math.sqrt(variance)
def calculate_parameters(data):
    params = [(mean(feature), stdev(feature)) for feature in zip(*data)]
    del params[-1]
    return params
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
            prob_density = calculate_probability(x, mean, stdev)
            probabilities[class_label] *= prob_density
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
    predictions = []
    for sample in test_set:
        result = predict(parameters, sample)
        predictions.append(result)
    return predictions
def main():
    given_data = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(4):
                if i == 3:
                    row[i] = 1 if row[i] == 'M' else 2
                row[i] = float(row[i])
            given_data.append(row)
    parameters = divide_by_label(given_data)
    print('Summary by class value:')
    for class_label, params in parameters.items():
        print(f"Class {class_label}: {params}")
    test_set = [float(x) for x in input('Enter data for prediction (separated by spaces): ').split()]
    prediction = predict(parameters, test_set)
    if prediction == 1:
        print('Predicted class: M')
    else:
        print('Predicted class: W')
if __name__ == '__main__':
    main()