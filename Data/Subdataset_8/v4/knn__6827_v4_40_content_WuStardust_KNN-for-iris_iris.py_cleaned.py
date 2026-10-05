import numpy as np
import operator
def main():
    features, labels = load_data_set()
    test_features = np.zeros((30, 4))
    test_labels = np.zeros(30)
    train_features = np.zeros((120, 4))
    train_labels = np.zeros(120)
    for i in range(3):
        test_features[i * 10: i * 10 + 10] = features[i * 50: i * 50 + 10]
        test_labels[i * 10: i * 10 + 10] = labels[i * 50: i * 50 + 10]
        train_features[i * 10: i * 10 + 40] = features[i * 50: i * 50 + 40]
        train_labels[i * 10: i * 10 + 40] = labels[i * 50: i * 50 + 40]
    error_count = 0
    for i in range(30):
        classifier_result = classifier_knn(test_features[i], train_features, train_labels, 5)
        print("The classifier came back with: %d, the real answer is: %d" % (classifier_result, test_labels[i]))
        if classifier_result != test_labels[i]:
            error_count += 1
    print("The total error rate is: %f" % (error_count / float(30)))
def load_data_set():
    iris_data = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    features = iris_data[:, 1:5]
    labels = iris_data[:, 5].astype(int)
    return features, labels
def classifier_knn(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = np.tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distance = sq_diff_mat.sum(axis=1)
    distance = sq_distance ** 0.5
    sorted_dist_indices = distance.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]
if __name__ == "__main__":
    main()