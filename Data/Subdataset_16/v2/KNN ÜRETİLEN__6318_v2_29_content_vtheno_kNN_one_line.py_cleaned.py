import time
from math import sqrt
from collections import Counter
b1 = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
b2 = ['A', 'A', 'B', 'B']
b3 = [1.0, 1.1]
a1 = 3
b4 = time.time()
def fonk1(point1, point2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
def fonk2(test_data, data_set, b2, a1):
    b5 = [fonk1(test_data, point) for point in data_set]
    b6 = sorted(range(len(b5)), key=lambda i: b5[i])[:a1]
    b7 = [b2[i] for i in b6]
    b8 = Counter(b7).most_common(1)[0][0]
    return b8
b9 = fonk2(b3, b1, b2, a1)
print(f"Time taken: {time.time() - b4:.6f} seconds")
print(f"Predicted label: {b9}")
b10 = fonk2([1.0, 1.1], [[1.0, 1.0], [0.0, 0.0], [0.0, 0.1]], ['A', 'B', 'B'], 3)
print(f"Verification b9: {b10}")