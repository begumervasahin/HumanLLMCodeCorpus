import numpy as np
import operator
a = 1
b = 2
c = a + b
print(f"Sum of a and b: {c}")
b = np.array([6, 7, 8])
c = b.shape[0]
print(f"Shape of array b: {c}")
a = np.sum([[0, 1, 2], [2, 1, 3]])
print(f"Sum of all elements: {a}")
a = np.sum([[0, 1, 2], [2, 1, 3]], axis=0)
print(f"Sum along axis 0: {a}")
a = np.sum([[8, 1, 2], [2, 1, 3], [0, 0, 0]], axis=1)
print(f"Sum along axis 1: {a}")
sorted_indices = a.argsort()
print(f"Indices of sorted array a: {sorted_indices}")
class_count = {"A": 6, "B": 1, "C": 0, "D": 2}
sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
print(f"Dictionary sorted by value: {sorted_class_count}")
f = np.array([[5, 8], [1, 2]])
def img_to_vector(array):
    my_vector = np.zeros((1, 4))
    for i in range(2):
        for j in range(2):
            my_vector[0, 2*i + j] = int(array[i, j])
    return my_vector
my_vector = img_to_vector(f)
print(f"Converted vector: {my_vector[0, 1]}")