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
    return sum(numbers) / len(numbers)
def standard_deviation(numbers):
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
def calculate_parameters(data):
    params = [(mean(feature), standard_deviation(feature)) for feature in zip(*data)]
    del params[-1]
    return params
def calculate_probability(x, mean, stdev):
    exponent = math.exp(-(pow(x - mean, 2) / (2 * pow(stdev, 2))))
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
def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row = [float(value) for value in row]
            row[-1] = 1 if row[-1] == 'M' else 2
            dataset.append(row)
    return dataset
def display_summary(parameters):
    print('Summary by class value:')
    for class_label, params in parameters.items():
        print(f"Class {class_label}: {params}")
def main():
    dataset = load_dataset('data.csv')
    labeled_data = divide_by_label(dataset)
    parameters = {class_label: calculate_parameters(data) for class_label, data in labeled_data.items()}
    display_summary(parameters)
    test_set = [float(x) for x in input('Enter data for prediction (separated by spaces): ').split()]
    prediction = predict(parameters, test_set)
    predicted_class = 'M' if prediction == 1 else 'W'
    print(f'Predicted class: {predicted_class}')
if __name__ == '__main__':
    main()