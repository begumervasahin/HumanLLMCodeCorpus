from math import sqrt
import time
b1 = lambda a, b: sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
def fonk1(testdata, dataSet, label, k):
    b2 = map(lambda x: b1(testdata, x), dataSet)
    b3 = sorted(range(len(b2)), b5=lambda x: b2[x])[:k]
    b4 = map(lambda x: label[x], b3)
    return max(b4, b5 = b4.count)
b6 = time.clock()
b7 = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
b8 = ['A', 'A', 'B', 'B']
b9 = [1.0, 1.1]
b10 = fonk1(b9, b7, b8, 3)
print("Execution time:", time.clock() - b6)
print("Result:", b10)