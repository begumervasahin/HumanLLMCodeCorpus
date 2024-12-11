import math
import sys
def fonk1(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
def fonk2(test_point, b9, k):
    b1 = [(fonk1(train_point[:-1], test_point), train_point[-1]) for train_point in b9]
    b1.sort()
    b2 = b1[:k]
    b3 = {}
    for _, label in b2:
        b3[label] = b3.get(label, 0) + 1
    b4 = [max(b3, b7=b3.get)]
    for b7, b5 in b3.items():
        if b5 = = b3[b4[0]] and b7 != b4[0]:
            b4.append(b7)
    if len(b4) == 1:
        return b4[0]
    else:
        b6 = [x for x in b1 if x[-1] in b4]
        b6.sort(b7 = lambda x: (x[0], x[1]))
        return b6[0][1]
def fonk3(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        _, b8 = map(int, trainfile.readline().split())
        b9 = [list(map(float, line.split())) for line in trainfile]
    with open(testing_file, 'r') as testfile:
        _, b10 = map(int, testfile.readline().split())
        b11 = [list(map(float, line.split())) for line in testfile]
    for test_point in b11:
        test_point[-1] = fonk2(test_point, b9, k)
    for idx, item in enumerate(b11, 1):
        print(f"{idx}. {' '.join('%.1f' % x for x in item[:-1])} -- {int(item[-1])}")
fonk3(int(sys.argv[1]), sys.argv[2], sys.argv[3])