import csv
import random
import math
import operator
def euclidean_distance(instance1, instance2):
    distance = 0
    for x in range(len(instance1) - 1):
        distance += (float(instance1[x]) - float(instance2[x])) ** 2
    return math.sqrt(distance)
def get_neighbors(training_set, test_instance, k):
    distances = [(train_instance, euclidean_distance(test_instance, train_instance)) for train_instance in training_set]
    distances.sort(key=operator.itemgetter(1))
    return [neighbor[0] for neighbor in distances[:k]]
def get_response(neighbors):
    class_votes = {}
    for neighbor in neighbors:
        response = neighbor[-1]
        class_votes[response] = class_votes.get(response, 0) + 1
    return max(class_votes.items(), key=operator.itemgetter(1))[0]
def get_accuracy(test_set, predictions):
    correct = sum(1 for x in range(len(test_set)) if test_set[x][-1] == predictions[x])
    return (correct / float(len(test_set))) * 100.0
def main():
    data_sets = []
    for i in range(1, 4):
        with open('{}.data'.format(i), 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter='     ')
            data_sets.append([list(map(float, line)) for line in lines])
    print('Number of data sets:', len(data_sets))
    for i, data_set in enumerate(data_sets):
        print('Data set {}: {}'.format(i+1, len(data_set)))
    avg_accuracy = 0
    for i in range(10):
        training_set = []
        test_set = []
        for data_set in data_sets:
            test_length = int(0.1 * len(data_set))
            test_indices = random.sample(range(len(data_set)), test_length)
            for j, instance in enumerate(data_set):
                if j in test_indices:
                    test_set.append(instance)
                else:
                    training_set.append(instance)
        print("Training set size:", len(training_set))
        print("Test set size:", len(test_set))
        predictions = []
        k = 1
        for instance in test_set:
            neighbors = get_neighbors(training_set, instance, k)
            result = get_response(neighbors)
            predictions.append(result)
        accuracy = get_accuracy(test_set, predictions)
        print("Fold {} - Accuracy: {:.2f}%".format(i+1, accuracy))
        avg_accuracy += accuracy
    print("Average accuracy over 10 folds:", avg_accuracy / 10)
if __name__ == "__main__":
    main()