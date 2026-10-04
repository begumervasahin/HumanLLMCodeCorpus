import numpy as np
import operator
a = 1
b = 2
c = a + b
print(f"Sum of a and b: {c}")
array_b = np.array([6, 7, 8])
shape_b = array_b.shape[0]
print(f"Shape of array b: {shape_b}")
sum_all_elements = np.sum([[0, 1, 2], [2, 1, 3]])
print(f"Sum of all elements: {sum_all_elements}")
sum_axis_0 = np.sum([[0, 1, 2], [2, 1, 3]], axis=0)
print(f"Sum along axis 0: {sum_axis_0}")
sum_axis_1 = np.sum([[8, 1, 2], [2, 1, 3], [0, 0, 0]], axis=1)
print(f"Sum along axis 1: {sum_axis_1}")
sorted_indices = sum_axis_1.argsort()
print(f"Indices of sorted array along axis 1: {sorted_indices}")
class_count = {"A": 6, "B": 1, "C": 0, "D": 2}
sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
print(f"Dictionary sorted by value: {sorted_class_count}")
array_f = np.array([[5, 8], [1, 2]])
def img_to_vector(array):
    vector_length = array.shape[0] * array.shape[1]
    my_vector = np.zeros((1, vector_length))
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            my_vector[0, array.shape[1]*i + j] = array[i, j]
    return my_vector
converted_vector = img_to_vector(array_f)
print(f"Converted vector: {converted_vector[0, 1]}")