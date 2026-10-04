import csv
import math
import operator
def calculate_distance(set1, set2, length):
    return math.sqrt(sum((set1[x] - set2[x]) ** 2 for x in range(length)))
def find_neighbors(training_data, test_sample, k):
    distances = [(data, calculate_distance(test_sample, data, len(test_sample))) for data in training_data]
    distances.sort(key=operator.itemgetter(1))
    return [distances[x][0] for x in range(k)]
def make_prediction(neighbors):
    label_counts = {}
    for neighbor in neighbors:
        label = neighbor[-1]
        label_counts[label] = label_counts.get(label, 0) + 1
    return max(label_counts.items(), key=operator.itemgetter(1))[0]
def load_training_data(filename):
    training_data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row[:3] = map(float, row[:3])
            row[3] = 1 if row[3] == 'M' else 2
            training_data.append(row)
    return training_data
def main():
    training_data = load_training_data('data.csv')
    k = int(input('Enter number of neighbors to use: '))
    test_sample = [float(x) for x in input('Enter data to be predicted (comma separated values): ').split(',')]
    nearest_neighbors = find_neighbors(training_data, test_sample, k)
    result = make_prediction(nearest_neighbors)
    print('Nearest neighbors:')
    for neighbor in nearest_neighbors:
        print(neighbor)
    print('Prediction for gender with given data:')
    print('M' if result == 1 else 'F')
if __name__ == "__main__":
    main()