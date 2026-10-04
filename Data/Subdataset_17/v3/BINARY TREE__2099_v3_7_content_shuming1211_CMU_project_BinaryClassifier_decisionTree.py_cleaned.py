import sys
import csv
import math
train_input = sys.argv[1]
test_input = sys.argv[2]
depth = int(sys.argv[3])
train_out = sys.argv[4]
test_out = sys.argv[5]
metrics = sys.argv[6]
def import_data(file_path):
    features = {}
    label_list = []
    feat = []
    with open(file_path, 'r') as all_data:
        reader = csv.reader(all_data)
        for row in reader:
            if not feat:
                for index in range(len(row) - 1):
                    feat.append([row[index]])
            else:
                for index in range(len(row) - 1):
                    feat[index].append(row[index])
                label_list.append(row[-1])
    for j in range(len(row) - 1):
        feature_name = feat[j].pop(0)
        features[feature_name] = feat[j]
    tags = list(set(label_list))
    return label_list, features, tags
def count_labels(label_list, tags):
    label0_count = label_list.count(tags[0])
    label1_count = label_list.count(tags[1])
    return label0_count, label1_count
def calculate_entropy(label_list, tags):
    label0_count, label1_count = count_labels(label_list, tags)
    if label0_count == 0 or label1_count == 0:
        return 0
    prob0 = label0_count / len(label_list)
    prob1 = label1_count / len(label_list)
    return -prob0 * math.log(prob0, 2) - prob1 * math.log(prob1, 2)
def calculate_mutual_information(feature, label_list):
    n_labels = []
    y_labels = []
    tags = list(set(label_list))
    for index in range(len(feature)):
        if feature[index] in ('n', 'notA', 'no'):
            n_labels.append(label_list[index])
        else:
            y_labels.append(label_list[index])
    prob1 = len(n_labels) / len(label_list)
    prob2 = len(y_labels) / len(label_list)
    return (calculate_entropy(label_list, tags) -
            (prob1 * calculate_entropy(n_labels, tags)) -
            (prob2 * calculate_entropy(y_labels, tags)),
            n_labels, y_labels)
def split_features(feature, features):
    n_features = {}
    y_features = {}
    len_list = len(features[feature])
    for index in features:
        if index == feature:
            continue
        n_features[index] = []
        y_features[index] = []
        for j in range(len_list):
            if features[feature][j] in ('n', 'notA', 'no'):
                n_features[index].append(features[index][j])
            else:
                y_features[index].append(features[index][j])
    return n_features, y_features
class Node:
    def __init__(self, tag, left=None, right=None, feature=None):
        self.tag = tag
        self.left = left
        self.right = right
        self.feature = feature
    def is_leaf(self):
        return self.left is None and self.right is None
def dt_train(label_list, features, tags, cur_depth, max_depth):
    label0_count, label1_count = count_labels(label_list, tags)
    predict = tags[0] if label0_count > label1_count else tags[1]
    predict_count = max(label0_count, label1_count)
    if predict_count == len(label_list) or not features or cur_depth >= max_depth:
        return Node(predict)
    best_feature = None
    best_score = -1
    n_labels, y_labels = [], []
    for feature in features:
        current_score, current_n_labels, current_y_labels = calculate_mutual_information(features[feature], label_list)
        if current_score > best_score:
            best_score = current_score
            n_labels = current_n_labels
            y_labels = current_y_labels
            best_feature = feature
    cur_depth += 1
    n_features, y_features = split_features(best_feature, features)
    left_child = dt_train(n_labels, n_features, tags, cur_depth, max_depth)
    right_child = dt_train(y_labels, y_features, tags, cur_depth, max_depth)
    return Node(tags[0], left_child, right_child, best_feature)
def dt_test(node, file_path, output):
    data = []
    feat = []
    incorrect_predictions = 0
    total = 0
    with open(file_path, 'r') as all_data:
        reader = csv.reader(all_data)
        for row in reader:
            if total == 0:
                feat = row[:-1]
            else:
                row_dict = {feat[index]: row[index] for index in range(len(row) - 1)}
                predicted_label = test(node, row_dict)
                data.append(predicted_label + '\n')
                if predicted_label != row[-1]:
                    incorrect_predictions += 1
            total += 1
    with open(output, 'w') as f:
        f.writelines(data)
    return incorrect_predictions / (total - 1)
def test(node, row_dict):
    if node.is_leaf():
        return node.tag
    if row_dict[node.feature] in ('n', 'notA', 'no'):
        return test(node.left, row_dict)
    return test(node.right, row_dict)
def train_and_test(train_input, test_input, depth, train_out, test_out, metrics):
    train_label_list, train_features, train_tags = import_data(train_input)
    tree = dt_train(train_label_list, train_features, train_tags, 0, depth)
    train_error = dt_test(tree, train_input, train_out)
    test_error = dt_test(tree, test_input, test_out)
    with open(metrics, 'w') as f:
        f.write(f'error(train): {train_error}\n')
        f.write(f'error(test): {test_error}\n')
if __name__ == '__main__':
    train_and_test(train_input, test_input, depth, train_out, test_out, metrics)