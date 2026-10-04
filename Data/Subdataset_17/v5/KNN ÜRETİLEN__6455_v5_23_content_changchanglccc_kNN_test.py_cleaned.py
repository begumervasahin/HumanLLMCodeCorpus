import numpy as np
import operator
a = 1
b = 2
c = a + b
print(c)
array_b = np.array([6, 7, 8])
array_b_shape = array_b.shape[0]
print(array_b_shape)
sum_all_elements = np.sum([[0, 1, 2], [2, 1, 3]])
print(sum_all_elements)
sum_axis_0 = np.sum([[0, 1, 2], [2, 1, 3]], axis=0)
print(sum_axis_0)
sum_axis_1 = np.sum([[8, 1, 2], [2, 1, 3], [0, 0, 0]], axis=1)
print(sum_axis_1)
argsorted_indices = sum_axis_1.argsort()
print(argsorted_indices)
class_count = {"A": 6, "B": 1, "C": 0, "D": 2}
sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_class_count)
array_f = np.array([[5, 8], [1, 2]])
def img_to_vector(matrix):
    rows, cols = matrix.shape
    vector = np.zeros((1, rows * cols))
    for i in range(rows):
        for j in range(cols):
            vector[0, cols * i + j] = int(matrix[i, j])
    return vector
vector_f = img_to_vector(array_f)
print(vector_f)
zero_vector = np.zeros((1, 4))
print(zero_vector[0, 1])
