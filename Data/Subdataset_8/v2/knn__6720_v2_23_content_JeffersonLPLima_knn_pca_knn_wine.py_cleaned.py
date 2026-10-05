import csv
import math
import operator
import random
def euclideanDistance(instance1, instance2):
    distance = 0
    for x in range(len(instance1) - 1):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x])
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0
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
        trainingSet = []
        testSet = []
        for data in [data1, data2, data3]:
            random.shuffle(data)
            split_index = int(0.1 * len(data))
            testSet.extend(data[i * split_index: (i + 1) * split_index])
            trainingSet.extend(data[:i * split_index] + data[(i + 1) * split_index:])
        print("\nFold", i)
        print("Training set:", len(trainingSet))
        print("Test set:", len(testSet))
        predictions = []
        k = 1
        for instance in testSet:
            neighbors = getNeighbors(trainingSet, instance, k)
            result = getResponse(neighbors)
            predictions.append(result)
        accuracy = getAccuracy(testSet, predictions)
        print("Accuracy:", accuracy)
        avg_accuracy += accuracy
    print("\nAverage accuracy over 10 folds:", avg_accuracy / 10)
if __name__ == "__main__":
    main()