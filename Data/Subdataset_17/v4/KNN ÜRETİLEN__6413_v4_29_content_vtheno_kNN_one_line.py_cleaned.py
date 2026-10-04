import time
from math import sqrt
def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
def knn(test_data, data_set, labels, k):
    distances = [(euclidean_distance(test_data, point), label) for point, label in zip(data_set, labels)]
    distances.sort(key=lambda x: x[0])
    k_nearest_labels = [label for _, label in distances[:k]]
    label_count = {label: k_nearest_labels.count(label) for label in set(k_nearest_labels)}
    most_common_label = max(label_count, key=label_count.get)
    return most_common_label
if __name__ == "__main__":
    start_time = time.time()
    group = [
        [1.0, 1.1],
        [1.0, 1.0],
        [0.0, 0.0],
        [0.0, 0.1]
    ]
    labels = ['A', 'A', 'B', 'B']
    test_point = [1.0, 1.1]
    result = knn(test_point, group, labels, 3)
    print(f"Result: {result}")
    print(f"Time taken: {time.time() - start_time:.6f} seconds")