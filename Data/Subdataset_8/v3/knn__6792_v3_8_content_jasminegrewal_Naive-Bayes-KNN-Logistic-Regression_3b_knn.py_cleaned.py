import csv
import math
import operator
def calculate_distance(set1, set2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(set1, set2)))
def find_neighbors(training_data, test_sample, k):
    distances = [(train_sample, calculate_distance(test_sample, train_sample[:-1])) for train_sample in training_data]
    distances.sort(key=operator.itemgetter(1))
    return [distance[0] for distance in distances[:k]]
def predict_class(neighbors):
    labels = {}
    for neighbor in neighbors:
        label = neighbor[-1]
        labels[label] = labels.get(label, 0) + 1
    return max(labels.items(), key=operator.itemgetter(1))[0]
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
    print('Predicted class based on given data is:', 'M' if predicted_class == 1 else 'W')
if __name__ == "__main__":
    main()