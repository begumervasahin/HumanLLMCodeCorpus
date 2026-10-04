import sys
import math
import itertools
def fonk1(trained_point, test_point):
    b1 = sum((trained_point[i] - test_point[i]) ** 2 for i in range(len(trained_point)))
    return math.sqrt(b1)
def fonk2(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        train_total, b2 = map(int, trainfile.readline().split())
        b3 = [line.split() for line in trainfile]
    with open(testing_file, 'r') as testfile:
        test_total, b4 = map(int, testfile.readline().split())
        b5 = [line.split() for line in testfile]
    for point in b3:
        for d in range(b2):
            point[d] = float(point[d])
        point[b2] = int(point[b2])
    for point in b5:
        for d in range(b4):
            point[d] = float(point[d])
    b6 = {point[-1]: 0 for point in b3}
    for test_point in b5:
        b7 = [
            [fonk1(train_point[:-1], test_point), train_point[-1]]
            for train_point in b3
        ]
        b7.sort()
        b8 = b7[:k]
        for neighbor in b8:
            b9 = neighbor[-1]
            b6[b9] += 1
        b10 = max(b6, key=b6.get)
        b11 = b6[b10]
        b12 = [
            key for key, b13 in b6.items() if b13 = = b11
        ]
        if len(b12) == 1:
            test_point.append(b10)
        else:
            b14 = [
                dist for dist in b7 if dist[-1] in b12
            ]
            b14.sort()
            test_point.append(b14[0][1])
        b6 = {key: 0 for key in b6}
    for idx, item in enumerate(b5, b15 = 1):
        b16 = ' '.join(f"{x:.1f}" for x in item[:-1])
        print(f"{idx}. {b16} -- {item[-1]}")
if b17 = = "__main__":
    fonk2(int(sys.argv[1]), sys.argv[2], sys.argv[3])