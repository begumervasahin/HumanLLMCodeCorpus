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
def import_data(train_input):
    features = {}
    label_list = []
    feat = []
    with open(train_input) as all_data:
        reader = csv.reader(all_data)
        for row in reader:
            if not feat:
                feat = [[row[index]] for index in range(len(row)-1)]
            else:
                for index in range(len(row)-1):
                    feat[index].append(row[index])
            label_list.append(row[-1])
        for j in range(len(row)-1):
            temp = feat[j].pop(0)
            features[temp] = feat[j]
    tags = list(set(label_list))
    return label_list, features, tags
def count_labels(label_list, tags):
    label0 = label_list.count(tags[0])
    label1 = len(label_list) - label0
    return label0, label1
def calculate_entropy(label_list, tags):
    label0, label1 = count_labels(label_list, tags)
    if label0 == 0 or label1 == 0:
        return 0
    prob0 = 1.0 * label0 / len(label_list)
    prob1 = 1.0 * label1 / len(label_list)
    return -prob0 * math.log(prob0, 2) - prob1 * math.log(prob1, 2)
def calculate_mutual_information(feature, label_list):
    n_labels = [label_list[i] for i in range(len(feature)) if feature[i] in ('n', 'notA', 'no')]
    y_labels = [label_list[i] for i in range(len(feature)) if feature[i] not in ('n', 'notA', 'no')]
    tags = list(set(label_list))
    prob1 = 1.0 * len(n_labels) / len(label_list)
    prob2 = 1.0 * len(y_labels) / len(label_list)
    return calculate_entropy(label_list, tags) - (prob1 * calculate_entropy(n_labels, tags)) - (prob2 * calculate_entropy(y_labels, tags)), n_labels, y_labels
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
def train_decision_tree(label_list, features, tags, cur_depth, max_depth):
    label0_num, label1_num = count_labels(label_list, tags)
    if label0_num > label1_num:
        predict = tags[0]
        predict_num = label0_num
    else:
        predict = tags[1]
        predict_num = label1_num
    if predict_num == len(label_list):
        return Node(predict)
    elif len(features) == 0:
        return Node(predict)
    elif cur_depth > max_depth:
        return Node(predict)
    else:
        n_labels = []
        y_labels = []
        score = -1
        feature = []
        for i in features:
            current_score, current_n_labels, current_y_labels = calculate_mutual_information(features[i], label_list)
            if current_score >= score:
                score = current_score
                n_labels = current_n_labels
                y_labels = current_y_labels
                feature = i
        cur_depth += 1
        n_features, y_features = split_features(feature, features)
        left = train_decision_tree(n_labels, n_features, tags, cur_depth, max_depth)
        right = train_decision_tree(y_labels, y_features, tags, cur_depth, max_depth)
        return Node(tags[0], left, right, feature)
def test_decision_tree(node, test_input, output):
    with open(test_input) as all_data:
        reader = csv.reader(all_data)
        data = []
        feat = next(reader)[:-1]
        for row in reader:
            dict_ = {feat[index]: row[index] for index in range(len(row)-1)}
            label = test_instance(node, dict_)
            data.append(label + '\n')
    with open(output, 'w') as f:
        f.writelines(data)
def test_instance(node, dict_):
    if node.is_leaf():
        return node.tag
    else:
        if dict_[node.feature] in ('n', 'notA', 'no'):
            return test_instance(node.left, dict_)
        else:
            return test_instance(node.right, dict_)
def train_and_test(train_input, test_input, depth, train_out, test_out, metrics):
    train_label_list, train_features, train_tags = import_data(train_input)
    node = train_decision_tree(train_label_list, train_features, train_tags, 0, depth)
    test_decision_tree(node, train_input, train_out)
    test_decision_tree(node, test_input, test_out)
    train_error = test_decision_tree(node, train_input, train_out)
    test_error = test_decision_tree(node, test_input, test_out)
    with open(metrics, 'w') as f:
        f.write(f'error(train): {train_error}\nerror(test): {test_error}')
if __name__ == '__main__':
    if len(sys.argv) != 7:
        print("Usage: python script.py train_input test_input depth train_out test_out metrics")
        sys.exit(1)
    train_input, test_input, depth, train_out, test_out, metrics = sys.argv[1:]
    depth = int(depth)
    train_and_test(train_input, test_input, depth, train_out, test_out, metrics)