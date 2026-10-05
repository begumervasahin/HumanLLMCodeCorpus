import math
import sys
def euclidean_distance(point1, point2):
    sum = 0.0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i]) ** 2
    return math.sqrt(sum)
def knn(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        train_total, train_dimensions = map(int, trainfile.readline().split())
        training_points = [list(map(float, line.split())) for line in trainfile]
    with open(testing_file, 'r') as testfile:
        test_total, test_dimensions = map(int, testfile.readline().split())
        testing_points = [list(map(float, line.split())) for line in testfile]
    for test_point in testing_points:
        distances = []
        for train_point in training_points:
            label = train_point[-1]
            train_point = train_point[:-1]
            distances.append([euclidean_distance(train_point, test_point), label])
        distances.sort()
        k_nearest = distances[:k]
        classes_count = {}
        for neighbor in k_nearest:
            classes_count[neighbor[-1]] = classes_count.get(neighbor[-1], 0) + 1
        most_popular_classes = [max(classes_count, key=classes_count.get)]
        for key, value in classes_count.items():
            if value == classes_count[most_popular_classes[0]] and key != most_popular_classes[0]:
                most_popular_classes.append(key)
        if len(most_popular_classes) == 1:
            test_point.append(most_popular_classes[0])
        else:
            filtered_distances = [x for x in distances if x[-1] in most_popular_classes]
            filtered_distances.sort(key=lambda x: (x[0], x[1]))
            test_point.append(filtered_distances[0][1])
    count = 1
    for item in testing_points:
        print(f"{count}. {' '.join('%.1f' % x for x in item[:-1])} -- {int(item[-1])}")
        count += 1
knn(int(sys.argv[1]), sys.argv[2], sys.argv[3])