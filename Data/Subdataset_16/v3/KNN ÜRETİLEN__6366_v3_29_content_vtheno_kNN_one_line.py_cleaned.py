import time
from math import sqrt
from collections import Counter
def fonk1(point1, point2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
def fonk2(test_data, data_set, b6, a1):
    b1 = [fonk1(test_data, point) for point in data_set]
    b2 = sorted(range(len(b1)), key=lambda i: b1[i])[:a1]
    b3 = [b6[i] for i in b2]
    b4 = Counter(b3).most_common(1)[0][0]
    return b4
def fonk3():
    b5 = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
    b6 = ['A', 'A', 'B', 'B']
    b7 = [1.0, 1.1]
    a1 = 3
    b8 = time.time()
    b9 = fonk2(b7, b5, b6, a1)
    print(f"Time taken: {time.time() - b8:.6f} seconds")
    print(f"Predicted label: {b9}")
    b10 = fonk2([1.0, 1.1], [[1.0, 1.0], [0.0, 0.0], [0.0, 0.1]], ['A', 'B', 'B'], 3)
    print(f"Verification b9: {b10}")
if b11 = = "__main__":
    fonk3()