import csv
import random
import math
import operator
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
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
def loadData(filename):
    data = []
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter='\t')
        dataset = list(lines)
        for x in range(len(dataset)):
            data.append([float(attr) for attr in dataset[x]])
    return data
def main():
    data1 = loadData('1.data')
    data2 = loadData('2.data')
    data3 = loadData('3.data')
    print('Dataset 1 size: ' + str(len(data1)))
    print('Dataset 2 size: ' + str(len(data2)))
    print('Dataset 3 size: ' + str(len(data3)))
    total_accuracy = 0
    for i in range(10):
        trainingSet = []
        testSet = []
        for x in range(len(data1)):
            if (x >= (0.1 * len(data1)) * i) and (x < (0.1 * len(data1)) * (i + 1)):
                testSet.append(data1[x])
            else:
                trainingSet.append(data1[x])
        for x in range(len(data2)):
            if (x >= (0.1 * len(data2)) * i) and (x < (0.1 * len(data2)) * (i + 1)):
                testSet.append(data2[x])
            else:
                trainingSet.append(data2[x])
        for x in range(len(data3)):
            if (x >= (0.1 * len(data3)) * i) and (x < (0.1 * len(data3)) * (i + 1)):
                testSet.append(data3[x])
            else:
                trainingSet.append(data3[x])
        print("Training set size: " + str(len(trainingSet)))
        print("Test set size: " + str(len(testSet)))
        predictions = []
        k = 1
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
        accuracy = getAccuracy(testSet, predictions)
        print("Fold " + str(i) + "    Accuracy: " + str(accuracy) + '%')
        total_accuracy += accuracy
    print("Average accuracy: " + str(total_accuracy / 10) + '%')
if __name__ == "__main__":
    main()