import time
from math import sqrt
group = [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]]
labels = ['A', 'A', 'B', 'B']
test = [1.0, 1.1]
k = 3
t1 = time.time()
distance = lambda a, b: sqrt((lambda x, y: x + y)(
    pow((lambda x, y: abs(x - y))(a[0], b[0]), 2.0),
    pow((lambda x, y: abs(x - y))(a[1], b[1]), 2.0)
))
result = (lambda testdata, dataSet, label, k:
    (lambda x: x[0][x[1].index(max(x[1]))])
    ((lambda x: [x, list(map(x.count, x))])
    (list(map(lambda x: label[x],
    (lambda x: list(map(x[0].index, x[1][:k])))
    ((lambda lst: [lst, sorted(lst)])
    ((lambda distance: list(map(lambda x: distance(testdata, x), dataSet)))
    (distance)
    ))))))
)(test, group, labels, k)
print("%f, %s" % (time.time() - t1, result))
verification_result = (lambda testdata, dataSet, label, k:
    (lambda x: x[0][x[1].index(max(x[1]))])
    ((lambda x: [x, list(map(x.count, x))])
    (list(map(lambda x: label[x],
    (lambda x: list(map(x[0].index, x[1][:k])))
    ((lambda lst: [lst, sorted(lst)])
    ((lambda distance: list(map(lambda x: distance(testdata, x), dataSet)))
    (distance)
    ))))))
)([1.0, 1.1], [[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]], ['A', 'A', 'B', 'B'], 3)
print(verification_result)