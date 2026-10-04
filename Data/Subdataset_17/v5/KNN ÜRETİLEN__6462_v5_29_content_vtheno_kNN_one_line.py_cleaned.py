import time
from math import sqrt
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
def knn(test_point, data_set, labels, k):
    distances = [(euclidean_distance(test_point, point), label) for point, label in zip(data_set, labels)]
    distances.sort(key=lambda x: x[0])
    k_nearest_labels = [label for _, label in distances[:k]]
    label_count = {label: k_nearest_labels.count(label) for label in set(k_nearest_labels)}
    most_common_label = max(label_count, key=label_count.get)
    return most_common_label
if __name__ == "__main__":
    start_time = time.time()
    data_set = [
        [1.0, 1.1],
        [1.0, 1.0],
        [0.0, 0.0],
        [0.0, 0.1]
    ]
    labels = ['A', 'A', 'B', 'B']
    test_point = [1.0, 1.1]
    result = knn(test_point, data_set, labels, 3)
    print(f"Result: {result}")
    print(f"Time taken: {time.time() - start_time:.6f} seconds")