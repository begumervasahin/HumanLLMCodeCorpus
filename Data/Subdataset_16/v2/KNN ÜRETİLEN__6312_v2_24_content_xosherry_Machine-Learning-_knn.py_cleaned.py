import sys
import math
def fonk1(trained_point, test_point):
    a1 = 0.0
    for i in range(len(trained_point)):
        a1 += (trained_point[i] - test_point[i]) ** 2
    return math.sqrt(a1)
def fonk2(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        train_total, b1 = map(int, trainfile.readline().split())
        b2 = [line.split() for line in trainfile]
    with open(testing_file, 'r') as testfile:
        test_total, b3 = map(int, testfile.readline().split())
        b4 = [line.split() for line in testfile]
    for point in b2:
        for d in range(b1):
            point[d] = float(point[d])
        point[b1] = int(point[b1])
    for point in b4:
        for d in range(b3):
            point[d] = float(point[d])
    b5 = {point[-1]: 0 for point in b2}
    for test_point in b4:
        b6 = []
        for train_point in b2:
            b7 = train_point[-1]
            b8 = train_point[:-1]
            b9 = fonk1(b8, test_point)
            b6.append([b9, b7])
        b6.sort()
        b10 = b6[:k]
        for neighbor in b10:
            b7 = neighbor[1]
            b5[b7] += 1
        b11 = [max(b5, key=b5.get)]
        b12 = b5[b11[0]]
        for key, b13 in b5.items():
            if b13 = = b12 and key != b11[0]:
                b11.append(key)
        if len(b11) == 1:
            test_point.append(b11[0])
        else:
            b14 = [x for x in b10 if x[1] in b11]
            b14.sort()
            if b14[0][0] == b14[1][0]:
                test_point.append(min(b14[0][1], b14[1][1]))
            else:
                test_point.append(b14[0][1])
        for key in b5:
            b5[key] = 0
    for count, item in enumerate(b4, 1):
        b15 = ' '.join(f"{x:.1f}" for x in item[:-1])
        print(f"{count}. {b15} -- {item[-1]}")
