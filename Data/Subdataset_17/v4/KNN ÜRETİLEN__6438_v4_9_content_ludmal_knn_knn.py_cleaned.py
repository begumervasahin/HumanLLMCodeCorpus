import csv
import random
import math
import operator
def load_dataset(filename, split_ratio, train_set=None, test_set=None, signal_length=4):
    if train_set is None:
        train_set = []
    if test_set is None:
        test_set = []
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for row in dataset[:-1]:
            for i in range(signal_length):
                row[i] = float(row[i])
            if random.random() < split_ratio:
                train_set.append(row)
            else:
                test_set.append(row)
def calculate_distance(instance1, instance2, length):
    distance = 0
    for i in range(length):
        distance += (instance1[i] - instance2[i]) ** 2
    return math.sqrt(distance)
def get_neighbors(train_set, test_instance, k):
    distances = []
    length = len(test_instance) - 1
    for train_instance in train_set:
        dist = calculate_distance(test_instance, train_instance, length)
        distances.append((train_instance, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = [distances[i][0] for i in range(k)]
    return neighbors
def get_response(neighbors):
    class_votes = {}
    for neighbor in neighbors:
        response = neighbor[-1]
        class_votes[response] = class_votes.get(response, 0) + 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]
def calculate_accuracy(test_set, predictions):
    correct = sum(1 for i in range(len(test_set)) if test_set[i][-1] == predictions[i])
    return (correct / float(len(test_set))) * 100.0
def main():
    train_set = []
    test_set = []
    split_ratio = 0.67
    load_dataset('traindata.csv', split_ratio, train_set, test_set, 4)
    print(f'Train set: {len(train_set)}')
    print(f'Test set: {len(test_set)}')
    predictions = []
    k = 3
    for test_instance in test_set:
        neighbors = get_neighbors(train_set, test_instance, k)
        result = get_response(neighbors)
        predictions.append(result)
        print(f'> Predicted Decision={result}, Actual Decision={test_instance[-1]}')
    accuracy = calculate_accuracy(test_set, predictions)
    print(f'Accuracy: {accuracy}%')
if __name__ == "__main__":
    main()