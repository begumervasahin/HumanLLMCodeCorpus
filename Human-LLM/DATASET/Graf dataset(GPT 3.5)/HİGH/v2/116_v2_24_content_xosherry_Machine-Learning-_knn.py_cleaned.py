import math
import sys
def fonk1(point1, point2):
    a1 = 0.0
    for i in range(len(point1)):
        a1 += (point1[i] - point2[i]) ** 2
    return math.sqrt(a1)
def fonk2(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        train_total, b1 = map(int, trainfile.readline().split())
        b2 = [list(map(float, line.split())) for line in trainfile]
    with open(testing_file, 'r') as testfile:
        test_total, b3 = map(int, testfile.readline().split())
        b4 = [list(map(float, line.split())) for line in testfile]
    for test_point in b4:
        b5 = []
        for b7 in b2:
            b6 = b7[-1]
            b7 = b7[:-1]
            b5.append([fonk1(b7, test_point), b6])
        b5.sort()
        b8 = b5[:k]
        b9 = {}
        for neighbor in b8:
            b9[neighbor[-1]] = b9.get(neighbor[-1], 0) + 1
        b10 = [max(b9, b13=b9.get)]
        for b13, b11 in b9.items():
            if b11 = = b9[b10[0]] and b13 != b10[0]:
                b10.append(b13)
        if len(b10) == 1:
            test_point.append(b10[0])
        else:
            b12 = [x for x in b5 if x[-1] in b10]
            b12.sort(b13 = lambda x: (x[0], x[1]))
            test_point.append(b12[0][1])
    a2 = 1
    for item in b4:
        print(f"{a2}. {' '.join('%.1f' % x for x in item[:-1])} -- {int(item[-1])}")
        a2 += 1
fonk2(int(sys.argv[1]), sys.argv[2], sys.argv[3])