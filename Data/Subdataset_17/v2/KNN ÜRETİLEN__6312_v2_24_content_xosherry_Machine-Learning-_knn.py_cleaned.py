import sys
import math
def euclidean_distance(trained_point, test_point):
    sum = 0.0
    for i in range(len(trained_point)):
        sum += (trained_point[i] - test_point[i]) ** 2
    return math.sqrt(sum)
def knn(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        train_total, train_dimensions = map(int, trainfile.readline().split())
        training_points = [line.split() for line in trainfile]
    with open(testing_file, 'r') as testfile:
        test_total, test_dimensions = map(int, testfile.readline().split())
        testing_points = [line.split() for line in testfile]
    for point in training_points:
        for d in range(train_dimensions):
            point[d] = float(point[d])
        point[train_dimensions] = int(point[train_dimensions])
    for point in testing_points:
        for d in range(test_dimensions):
            point[d] = float(point[d])
    classes_count = {point[-1]: 0 for point in training_points}
    for test_point in testing_points:
        euclideans = []
        for train_point in training_points:
            label = train_point[-1]
            train_coords = train_point[:-1]
            distance = euclidean_distance(train_coords, test_point)
            euclideans.append([distance, label])
        euclideans.sort()
        k_nearest = euclideans[:k]
        for neighbor in k_nearest:
            label = neighbor[1]
            classes_count[label] += 1
        most_popular_classes = [max(classes_count, key=classes_count.get)]
        max_count = classes_count[most_popular_classes[0]]
        for key, value in classes_count.items():
            if value == max_count and key != most_popular_classes[0]:
                most_popular_classes.append(key)
        if len(most_popular_classes) == 1:
            test_point.append(most_popular_classes[0])
        else:
            k_nearest_filtered = [x for x in k_nearest if x[1] in most_popular_classes]
            k_nearest_filtered.sort()
            if k_nearest_filtered[0][0] == k_nearest_filtered[1][0]:
                test_point.append(min(k_nearest_filtered[0][1], k_nearest_filtered[1][1]))
            else:
                test_point.append(k_nearest_filtered[0][1])
        for key in classes_count:
            classes_count[key] = 0
    for count, item in enumerate(testing_points, 1):
        formatted_coords = ' '.join(f"{x:.1f}" for x in item[:-1])
        print(f"{count}. {formatted_coords} -- {item[-1]}")
