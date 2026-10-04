import sys
import math
def euclidean_distance(trained_point, test_point):
    sum = 0.0
    for i in range(len(trained_point)):
        sum += (trained_point[i] - test_point[i]) ** 2
    return math.sqrt(sum)
def knn(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        total_and_dimensions = trainfile.readline().split()
        train_total = int(total_and_dimensions[0])
        train_dimensions = int(total_and_dimensions[1])
        training_points = [line.split() for line in trainfile]
    with open(testing_file, 'r') as testfile:
        total_and_dimensions = testfile.readline().split()
        test_total = int(total_and_dimensions[0])
        test_dimensions = int(total_and_dimensions[1])
        testing_points = [line.split() for line in testfile]
    for point in training_points:
        for d in range(train_dimensions):
            point[d] = float(point[d])
        point[train_dimensions] = int(point[train_dimensions])
    for point in testing_points:
        for d in range(test_dimensions):
            point[d] = float(point[d])
    classes_count = {}
    for point_label in training_points:
        label = point_label[len(point_label) - 1]
        classes_count[label] = 0
    for test_point in testing_points:
        euclideans = []
        for train_point in training_points:
            label = train_point[-1]
            train_point = train_point[:-1]
            euclideans.append([euclidean_distance(train_point, test_point), label])
        euclideans = sorted(euclideans)
        k_nearest = euclideans[:k]
        most_popular_classes = []
        for neighbor in k_nearest:
            label = neighbor[-1]
            classes_count[label] = classes_count.get(label, 0) + 1
        most_popular_classes.append(max(classes_count, key=classes_count.get))
        for key, value in classes_count.items():
            if classes_count.get(key) == classes_count.get(most_popular_classes[0]) and key != most_popular_classes[0]:
                most_popular_classes.append(key)
        if len(most_popular_classes) == 1:
            test_point.append(most_popular_classes[0])
        else:
            euclideans = sorted([x for x in euclideans if x[-1] in most_popular_classes])
            if euclideans[0][0] == euclideans[1][0]:
                test_point.append(euclideans[0][1] if euclideans[0][1] < euclideans[1][1] else euclideans[1][1])
            else:
                test_point.append(euclideans[0][1])
        for key in classes_count.keys():
            classes_count[key] = 0
    count = 1
    for item in testing_points:
        print(str(count) + '. ' + (' ').join("%.1f" % x for x in item[:-1]) + ' -- ' + str(item[-1]))
        count += 1
