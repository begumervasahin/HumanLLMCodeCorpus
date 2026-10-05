import csv
import math
import operator
import random
def euclidean_distance(instance1, instance2):
    distance = 0
    for x in range(len(instance1) - 1):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)
def get_neighbors(training_set, test_instance, k):
    distances = []
    for x in range(len(training_set)):
        dist = euclidean_distance(test_instance, training_set[x])
        distances.append((training_set[x], dist))
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
def get_accuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(test_set))) * 100.0
def load_dataset(filename):
    dataset = []
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=' ')
        for row in lines:
            dataset.append([float(x) for x in row])
    return dataset
def main():
    data1 = load_dataset('1.data')
    data2 = load_dataset('2.data')
    data3 = load_dataset('3.data')
    print('Dataset lengths:')
    print('Data 1:', len(data1))
    print('Data 2:', len(data2))
    print('Data 3:', len(data3))
    avg_accuracy = 0
    for i in range(10):
        training_set = []
        test_set = []
        for data in [data1, data2, data3]:
            random.shuffle(data)
            split_index = int(0.1 * len(data))
            test_set.extend(data[i * split_index: (i + 1) * split_index])
            training_set.extend(data[:i * split_index] + data[(i + 1) * split_index:])
        print("\nFold", i)
        print("Training set:", len(training_set))
        print("Test set:", len(test_set))
        predictions = []
        k = 1
        for instance in test_set:
            neighbors = get_neighbors(training_set, instance, k)
            result = get_response(neighbors)
            predictions.append(result)
        accuracy = get_accuracy(test_set, predictions)
        print("Accuracy:", accuracy)
        avg_accuracy += accuracy
    print("\nAverage accuracy over 10 folds:", avg_accuracy / 10)
if __name__ == "__main__":
    main()