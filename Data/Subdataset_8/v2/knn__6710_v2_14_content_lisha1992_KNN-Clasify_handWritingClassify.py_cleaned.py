import numpy as np
import os
def KNNClassifier(unlabeled_data, data_set, labels, k):
    distances = np.sqrt(np.sum((data_set - unlabeled_data) ** 2, axis=1))
    sorted_indices = np.argsort(distances)
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    max_vote_class = max(class_count.items(), key=lambda x: x[1])[0]
    return max_vote_class
def image_to_vector(file_name):
    vector = np.zeros((1, 1024))
    with open(file_name) as img_file:
        for i in range(32):
            line_string = img_file.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line_string[j])
    return vector
def handwriting_recognition_test():
    train_sample_list = os.listdir('digits/trainingDigits')
    train_sample_count = len(train_sample_list)
    train_mat = np.zeros((train_sample_count, 1024))
    hand_writing_labels = []
    for i, file_name_str in enumerate(train_sample_list):
        file_str = file_name_str.split('.')[0]
        class_str = int(file_str.split('_')[0])
        hand_writing_labels.append(class_str)
        train_mat[i, :] = image_to_vector('digits/trainingDigits/' + file_name_str)
    test_sample_list = os.listdir('digits/testDigits')
    len_test = len(test_sample_list)
    error_count = 0.0
    for file_name_str in test_sample_list:
        file_str = file_name_str.split('.')[0]
        class_str = int(file_str.split('_')[0])
        vector_for_test = image_to_vector('digits/testDigits/' + file_name_str)
        classified_result = KNNClassifier(vector_for_test, train_mat, hand_writing_labels, 3)
        print(f'The classified result by KNN is: {classified_result}, the actual class is: {class_str}')
        if classified_result != class_str:
            error_count += 1
    print(f'\nThe total number of incorrectly classified samples is: {error_count}')
    print(f'\nThe error rate is: {error_count / len_test:.4f}')
handwriting_recognition_test()