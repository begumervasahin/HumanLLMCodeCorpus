import sys
import math
def fonk1(point1, point2):
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))
def fonk2(file_name):
    with open(file_name, 'r') as file:
        total, b1 = map(int, file.readline().split())
        b2 = [[float(val) for val in line.split()] for line in file]
    return total, b1, b2
def fonk3(k, training_file, testing_file):
    train_total, train_dimensions, b3 = fonk2(training_file)
    test_total, test_dimensions, b4 = fonk2(testing_file)
    for test_point in b4:
        b5 = [(fonk1(train_point[:-1], test_point), train_point[-1]) for train_point in b3]
        b6 = sorted(b5)[:k]
        b7 = {}
        for distance, label in b6:
            b7[label] = b7.get(label, 0) + 1
        b8 = [label for label, count in b7.items() if count == max(b7.values())]
        if len(b8) == 1:
            test_point.append(b8[0])
        else:
            b9 = sorted([x for x in b6 if x[1] in b8])
            test_point.append(b9[0][1] if b9[0][1] < b9[1][1] else b9[1][1])
    for i, item in enumerate(b4, 1):
        print(f"{i}. {' '.join(f'{val:.1f}' for val in item[:-1])} -- {item[-1]}")
fonk3(int(sys.argv[1]), sys.argv[2], sys.argv[3])