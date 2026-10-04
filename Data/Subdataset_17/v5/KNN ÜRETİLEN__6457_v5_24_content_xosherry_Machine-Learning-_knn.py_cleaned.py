import sys
import math
def euclidean_distance(trained_point, test_point):
    return math.sqrt(sum((trained_point[i] - test_point[i]) ** 2 for i in range(len(trained_point))))
def load_data(file_path):
    with open(file_path, 'r') as file:
        total_points, dimensions = map(int, file.readline().split())
        points = [line.split() for line in file]
        for point in points:
            for d in range(dimensions):
                point[d] = float(point[d])
            if len(point) > dimensions:
                point[dimensions] = int(point[dimensions])
    return points, dimensions
def classify_points(k, training_points, testing_points, train_dimensions):
    classes_count = {point[-1]: 0 for point in training_points}
    for test_point in testing_points:
        distances = [
            [euclidean_distance(train_point[:-1], test_point), train_point[-1]]
            for train_point in training_points
        ]
        k_nearest = sorted(distances)[:k]
        for _, label in k_nearest:
            classes_count[label] += 1
        most_frequent_class = max(classes_count, key=classes_count.get)
        most_frequent_count = classes_count[most_frequent_class]
        tied_classes = [key for key, value in classes_count.items() if value == most_frequent_count]
        if len(tied_classes) == 1:
            test_point.append(most_frequent_class)
        else:
            tied_distances = [dist for dist in distances if dist[1] in tied_classes]
            test_point.append(min(tied_distances)[1])
        classes_count = {key: 0 for key in classes_count}
def print_results(testing_points):
    for idx, item in enumerate(testing_points, start=1):
        formatted_point = ' '.join(f"{x:.1f}" for x in item[:-1])
        print(f"{idx}. {formatted_point} -- {item[-1]}")
def knn(k, training_file, testing_file):
    training_points, train_dimensions = load_data(training_file)
    testing_points, _ = load_data(testing_file)
    classify_points(k, training_points, testing_points, train_dimensions)
    print_results(testing_points)
if __name__ == "__main__":
    knn(int(sys.argv[1]), sys.argv[2], sys.argv[3])