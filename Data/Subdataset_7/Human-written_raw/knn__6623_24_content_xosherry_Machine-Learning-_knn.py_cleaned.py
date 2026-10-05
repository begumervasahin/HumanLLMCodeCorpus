import sys
import math
import itertools
def fonk1(trained_point, test_point):
    a1 = 0.0
    for i in range(len(trained_point)):
        a1 += (trained_point[i] - test_point[i]) ** 2
    return math.sqrt(a1)
def fonk2(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        b1 = trainfile.readline().split()
        b2 = int(b1[0])
        b3 = int(b1[1])
        b4 = [line.split() for line in trainfile]
    trainfile.close()
    with open(testing_file, 'r') as testfile:
        b1 = testfile.readline().split()
        b5 = int(b1[0])
        b6 = int(b1[1])
        b7 = [line.split() for line in testfile]
    testfile.close()
    for point in b4:
        for d in range(b3):
            point[d] = float(point[d])
        point[b3] = int(point[b3])
    for point in b7:
        for d in range(b6):
            point[d] = float(point[d])
    b8 = {}
    for point_label in b4:
        b9 = point_label[len(point_label) - 1]
        b8[b9] = 0
    for test_point in b7:
        b10 = []
        for b11 in b4:
            b9 = b11[-1]
            b11 = b11[:-1]
            b10.append([fonk1(b11, test_point), b9])
        b10 = sorted(b10)
        b12 = []
        b12 = b10[:k]
        b13 = []
        for neighbor in b12:
            b9 = neighbor[-1]
            b8[b9] = b8.get(b9, 0) + 1
        b13.append(max(b8, b14 = b8.get))
        for b14, value in b8.items():
            if b8.get(b14) == b8.get(b13[0]) and b14 is not b13[0]:
                b13.append(b14)
        if len(b13) == 1:
            test_point.append(b13[0])
        else:
            b10 = sorted([x for x in b10 if x[-1] in b13])
            if b10[0][0] == b10[1][0]:
                test_point.append(b10[0][1] if b10[0][1] < b10[1][1] else b10[1][1])
            else:
                test_point.append(b10[0][1])
        for b14,value in b8.items():
            b8[b14] = 0
    a2 = 1
    for item in b7:
        print str(a2) + '. ' + (' ').join("%.1f" % x for x in item[:-1]) + ' -- ' + str(item[-1])
        a2 += 1
fonk2(int(sys.argv[1]), sys.argv[2], sys.argv[3])