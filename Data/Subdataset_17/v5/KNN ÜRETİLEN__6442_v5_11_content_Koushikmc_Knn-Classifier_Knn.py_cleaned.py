import csv
import math
import operator
def load_train_data(file_name):
    training_data = []
    try:
        with open(file_name, mode='r') as train_file:
            data = csv.reader(train_file)
            for rec in data:
                temp_list = [float(cols) if i != len(rec) - 1 else cols for i, cols in enumerate(rec)]
                training_data.append(temp_list)
        print("Training data loaded")
    except IOError:
        print("File not available. Please check the filename")
        exit()
    return training_data
def calculate_distance(train, test):
    if any(len(rec) - 1 != len(test) for rec in train):
        print("Dimensions of test and train do not match")
        return []
    distance_set = []
    for idx, rec in enumerate(train):
        dist = sum((test[i] - rec[i]) ** 2 for i in range(len(test)))
        distance = round(math.sqrt(dist), 3)
        print(f"Distance between the test point and training data {idx + 1}: {distance}")
        distance_set.append(distance)
    return distance_set
def find_neighbours(training_data, distances, num_neighbors):
    sorted_indices = sorted(range(len(distances)), key=lambda x: distances[x])
    neighbours = sorted_indices[:num_neighbors]
    class_votes = {}
    for n in neighbours:
        label = training_data[n][-1]
        class_votes[label] = class_votes.get(label, 0) + 1
    predicted_class = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    print(f"Predicted class: {predicted_class}")
    return predicted_class
def main():
    print("Place the input dataset CSV file in the same directory as the Python module.")
    file_name = input("Enter the name of the training dataset CSV file: ")
    training_data = load_train_data(file_name)
    test = [float(x) for x in input("Enter the values separated by ',': ").split(",")]
    k = int(input("Enter the number of neighbors to consider: "))
    distances = calculate_distance(training_data, test)
    if distances:
        find_neighbours(training_data, distances, k)
if __name__ == "__main__":
    main()