import sys
import csv
import math
class Node:
    def __init__(self, tag, left=None, right=None, feature=None):
        self.tag = tag
        self.left = left
        self.right = right
        self.feature = feature
    def is_leaf(self):
        return self.left is None and self.right is None
def import_data(file_path):
    features = {}
    labels = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        features_list = next(reader)[:-1]
        for row in reader:
            labels.append(row[-1])
            for index, value in enumerate(row[:-1]):
                features.setdefault(features_list[index], []).append(value)
    tags = list(set(labels))
    return labels, features, tags
def count_labels(labels, tags):
    label_0 = labels.count(tags[0])
    label_1 = len(labels) - label_0
    return label_0, label_1
def entropy(labels, tags):
    label_0, label_1 = count_labels(labels, tags)
    if label_0 == 0 or label_1 == 0:
        return 0
    prob_0 = label_0 / len(labels)
    prob_1 = label_1 / len(labels)
    return -prob_0 * math.log(prob_0, 2) - prob_1 * math.log(prob_1, 2)
def mutual_information(feature, labels):
    n_labels = [label for index, label in enumerate(labels) if feature[index] in ['n', 'notA', 'no']]
    y_labels = [label for index, label in enumerate(labels) if feature[index] not in ['n', 'notA', 'no']]
    prob_1 = len(n_labels) / len(labels)
    prob_2 = len(y_labels) / len(labels)
    return entropy(labels, set(labels)) - (prob_1 * entropy(n_labels, set(labels))) - (prob_2 * entropy(y_labels, set(labels))), n_labels, y_labels
def split_data(feature, features):
    n_features = {key: [] for key in features.keys() if key != feature}
    y_features = {key: [] for key in features.keys() if key != feature}
    for index, value in features.items():
        for j, item in enumerate(value):
            if features[feature][j] in ['n', 'notA', 'no']:
                n_features[index].append(item)
            else:
                y_features[index].append(item)
    return n_features, y_features
def train_decision_tree(labels, features, tags, cur_depth, max_depth):
    label_0_num, label_1_num = count_labels(labels, tags)
    if label_0_num >= label_1_num:
        predict = tags[0]
    else:
        predict = tags[1]
    if label_0_num == len(labels) or label_1_num == len(labels) or not features or cur_depth >= max_depth:
        return Node(predict)
    else:
        best_score = -1
        best_feature = None
        best_n_labels = []
        best_y_labels = []
        for feature, values in features.items():
            score, n_labels, y_labels = mutual_information(values, labels)
            if score >= best_score:
                best_score = score
                best_feature = feature
                best_n_labels = n_labels
                best_y_labels = y_labels
        cur_depth += 1
        n_features, y_features = split_data(best_feature, features)
        left = train_decision_tree(best_n_labels, n_features, tags, cur_depth, max_depth)
        right = train_decision_tree(best_y_labels, y_features, tags, cur_depth, max_depth)
        return Node(tags[0], left, right, best_feature)
def test_decision_tree(node, test_input, output):
    with open(test_input, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = [test(node, row) + '\n' for row in reader]
    with open(output, 'w') as file:
        file.writelines(data)
def test(node, row):
    if node.is_leaf():
        return node.tag
    else:
        if row[node.feature] in ['n', 'notA', 'no']:
            return test(node.left, row)
        else:
            return test(node.right, row)
def train_and_test(train_input, test_input, depth, train_out, test_out, metrics):
    train_labels, train_features, train_tags = import_data(train_input)
    decision_tree = train_decision_tree(train_labels, train_features, train_tags, 0, depth)
    test_decision_tree(decision_tree, train_input, train_out)
    test_decision_tree(decision_tree, test_input, test_out)
    train_error = "Implement calculation of training error"
    test_error = "Implement calculation of testing error"
    metrics_str = f'error(train): {train_error}\nerror(test): {test_error}'
    with open(metrics, 'w') as file:
        file.write(metrics_str)
if __name__ == '__main__':
    if len(sys.argv) != 7:
        print("Usage: python script.py train_input test_input depth train_out test_out metrics")
    else:
        train_input, test_input, depth, train_out, test_out, metrics = sys.argv[1:]
        train_and_test(train_input, test_input, int(depth), train_out, test_out, metrics)