import csv
import math
import operator
def calcdistance(set1, set2, length):
    distance = 0
    for x in range(length):
        distance += pow((set1[x] - set2[x]), 2)
    return math.sqrt(distance)
def neighbors(givendata, sample, k):
    distances = []
    length = len(sample)
    for x in range(len(givendata)):
        dist = calcdistance(sample, givendata[x], length)
        distances.append((givendata[x], dist))
    distances.sort(key=operator.itemgetter(1))
    nearestneighbors = []
    for x in range(k):
        nearestneighbors.append(distances[x][0])
    return nearestneighbors
def predict(neighbors):
    labels = {}
    for x in range(len(neighbors)):
        label = neighbors[x][-1]
        if label in labels:
            labels[label] += 1
        else:
            labels[label] = 1
    prediction = sorted(labels.items(), key=operator.itemgetter(1), reverse=True)
    return prediction[0][0]
def main():
    with open('data.csv', 'r') as csvfile:
        indata = csv.reader(csvfile)
        trdata = list(indata)
        for x in range(len(trdata)):
            for y in range(3):
                if y == 3:
                    if trdata[x][y] == 'M':
                        trdata[x][y] = 1
                    else:
                        trdata[x][y] = 2
                trdata[x][y] = float(trdata[x][y])
    k = int(input('Enter number of neighbors to use: '))
    testSet = list(map(float, input('Enter data to be predicted (comma-separated): ').split(',')))
    kNearneighbors = neighbors(trdata, testSet, k)
    result = predict(kNearneighbors)
    print('Nearest neighbors are:')
    print(kNearneighbors)
    print('Prediction for gender with given data is:')
    if result == 1:
        print('M')
    else:
        print('W')
if __name__ == "__main__":
    main()