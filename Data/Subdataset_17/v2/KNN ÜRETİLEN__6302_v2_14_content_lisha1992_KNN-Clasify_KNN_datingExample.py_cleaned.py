
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
def knn_classifier(unlabeled_sample, dataset, labels, k):
    num_samples = dataset.shape[0]
    diff = np.tile(unlabeled_sample, (num_samples, 1)) - dataset
    sq_diff = diff ** 2
    sq_dist = np.sum(sq_diff, axis=1)
    distances = np.sqrt(sq_dist)
    sorted_dist_indices = np.argsort(distances)
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=itemgetter(1), reverse=True)
    return sorted_class_count[0][0]
def file_to_matrix(filename, num_features):
    with open(filename) as file:
        lines = file.readlines()
    num_lines = len(lines)
    dataset = np.zeros((num_lines, num_features))
    labels = []
    for index, line in enumerate(lines):
        line = line.strip()
        elements = line.split('\t')
        dataset[index, :] = elements[:num_features]
        labels.append(int(elements[-1]))
    return dataset, labels
def draw_scatter_plot(data_matrix, labels):
    plt.figure()
    plt.scatter(data_matrix[:, 0], data_matrix[:, 1],
                s=15.0 * np.array(labels),
                c=15.0 * np.array(labels))
    plt.show()
def normalize_data(dataset):
    min_values = dataset.min(0)
    max_values = dataset.max(0)
    ranges = max_values - min_values
    norm_dataset = (dataset - min_values) / ranges
    return norm_dataset, ranges, min_values
def dating_class_test():
    test_ratio = 0.1
    dataset, labels = file_to_matrix('datingTestSet2.txt', 3)
    norm_dataset, ranges, min_values = normalize_data(dataset)
    num_test_vectors = int(norm_dataset.shape[0] * test_ratio)
    error_count = 0.0
    for i in range(num_test_vectors):
        result = knn_classifier(norm_dataset[i, :],
                                norm_dataset[num_test_vectors:],
                                labels[num_test_vectors:],
                                3)
        print(f'Result from KNN Classifier: {result}, Actual class: {labels[i]}')
        if result != labels[i]:
            error_count += 1
    print(f'Total error rate: {error_count / num_test_vectors:.2f}')
def classify_person():
    results = ['not at all', 'in small doses', 'in large doses']
    percent_time_game = float(input('Percentage of time spent playing video games? '))
    frequent_flyer_miles = float(input('Frequent flier miles earned per year? '))
    ice_cream_consumed = float(input('Liters of ice cream consumed per year? '))
    dataset, labels = file_to_matrix('datingTestSet2.txt', 3)
    norm_dataset, ranges, min_values = normalize_data(dataset)
    input_array = np.array([percent_time_game, frequent_flyer_miles, ice_cream_consumed])
    normalized_input = (input_array - min_values) / ranges
    result = knn_classifier(normalized_input, norm_dataset, labels, 3)
    print(f'You will probably like this person: {results[result - 1]}')
if __name__ == '__main__':
    classify_person()