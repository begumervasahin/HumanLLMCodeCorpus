import csv
import math
import operator
def calculate_distance(set1, set2, length):
    distance = 0
    for x in range(length):
        distance += (set1[x] - set2[x]) ** 2
    return math.sqrt(distance)
def find_neighbors(training_data, test_sample, k):
    distances = []
    length = len(test_sample)
    for data in training_data:
        dist = calculate_distance(test_sample, data, length)
        distances.append((data, dist))
    distances.sort(key=operator.itemgetter(1))
    nearest_neighbors = [distances[x][0] for x in range(k)]
    return nearest_neighbors
def make_prediction(neighbors):
    label_counts = {}
    for neighbor in neighbors:
        label = neighbor[-1]
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    sorted_labels = sorted(label_counts.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_labels[0][0]
def main():
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        training_data = []
        for row in reader:
            for y in range(3):
                row[y] = float(row[y])
            if row[3] == 'M':
                row[3] = 1
            else:
                row[3] = 2
            training_data.append(row)
    k = int(input('Enter number of neighbors to use: '))
    test_sample = [float(x) for x in input('Enter data to be predicted (comma separated values): ').split(',')]
    nearest_neighbors = find_neighbors(training_data, test_sample, k)
    result = make_prediction(nearest_neighbors)
    print('Nearest neighbors:')
    for neighbor in nearest_neighbors:
        print(neighbor)
    print('Prediction for gender with given data:')
    if result == 1:
        print('M')
    else:
        print('F')
if __name__ == "__main__":
    main()