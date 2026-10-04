import sys
import csv
from collections import defaultdict
import ID3
import Node
import Accuracy
def parse_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        attribute_names = next(csvreader)[:-1]
        for row in csvreader:
            data.append([int(i) for i in row])
    attributes = list(range(len(attribute_names)))
    class_labels = [row[-1] for row in data]
    return attribute_names, data, attributes, class_labels
def main():
    L = int(sys.argv[1])
    K = int(sys.argv[2])
    directory = "data_sets1/"
    train_file = directory + sys.argv[3]
    validation_file = directory + sys.argv[4]
    test_file = directory + sys.argv[5]
    display_tree = sys.argv[6].lower() == 'yes'
    decision_tree = ID3.DTree(train_file)
    if display_tree:
        print("Decision Tree before Pruning:")
        print(decision_tree)
    test_accuracy = Accuracy.Accuracy(test_file)
    test_accuracy.calculateAccuracy(decision_tree.root)
    print("Accuracy before Pruning:")
    test_accuracy.displayAccuracy()
    decision_tree.pruneTree(L, K, validation_file)
    if display_tree:
        print("Decision Tree after Pruning:")
        print(decision_tree)
    test_accuracy.calculateAccuracy(decision_tree.root)
    print("Accuracy after Pruning:")
    test_accuracy.displayAccuracy()
if __name__ == '__main__':
    main()