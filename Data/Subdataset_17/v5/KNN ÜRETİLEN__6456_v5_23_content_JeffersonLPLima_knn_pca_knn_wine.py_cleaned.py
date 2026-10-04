import csv
import math
import operator
def euclidean_distance(instance1, instance2, length):
    return math.sqrt(sum((float(instance1[x]) - float(instance2[x])) ** 2 for x in range(length)))
def get_neighbors(training_set, test_instance, k):
    distances = [(training_instance, euclidean_distance(test_instance, training_instance, len(test_instance) - 1))
                 for training_instance in training_set]
    distances.sort(key=operator.itemgetter(1))
    return [distances[x][0] for x in range(k)]
def get_response(neighbors):
    class_votes = {}
    for neighbor in neighbors:
        response = neighbor[-1]
        class_votes[response] = class_votes.get(response, 0) + 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]
def get_accuracy(test_set, predictions):
    correct = sum(1 for x in range(len(test_set)) if test_set[x][-1] == predictions[x])
    return (correct / float(len(test_set))) * 100.0
def load_data(filename, delimiter='\t'):
    data = []
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=delimiter)
        for line in lines:
            data.append([float(value) for value in line])
    return data
def main():
    data1 = load_data('1.data')
    data2 = load_data('2.data')
    data3 = load_data('3.data')
    print(f'Training set size: {len(data1)}')
    print(f'Set 1 size: {len(data1)}')
    print(f'Set 2 size: {len(data2)}')
    print(f'Set 3 size: {len(data3)}')
    total_accuracy = 0
    for fold in range(10):
        training_set, test_set = [], []
        for data in (data1, data2, data3):
            fold_size = len(data)
            fold_start = fold_size * fold
            fold_end = fold_start + fold_size
            for index, instance in enumerate(data):
                if fold_start <= index < fold_end:
                    test_set.append(instance)
                else:
                    training_set.append(instance)
        print(f"Fold {fold}: Training set size: {len(training_set)}, Test set size: {len(test_set)}")
        predictions = []
        k = 1
        for test_instance in test_set:
            neighbors = get_neighbors(training_set, test_instance, k)
            result = get_response(neighbors)
            predictions.append(result)
        accuracy = get_accuracy(test_set, predictions)
        print(f"Fold {fold} Accuracy: {accuracy:.2f}%")
        total_accuracy += accuracy
    print(f"Average Accuracy: {total_accuracy / 10:.2f}%")
if __name__ == "__main__":
    main()