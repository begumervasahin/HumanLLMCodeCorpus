import csv
import math
import operator
def calculate_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
def find_neighbors(training_data, sample, k):
    distances = [(data, calculate_distance(sample, data[:-1])) for data in training_data]
    distances.sort(key=operator.itemgetter(1))
    nearest_neighbors = [data for data, _ in distances[:k]]
    return nearest_neighbors
def predict_gender(neighbors):
    labels = {}
    for neighbor in neighbors:
        label = neighbor[-1]
        labels[label] = labels.get(label, 0) + 1
    sorted_labels = sorted(labels.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_labels[0][0]
def preprocess_data(data):
    for entry in data:
        entry[2] = 1 if entry[2] == 'M' else 0
        entry[:2] = map(float, entry[:2])
    return data
def main():
    with open('data.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        training_data = preprocess_data(list(csv_reader))
    k = int(input('Enter the number of neighbors to use: '))
    test_data = list(map(float, input('Enter the data to be predicted: ').split()))
    nearest_neighbors = find_neighbors(training_data, test_data, k)
    result = predict_gender(nearest_neighbors)
    print('Nearest neighbors are:')
    for neighbor in nearest_neighbors:
        print(neighbor)
    print('Prediction for gender with given data is:')
    print('Male' if result == 1 else 'Female')
if __name__ == '__main__':
    main()