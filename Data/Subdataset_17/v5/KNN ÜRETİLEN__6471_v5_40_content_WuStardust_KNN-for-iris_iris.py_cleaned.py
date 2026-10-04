import numpy as np
import operator
def main():
    features, labels = load_dataset()
    test_features = np.zeros((30, 4))
    test_labels = np.zeros(30)
    train_features = np.zeros((120, 4))
    train_labels = np.zeros(120)
    for i in range(3):
        test_features[i * 10: i * 10 + 10] = features[i * 50: i * 50 + 10]
        test_labels[i * 10: i * 10 + 10] = labels[i * 50: i * 50 + 10]
        train_features[i * 10 * 4: i * 10 * 4 + 40] = features[i * 50 + 10: i * 50 + 50]
        train_labels[i * 10 * 4: i * 10 * 4 + 40] = labels[i * 50 + 10: i * 50 + 50]
    error_count = 0
    for i in range(30):
        classifier_result = knn_classifier(test_features[i], train_features, train_labels, 5)
        print(f"The classifier came back with: {classifier_result}, the real answer is: {test_labels[i]}")
        if classifier_result != test_labels[i]:
            error_count += 1
    print(f"The total error rate is: {error_count / float(30):.2f}")
def load_dataset():
    iris = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    features = iris[:, 1:5]
    labels = iris[:, 5].astype(int)
    return features, labels
def knn_classifier(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = np.tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_dist_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]
if __name__ == "__main__":
    main()