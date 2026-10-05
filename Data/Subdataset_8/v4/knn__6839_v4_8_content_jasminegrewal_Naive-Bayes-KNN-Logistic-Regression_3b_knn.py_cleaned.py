import csv
import math
import operator
def calculate_distance(set1, set2, length):
    distance = 0
    for x in range(length):
        distance += pow((set1[x] - set2[x]), 2)
    return math.sqrt(distance)
def find_neighbors(training_data, sample, k):
    distances = []
    length = len(sample)
    for x in range(len(training_data)):
        dist = calculate_distance(sample, training_data[x], length)
        distances.append((training_data[x], dist))
    distances.sort(key=operator.itemgetter(1))
    nearest_neighbors = [dist[0] for dist in distances[:k]]
    return nearest_neighbors
def predict_gender(neighbors):
    labels = {}
    for neighbor in neighbors:
        label = neighbor[-1]
        if label in labels:
            labels[label] += 1
        else:
            labels[label] = 1
    sorted_labels = sorted(labels.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_labels[0][0]
def preprocess_data(data):
    for entry in data:
        for i in range(3):
            if i == 2:
                if entry[i] == 'M':
                    entry[i] = 1
                else:
                    entry[i] = 0
            entry[i] = float(entry[i])
    return data
def main():
    with open('data.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        training_data = list(csv_reader)
        training_data = preprocess_data(training_data)
    k = int(input('Enter the number of neighbors to use: '))
    test_data = [float(x) for x in input('Enter the data to be predicted: ').split()]
    nearest_neighbors = find_neighbors(training_data, test_data, k)
    result = predict_gender(nearest_neighbors)
    print('Nearest neighbors are:')
    for neighbor in nearest_neighbors:
        print(neighbor)
    print('Prediction for gender with given data is:')
    if result == 1:
        print('Male')
    else:
        print('Female')
if __name__ == '__main__':
    main()