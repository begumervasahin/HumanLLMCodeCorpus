from math import sqrt
import time
distance = lambda a, b: sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
def knn(testdata, dataSet, label, k):
    distances = map(lambda x: distance(testdata, x), dataSet)
    nearest_indices = sorted(range(len(distances)), key=lambda x: distances[x])[:k]
    nearest_labels = map(lambda x: label[x], nearest_indices)
    return max(nearest_labels, key=nearest_labels.count)
t1 = time.clock()
group = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
labels = ['A', 'A', 'B', 'B']
test = [1.0, 1.1]
result = knn(test, group, labels, 3)
print("Execution time:", time.clock() - t1)
print("Result:", result)