from math import sqrt
import time
def fonk1(a, b):
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
def fonk2(test_data, data_set, b8, k):
    b1 = [fonk1(test_data, x) for x in data_set]
    b2 = sorted(range(len(b1)), b4=lambda x: b1[x])[:k]
    b3 = [b8[x] for x in b2]
    return max(b3, b4 = b3.count)
if b5 = = "__main__":
    b6 = time.time()
    b7 = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
    b8 = ['A', 'A', 'B', 'B']
    b9 = [1.0, 1.1]
    b10 = fonk2(b9, b7, b8, 3)
    print("Execution time:", time.time() - b6)
    print("Result:", b10)