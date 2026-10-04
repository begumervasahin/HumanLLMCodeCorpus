
import numpy as np
from os import listdir
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
    sorted_class_count = sorted(class_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_class_count[0][0]
def image_to_vector(file_name):
    vector = np.zeros((1, 1024))
    with open(file_name) as img_file:
        for i in range(32):
            line = img_file.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
    return vector
def handwriting_recognition_test():
    labels = []
    training_files = listdir('digits/trainingDigits')
    num_training_samples = len(training_files)
    training_matrix = np.zeros((num_training_samples, 1024))
    for i, file_name in enumerate(training_files):
        class_label = int(file_name.split('_')[0])
        labels.append(class_label)
        training_matrix[i, :] = image_to_vector(f'digits/trainingDigits/{file_name}')
    test_files = listdir('digits/testDigits')
    num_test_samples = len(test_files)
    error_count = 0.0
    for file_name in test_files:
        class_label = int(file_name.split('_')[0])
        test_vector = image_to_vector(f'digits/testDigits/{file_name}')
        predicted_label = knn_classifier(test_vector, training_matrix, labels, 3)
        print(f'The KNN classified result is: {predicted_label}, the actual class is: {class_label}')
        if predicted_label != class_label:
            error_count += 1
    print(f'\nThe total number of incorrectly classified samples is: {error_count}')
    print(f'The error rate is: {error_count / num_test_samples:.6f}')
if __name__ == '__main__':
    handwriting_recognition_test()