import numpy as np
import operator
def load_data_set():
    iris = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    features = iris[:, 1:5]
    labels = iris[:, 5].astype(int)
    return features, labels
def knn_classifier(inX, dataSet, labels, k):
    distances = np.sqrt(((dataSet - inX) ** 2).sum(axis=1))
    sorted_dist_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]
def main():
    features, labels = load_data_set()
    test_features = np.zeros((30, 4))
    test_labels = np.zeros(30)
    train_features = np.zeros((120, 4))
    train_labels = np.zeros(120)
    for i in range(3):
        start, end = i * 50, i * 50 + 50
        test_features[i * 10: i * 10 + 10] = features[start: start + 10]
        test_labels[i * 10: i * 10 + 10] = labels[start: start + 10]
        train_features[i * 40: i * 40 + 40] = features[start + 10: end]
        train_labels[i * 40: i * 40 + 40] = labels[start + 10: end]
    error_count = 0
    for i in range(30):
        classifier_result = knn_classifier(test_features[i], train_features, train_labels, 5)
        real_label = test_labels[i]
        print(f"The classifier came back with: {classifier_result}, the real answer is: {real_label}")
        if classifier_result != real_label:
            error_count += 1
    print(f"The total error rate is: {error_count / 30.0:.2%}")
if __name__ == "__main__":
    main()