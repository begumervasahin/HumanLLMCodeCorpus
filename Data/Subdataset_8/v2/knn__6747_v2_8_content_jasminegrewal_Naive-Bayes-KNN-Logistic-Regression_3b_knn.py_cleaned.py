import csv
import math
import operator
def calculate_distance(set1, set2, length):
    distance = 0
    for x in range(length):
        distance += pow((set1[x] - set2[x]), 2)
    return math.sqrt(distance)
def find_neighbors(training_data, test_sample, k):
    distances = []
    length = len(test_sample)
    for x in range(len(training_data)):
        dist = calculate_distance(test_sample, training_data[x], length)
        distances.append((training_data[x], dist))
    distances.sort(key=operator.itemgetter(1))
    nearest_neighbors = []
    for x in range(k):
        nearest_neighbors.append(distances[x][0])
    return nearest_neighbors
def predict_class(neighbors):
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
        data_reader = csv.reader(csvfile)
        training_data = [list(map(float, row)) for row in data_reader]
    k = int(input('Enter the number of neighbors to consider: '))
    test_sample = [float(x) for x in input('Enter data to be predicted (separated by spaces): ').split()]
    k_nearest_neighbors = find_neighbors(training_data, test_sample, k)
    predicted_class = predict_class(k_nearest_neighbors)
    print('Nearest neighbors are:')
    print(k_nearest_neighbors)
    print('Predicted class based on given data is:')
    if predicted_class == 1:
        print('M')
    else:
        print('W')
if __name__ == "__main__":
    main()