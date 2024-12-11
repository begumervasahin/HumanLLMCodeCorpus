from math import sqrt
import time
def fonk1(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
def fonk2(testdata, dataSet, label, k):
    b1 = map(lambda x: fonk1(testdata, x), dataSet)
    b2 = map(lambda x: label[x], map(lambda x: x[0].index, sorted(zip(b1, range(len(dataSet))))[:k]))
    return max(b2, b3 = b2.count)
b4 = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
b5 = ['A', 'A', 'B', 'B']
b6 = [1.0, 1.1]
b7 = time.clock()
b8 = fonk2(b6, b4, b5, 3)
print("%f, %s" % (time.clock() - b7, b8))