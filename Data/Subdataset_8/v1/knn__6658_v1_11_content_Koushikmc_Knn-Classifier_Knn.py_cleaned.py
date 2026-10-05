import csv
import math
import operator
training_data = []
def load_train_data(file_name):
    try:
        with open(file_name, 'r') as train:
            data = csv.reader(train)
            for rec in data:
                temp_list = [float(cols) for cols in rec[:-1]]
                temp_list.append(rec[-1])
                training_data.append(temp_list)
        print("Training data loaded")
    except IOError:
        print("File not available. Please check the filename")
        exit()
def calcdist(train, test):
    distance_set = []
    for rec in train:
        if len(rec[:-1]) != len(test):
            print("Dimensions of test and train do not match")
            break
        else:
            dist = sum((x - y) ** 2 for x, y in zip(test, rec[:-1]))
            dist = round(math.sqrt(dist), 3)
            print("Distance between the test point and training data {}: {}".format(train.index(rec) + 1, dist))
            distance_set.append(dist)
    return distance_set
def find_neighbours(dist, num_of_neighbors):
    top_elements_list = sorted(range(len(dist)), key=lambda x: dist[x])
    neighbors = top_elements_list[:num_of_neighbors]
    class_dict = {}
    for n in neighbors:
        class_label = training_data[n][-1]
        class_dict[class_label] = class_dict.get(class_label, 0) + 1
    output_class = max(class_dict.items(), key=operator.itemgetter(1))[0]
    print("Predicted class:", output_class)
if __name__ == "__main__":
    print("Place the input dataset CSV file in the same directory as the Python module")
    file_name = input("Enter the name of the training dataset CSV file: ")
    load_train_data(file_name)
    test = [float(x) for x in input("Enter the values separated by ',': ").split(",")]
    k = int(input("Enter the number of neighbors to consider: "))
    distance = calcdist(training_data, test)
    find_neighbours(distance, k)