import csv
import random
import math
import operator
def load_dataset(filename, split_ratio, train_set=[], test_set=[], signal_count=4):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for row in dataset:
            row[:signal_count] = [float(val) for val in row[:signal_count]]
            if random.random() < split_ratio:
                train_set.append(row)
            else:
                test_set.append(row)
def calculate_distance(instance1, instance2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(instance1, instance2)))
def get_neighbors(train_set, test_instance, k):
    distances = [(train_instance, calculate_distance(test_instance, train_instance[:-1])) for train_instance in train_set]
    distances.sort(key=operator.itemgetter(1))
    return [train_instance for train_instance, _ in distances[:k]]
def get_response(neighbors):
    class_votes = {}
    for neighbor in neighbors:
        response = neighbor[-1]
        class_votes[response] = class_votes.get(response, 0) + 1
    return max(class_votes.items(), key=operator.itemgetter(1))[0]
def calculate_accuracy(test_set, predictions):
    correct_count = sum(1 for actual, predicted in zip(test_set, predictions) if actual[-1] == predicted)
    return (correct_count / float(len(test_set))) * 100.0
def main():
    train_set = []
    test_set = []
    split_ratio = 0.67
    load_dataset('traindata.csv', split_ratio, train_set, test_set, 4)
    print('Train set size:', len(train_set))
    print('Test set size:', len(test_set))
    predictions = []
    k_neighbors = 3
    for test_instance in test_set:
        neighbors = get_neighbors(train_set, test_instance, k_neighbors)
        result = get_response(neighbors)
        predictions.append(result)
        print('> Predicted Decision:', result, ', Actual Decision:', test_instance[-1])
    accuracy = calculate_accuracy(test_set, predictions)
    print('Accuracy:', accuracy, '%')
if __name__ == '__main__':
    main()