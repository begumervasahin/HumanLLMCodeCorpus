import time
from math import sqrt
from collections import Counter
group = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
labels = ['A', 'A', 'B', 'B']
test = [1.0, 1.1]
k = 3
start_time = time.time()
def euclidean_distance(point1, point2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
def knn(test_data, data_set, labels, k):
    distances = [euclidean_distance(test_data, point) for point in data_set]
    k_nearest_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:k]
    k_nearest_labels = [labels[i] for i in k_nearest_indices]
    most_common_label = Counter(k_nearest_labels).most_common(1)[0][0]
    return most_common_label
result = knn(test, group, labels, k)
print(f"Time taken: {time.time() - start_time:.6f} seconds")
print(f"Predicted label: {result}")
verification_result = knn([1.0, 1.1], [[1.0, 1.0], [0.0, 0.0], [0.0, 0.1]], ['A', 'B', 'B'], 3)
print(f"Verification result: {verification_result}")