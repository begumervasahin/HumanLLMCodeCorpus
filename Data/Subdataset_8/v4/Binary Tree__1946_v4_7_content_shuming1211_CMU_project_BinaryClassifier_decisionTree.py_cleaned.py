import sys
import csv
import math
train_input = sys.argv[1]
test_input = sys.argv[2]
depth = int(sys.argv[3])
train_out = sys.argv[4]
test_out = sys.argv[5]
metrics = sys.argv[6]
def import_data(train_input):
    features = {}
    label_list = []
    feat = []
    with open(train_input, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not feat:
                feat = [row[index] for index in range(len(row) - 1)]
            else:
                for index in range(len(row) - 1):
                    feat[index].append(row[index])
                label_list.append(row[-1])
    for j, feature in enumerate(feat):
        temp = feature.pop(0)
        features[temp] = feature
    tags = list(set(label_list))
    return label_list, features, tags
def count_number(label_list, tags):
    label_0 = sum(1 for index in label_list if index == tags[0])
    label_1 = len(label_list) - label_0
    return label_0, label_1
def cal_entropy(label_list, tags):
    label_0, label_1 = count_number(label_list, tags)
    if label_0 == 0 or label_1 == 0:
        return 0
    prob_0 = label_0 / len(label_list)
    prob_1 = label_1 / len(label_list)
    return -prob_0 * math.log(prob_0, 2) - prob_1 * math.log(prob_1, 2)
def cal_mutual_information(feature, label_list):
    n_labels = []
    y_labels = []
    tags = list(set(label_list))
    for index, value in enumerate(feature):
        if value in ['n', 'notA', 'no']:
            n_labels.append(label_list[index])
        else:
            y_labels.append(label_list[index])
    prob_1 = len(n_labels) / len(label_list)
    prob_2 = len(y_labels) / len(label_list)
    return cal_entropy(label_list, tags) - (prob_1 * cal_entropy(n_labels, tags)) - (prob_2 * cal_entropy(y_labels, tags)), n_labels, y_labels
def split_features(feature, features):
    n_features = {}
    y_features = {}
    len_list = len(features[feature])
    for index, value in features.items():
        if index == feature:
            continue
        n_features[index] = []
        y_features[index] = []
        for j in range(len_list):
            if features[feature][j] in ['n', 'notA', 'no']:
                n_features[index].append(value[j])
            else:
                y_features[index].append(value[j])
    return n_features, y_features
class Node:
    def __init__(self, tag, left=None, right=None, feature=None):
        self.tag = tag
        self.left = left
        self.right = right
        self.feature = feature
    def is_leaf(self):
        return self.left is None and self.right is None
def train_decision_tree(label_list, features, tags, cur_depth, max_depth):
    label_0_num, label_1_num = count_number(label_list, tags)
    if label_0_num >= label_1_num:
        predict = tags[0]
    else:
        predict = tags[1]
    if label_0_num == len(label_list) or label_1_num == len(label_list) or not features or cur_depth >= max_depth:
        return Node(predict)
    else:
        n_labels = []
        y_labels = []
        score = -1
        best_feature = None
        for feature, values in features.items():
            current_score, current_n_labels, current_y_labels = cal_mutual_information(values, label_list)
            if current_score >= score:
                score = current_score
                n_labels = current_n_labels
                y_labels = current_y_labels
                best_feature = feature
        cur_depth += 1
        n_features, y_features = split_features(best_feature, features)
        left = train_decision_tree(n_labels, n_features, tags, cur_depth, max_depth)
        right = train_decision_tree(y_labels, y_features, tags, cur_depth, max_depth)
        return Node(tags[0], left, right, best_feature)
def test_decision_tree(node, test_input, output):
    with open(test_input, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = []
        for row in reader:
            label = test(node, row)
            data.append(label + '\n')
        str_data = ''.join(data)
    with open(output, 'w') as file:
        file.write(str_data)
def test(node, row):
    if node.is_leaf():
        return node.tag
    else:
        if row[node.feature] in ['n', 'notA', 'no']:
            return test(node.left, row)
        else:
            return test(node.right, row)
def train_and_test(train_input, test_input, depth, train_out, test_out, metrics):
    train_label_list, train_features, train_tags = import_data(train_input)
    decision_tree = train_decision_tree(train_label_list, train_features, train_tags, 0, depth)
    train_error = test_decision_tree(decision_tree, train_input, train_out)
    test_error = test_decision_tree(decision_tree, test_input, test_out)
    metrics_str = f'error(train): {train_error}\nerror(test): {test_error}'
    with open(metrics, 'w') as file:
        file.write(metrics_str)
if __name__ == '__main__':
    train_and_test(train_input, test_input, depth, train_out, test_out, metrics)