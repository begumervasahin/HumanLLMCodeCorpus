import csv
import getopt
import math
import sys
import numpy as np
import pandas as pd
def separate_by_class(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[0] not in separated:
            separated[vector[0]] = []
        separated[vector[0]].append(vector)
    return separated
def mean(numbers):
    return sum(numbers) / float(len(numbers))
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)
def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[:1]
    return summaries
def prior(dataset):
    class_col = dataset[:, 0]
    class_count = np.bincount(class_col.astype(int))
    total_count = len(class_col)
    priors = class_count / total_count
    return priors
def summarize_by_class(dataset):
    separated = separate_by_class(dataset)
    summaries = {}
    for class_value, instances in separated.items():
        summaries[class_value] = summarize(instances)
    return summaries
def calculate_probability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent
def calculate_class_probabilities(summaries, input_vector):
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = 1
        for i in range(len(class_summaries)):
            mean, stdev = class_summaries[i]
            x = input_vector[i + 1]
            probabilities[class_value] *= calculate_probability(x, mean, stdev)
    return probabilities
def predict(summaries, input_vector):
    probabilities = calculate_class_probabilities(summaries, input_vector)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label
def get_predictions(summaries, test_set):
    predictions = []
    for i in range(len(test_set)):
        result = predict(summaries, test_set[i])
        predictions.append(result)
    return predictions
def get_accuracy(test_set, predictions):
    correct = 0
    for i in range(len(test_set)):
        if test_set[i][0] == predictions[i]:
            correct += 1
    return correct / float(len(test_set)) * 100.0
def write_data(row1, row2, row3, filename):
    with open(filename, 'w', newline='') as outfile:
        output_file = csv.writer(outfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        output_file.writerow(row1)
        output_file.writerow(row2)
        output_file.writerow(row3)
        print("Output file written to " + filename)
if __name__ == '__main__':
    argv = sys.argv[1:]
    inputfile = ""
    outputfile = ""
    if len(argv) != 0:
        try:
            opts, args = getopt.getopt(argv, "hi:o:", ["data=", "output="])
        except getopt.GetoptError:
            print('usage: Naive_bayes.py -i <inputfile> -o <outputfile>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('usage: Naive_bayes.py -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ("-i", "--data"):
                inputfile = arg
                if '.tsv' not in inputfile:
                    inputfile = inputfile + '.tsv'
            elif opt in ("-o", "--output"):
                outputfile = arg
                if '.tsv' not in outputfile:
                    outputfile = outputfile + '.tsv'
    else:
        inputfile = input("Enter data file name: ")
        if '.tsv' not in inputfile:
            inputfile = inputfile + '.tsv'
        outputfile = input("Enter Output file name: ")
        if '.tsv' not in outputfile:
            outputfile = outputfile + '.tsv'
    if inputfile == "":
        inputfile = input("Enter data file name: ")
        if '.tsv' not in inputfile:
            inputfile = inputfile + '.tsv'
    if outputfile == "":
        outputfile = input("Enter Output file name: ")
        if '.tsv' not in outputfile:
            outputfile = outputfile + '.tsv'
    data = pd.read_csv(inputfile, sep='\t', header=None)
    data.columns = ['Class', 'x1', 'x2']
    data['Class'] = np.where(data['Class'] == 'A', 1, 0)
    data = data.values
    prior_prob = prior(data)
    summaries = summarize_by_class(data)
    predictions = get_predictions(summaries, data)
    accuracy = get_accuracy(data, predictions)
    print(f'Accuracy: {accuracy:.2f}%')
    row1 = [
        summaries[1.0][0][0],
        math.pow(summaries[1.0][0][1], 2),
        summaries[1.0][1][0],
        math.pow(summaries[1.0][1][1], 2),
        prior_prob[1]
    ]
    row2 = [
        summaries[0.0][0][0],
        math.pow(summaries[0.0][0][1], 2),
        summaries[0.0][1][0],
        math.pow(summaries[0.0][1][1], 2),
        prior_prob[0]
    ]
    row3 = [len(data) - accuracy]
    write_data(row1, row2, row3, outputfile)