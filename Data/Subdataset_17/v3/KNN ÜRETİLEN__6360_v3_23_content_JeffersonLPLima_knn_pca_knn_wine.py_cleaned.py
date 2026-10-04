import csv
import math
import operator
def euclidean_distance(instance1, instance2, length):
    return math.sqrt(sum((float(instance1[x]) - float(instance2[x])) ** 2 for x in range(length)))
def get_neighbors(training_set, test_instance, k):
    distances = [(train_instance, euclidean_distance(test_instance, train_instance, len(test_instance) - 1)) for train_instance in training_set]
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
def load_data(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            data.append([float(attr) for attr in row])
    return data
def main():
    datasets = [load_data(f'{i}.data') for i in range(1, 4)]
    for i, dataset in enumerate(datasets, start=1):
        print(f'Dataset {i} size: {len(dataset)}')
    total_accuracy = 0
    for i in range(10):
        training_set, test_set = [], []
        for dataset in datasets:
            fold_size = len(dataset)
            test_set.extend(dataset[i * fold_size: (i + 1) * fold_size])
            training_set.extend(dataset[:i * fold_size] + dataset[(i + 1) * fold_size:])
        print(f"Fold {i + 1}")
        print(f"Training set size: {len(training_set)}")
        print(f"Test set size: {len(test_set)}")
        predictions = [get_response(get_neighbors(training_set, test_instance, k=1)) for test_instance in test_set]
        accuracy = get_accuracy(test_set, predictions)
        print(f"Accuracy: {accuracy:.2f}%")
        total_accuracy += accuracy
    print(f"Average accuracy: {total_accuracy / 10:.2f}%")
if __name__ == "__main__":
    main()