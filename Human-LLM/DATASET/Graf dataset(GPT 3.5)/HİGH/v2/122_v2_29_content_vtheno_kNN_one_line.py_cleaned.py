from math import sqrt
import time
def fonk1(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
def fonk2(test_data, data_set, b7, k):
    b1 = [fonk1(test_data, x) for x in data_set]
    b2 = sorted(range(len(b1)), b4=lambda x: b1[x])[:k]
    b3 = [b7[x] for x in b2]
    return max(b3, b4 = b3.count)
b5 = time.time()
b6 = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
b7 = ['A', 'A', 'B', 'B']
b8 = [1.0, 1.1]
b9 = fonk2(b8, b6, b7, 3)
print("Execution time:", time.time() - b5)
print("Result:", b9)