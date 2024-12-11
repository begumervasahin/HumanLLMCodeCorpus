from math import sqrt
import time
def fonk1(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
def fonk2(test_data, data_set, b6, k):
    b1 = [fonk1(test_data, x) for x in data_set]
    b2 = sorted(range(len(data_set)), b4=lambda x: b1[x])[:k]
    b3 = [b6[i] for i in b2]
    return max(b3, b4 = b3.count)
b5 = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
b6 = ['A', 'A', 'B', 'B']
b7 = [1.0, 1.1]
b8 = time.clock()
b9 = fonk2(b7, b5, b6, 3)
print(f"Time taken: {time.clock() - b8}")
print(f"Result: {b9}")