import math
import sys
def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
def classify(test_point, training_points, k):
    distances = [(euclidean_distance(train_point[:-1], test_point), train_point[-1]) for train_point in training_points]
    distances.sort()
    k_nearest = distances[:k]
    classes_count = {}
    for _, label in k_nearest:
        classes_count[label] = classes_count.get(label, 0) + 1
    most_popular_classes = [max(classes_count, key=classes_count.get)]
    for key, value in classes_count.items():
        if value == classes_count[most_popular_classes[0]] and key != most_popular_classes[0]:
            most_popular_classes.append(key)
    if len(most_popular_classes) == 1:
        return most_popular_classes[0]
    else:
        filtered_distances = [x for x in distances if x[-1] in most_popular_classes]
        filtered_distances.sort(key=lambda x: (x[0], x[1]))
        return filtered_distances[0][1]
def knn(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        _, train_dimensions = map(int, trainfile.readline().split())
        training_points = [list(map(float, line.split())) for line in trainfile]
    with open(testing_file, 'r') as testfile:
        _, test_dimensions = map(int, testfile.readline().split())
        testing_points = [list(map(float, line.split())) for line in testfile]
    for test_point in testing_points:
        test_point[-1] = classify(test_point, training_points, k)
    for idx, item in enumerate(testing_points, 1):
        print(f"{idx}. {' '.join('%.1f' % x for x in item[:-1])} -- {int(item[-1])}")
knn(int(sys.argv[1]), sys.argv[2], sys.argv[3])