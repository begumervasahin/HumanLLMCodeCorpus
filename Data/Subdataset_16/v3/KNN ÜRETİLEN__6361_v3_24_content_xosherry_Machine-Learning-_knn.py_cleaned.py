import sys
import math
from collections import defaultdict
def fonk1(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
def fonk2(k, training_file, testing_file):
    def fonk3(file_path):
        with open(file_path, 'r') as file:
            total, b1 = map(int, file.readline().split())
            b2 = [line.split() for line in file]
            return total, b1, b2
    def fonk4(b2, b1):
        for point in b2:
            for d in range(b1):
                point[d] = float(point[d])
            point[b1] = int(point[b1]) if len(point) > b1 else None
        return b2
    train_total, train_dimensions, b3 = fonk3(training_file)
    test_total, test_dimensions, b4 = fonk3(testing_file)
    b3 = fonk4(b3, train_dimensions)
    b4 = fonk4(b4, test_dimensions)
    for test_point in b4:
        b5 = []
        for train_point in b3:
            b6 = train_point[-1]
            b7 = train_point[:-1]
            b8 = fonk1(b7, test_point)
            b5.append((b8, b6))
        b5.sort()
        b9 = b5[:k]
        b10 = defaultdict(int)
        for _, b6 in b9:
            b10[b6] += 1
        b11 = max(b10.values())
        b12 = [b6 for b6, votes in b10.items() if votes == b11]
        if len(b12) == 1:
            test_point.append(b12[0])
        else:
            b13 = [x for x in b9 if x[1] in b12]
            b13.sort()
            test_point.append(b13[0][1])
    for count, item in enumerate(b4, 1):
        b14 = ' '.join(f"{x:.1f}" for x in item[:-1])
        print(f"{count}. {b14} -- {item[-1]}")
