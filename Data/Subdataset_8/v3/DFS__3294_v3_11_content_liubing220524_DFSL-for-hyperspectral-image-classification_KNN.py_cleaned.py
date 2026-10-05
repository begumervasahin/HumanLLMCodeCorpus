import time
import numpy as np
import scipy.io as sio
from sklearn.neighbors import KNeighborsClassifier
import input_data
import pickle
def load_data(file_path, num_labeled):
    return input_data.read_data_sets(file_path, num_labeled)
def train_classifier(data, labels):
    clf = KNeighborsClassifier(n_neighbors=1)
    clf.fit(data, labels)
    return clf
def print_scores(train_score, test_score):
    print('Training score: {:.2f}'.format(train_score))
    print('Testing score: {:.2f}'.format(test_score))
def predict_labels(classifier, test_data):
    return classifier.predict(test_data)
def load_ground_truth_indices(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)
def map_labels_to_result(predictions, ground_truth_indices, m, n):
    final_result = np.zeros((m, n), dtype=np.int8).reshape(m * n)
    final_result[ground_truth_indices] = predictions + 1
    return final_result.reshape(m, n)
def save_result(file_path, result):
    sio.savemat(file_path, {'final_result': result})
if __name__ == "__main__":
    start_time = time.time()
    num_labeled = 5
    dataSet = load_data('I_feature.h5', num_labeled)
    train_data, train_label = dataSet.train.images, dataSet.train.labels
    test_data, test_label = dataSet.test.images, dataSet.test.labels
    print('Training the KNN classifier...')
    clf = train_classifier(train_data, train_label)
    train_score = clf.score(train_data, train_label)
    test_score = clf.score(test_data, test_label)
    print_scores(train_score, test_score)
    elapsed_time = time.time() - start_time
    print('Time taken:', elapsed_time)
    print('Predicting labels for test data...')
    label_predictions = predict_labels(clf, test_data)
    print('Loading ground truth indices...')
    ground_truth_indices = load_ground_truth_indices('./gt_I.data')
    m, n = 145, 145
    final_result = map_labels_to_result(label_predictions, ground_truth_indices, m, n)
    print('Saving the final result...')
    save_result('I-25.mat', final_result)