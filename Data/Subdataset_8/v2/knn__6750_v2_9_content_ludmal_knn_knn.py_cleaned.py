import csv
import random
import math
import operator
def load_data(filename, split, train_set=[], test_set=[], num_features=4):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(num_features):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                train_set.append(dataset[x])
            else:
                test_set.append(dataset[x])
def euclidean_distance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)
def get_neighbors(train_set, test_instance, k):
    distances = []
    length = len(test_instance) - 1
    for x in range(len(train_set)):
        dist = euclidean_distance(test_instance, train_set[x], length)
        distances.append((train_set[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
def get_response(neighbors):
    class_votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]
def calculate_accuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(test_set))) * 100.0
def main():
    train_set = []
    test_set = []
    split_ratio = 0.67
    load_data('traindata.csv', split_ratio, train_set, test_set, num_features=4)
    print('Train set size:', len(train_set))
    print('Test set size:', len(test_set))
    predictions = []
    k_neighbors = 3
    for x in range(len(test_set)):
        neighbors = get_neighbors(train_set, test_set[x], k_neighbors)
        result = get_response(neighbors)
        predictions.append(result)
        print('> Predicted Decision:', result, ', Actual Decision:', test_set[x][-1])
    accuracy = calculate_accuracy(test_set, predictions)
    print('Accuracy:', accuracy, '%')
if __name__ == "__main__":
    main()