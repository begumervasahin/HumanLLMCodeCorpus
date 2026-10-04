import sys
import math
def fonk1(trained_point, test_point):
    return math.sqrt(sum((trained_point[i] - test_point[i]) ** 2 for i in range(len(trained_point))))
def fonk2(file_path):
    with open(file_path, 'r') as file:
        total_points, b1 = map(int, file.readline().split())
        b2 = [line.split() for line in file]
        for point in b2:
            for d in range(b1):
                point[d] = float(point[d])
            if len(point) > b1:
                point[b1] = int(point[b1])
    return b2, b1
def fonk3(k, training_points, testing_points, b12):
    b3 = {point[-1]: 0 for point in training_points}
    for test_point in testing_points:
        b4 = [
            [fonk1(train_point[:-1], test_point), train_point[-1]]
            for train_point in training_points
        ]
        b5 = sorted(b4)[:k]
        for b13, label in b5:
            b3[label] += 1
        b6 = max(b3, key=b3.get)
        b7 = b3[b6]
        b8 = [key for key, value in b3.items() if value == b7]
        if len(b8) == 1:
            test_point.append(b6)
        else:
            b9 = [dist for dist in b4 if dist[1] in b8]
            test_point.append(min(b9)[1])
        b3 = {key: 0 for key in b3}
def fonk4(testing_points):
    for idx, item in enumerate(testing_points, b10 = 1):
        b11 = ' '.join(f"{x:.1f}" for x in item[:-1])
        print(f"{idx}. {b11} -- {item[-1]}")
def fonk5(k, training_file, testing_file):
    training_points, b12 = fonk2(training_file)
    testing_points, b13 = fonk2(testing_file)
    fonk3(k, training_points, testing_points, b12)
    fonk4(testing_points)
if b14 = = "__main__":
    fonk5(int(sys.argv[1]), sys.argv[2], sys.argv[3])