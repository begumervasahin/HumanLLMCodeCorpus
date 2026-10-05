from math import sqrt
import time
def euclidean_distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
def knn(test_data, data_set, labels, k):
    distances = [euclidean_distance(test_data, x) for x in data_set]
    nearest_indices = sorted(range(len(distances)), key=lambda x: distances[x])[:k]
    nearest_labels = [labels[x] for x in nearest_indices]
    return max(nearest_labels, key=nearest_labels.count)
t1 = time.time()
group = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
labels = ['A', 'A', 'B', 'B']
test = [1.0, 1.1]
result = knn(test, group, labels, 3)
print("Execution time:", time.time() - t1)
print("Result:", result)