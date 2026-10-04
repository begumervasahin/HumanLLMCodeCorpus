import time
from math import sqrt
b1 = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
b2 = ['A', 'A', 'B', 'B']
b3 = [1.0, 1.1]
a1 = 3
b4 = time.time()
b5 = lambda a, b: sqrt((lambda x, y: x + y)(
    pow((lambda x, y: abs(x - y))(a[0], b[0]), 2.0),
    pow((lambda x, y: abs(x - y))(a[1], b[1]), 2.0)
))
b6 = (lambda testdata, dataSet, label, a1:
    (lambda x: x[0][x[1].index(max(x[1]))])
    ((lambda x: [x, list(map(x.count, x))])
    (list(map(lambda x: label[x],
    (lambda x: list(map(x[0].index, x[1][:a1])))
    ((lambda lst: [lst, sorted(lst)])
    ((lambda b5: list(map(lambda x: b5(testdata, x), dataSet)))
    (b5)
    ))))))
)(b3, b1, b2, a1)
print("%f, %s" % (time.time() - b4, b6))
b7 = (lambda testdata, dataSet, label, a1:
    (lambda x: x[0][x[1].index(max(x[1]))])
    ((lambda x: [x, list(map(x.count, x))])
    (list(map(lambda x: label[x],
    (lambda x: list(map(x[0].index, x[1][:a1])))
    ((lambda lst: [lst, sorted(lst)])
    ((lambda b5: list(map(lambda x: b5(testdata, x), dataSet)))
    (b5)
    ))))))
)([1.0, 1.1], [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]], ['A', 'A', 'B', 'B'], 3)
print(b7)