from numpy import loadtxt, zeros, tile, argsort, sum, sqrt
import operator
def main():
    features, labels = load_dataset()
    test_features = zeros((30, 4))
    test_labels = zeros(30)
    train_features = zeros((120, 4))
    train_labels = zeros(120)
    for i in range(3):
        test_features[i * 10: i * 10 + 10] = features[i * 50: i * 50 + 10]
        test_labels[i * 10: i * 10 + 10] = labels[i * 50: i * 50 + 10]
        train_features[i * 10: i * 10 + 40] = features[i * 50: i * 50 + 40]
        train_labels[i * 10: i * 10 + 40] = labels[i * 50: i * 50 + 40]
    error_count = knn_classification(test_features, train_features, train_labels, k=5)
    error_rate = error_count / float(30)
    print(f"The total error rate is: {error_rate:.2%}")
def load_dataset():
    iris_data = loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    features = iris_data[:, 1:5]
    labels = iris_data[:, 5].astype(int)
    return features, labels
def knn_classification(inX, dataset, labels, k):
    distances = calculate_distances(inX, dataset)
    sorted_indices = argsort(distances)
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]
def calculate_distances(inX, dataset):
    diff_mat = tile(inX, (dataset.shape[0], 1)) - dataset
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sqrt(sq_distances)
    return distances
if __name__ == '__main__':
    main()