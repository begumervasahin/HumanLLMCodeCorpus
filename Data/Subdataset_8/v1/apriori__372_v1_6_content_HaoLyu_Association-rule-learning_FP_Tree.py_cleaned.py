import sys
import time
import csv
from itertools import combinations
import operator
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        self.children_value = {}
    def add_child(self, obj, val):
        if len(self.children) < 1:
            self.children.append(obj)
            obj.parent = self
            self.children_value[val] = 0
        else:
            self.children_value[val] = len(self.children)
            self.children.append(obj)
            obj.parent = self
class NodeLink:
    def __init__(self, data):
        self.val = data
        self.next = None
def process(child, header_table):
    child_data = child.data
    key = list(child_data.keys())[0]
    head = header_table[key][0]
    if head is None:
        new_node_link = NodeLink(child)
        header_table[key][0] = new_node_link
        header_table[key][1] = new_node_link
    else:
        new_node_link = NodeLink(child)
        header_table[key][1].next = new_node_link
        header_table[key][1] = new_node_link
def generate_freq_pattern(condition_pattern_base, sigma):
    d, rt = {}, {}
    for key in condition_pattern_base:
        count = condition_pattern_base[key]
        for item in key:
            if item not in d:
                d[item] = count
            else:
                d[item] += count
    d_keys = list(d.keys())
    for key in d_keys:
        if d[key] < sigma:
            d.pop(key)
    for key in condition_pattern_base:
        count = condition_pattern_base[key]
        item_set = list(key)
        prune_item_set = [x for x in item_set if x in d]
        if len(prune_item_set) < 2:
            continue
        prune_item_set = sorted(prune_item_set)
        for k in range(2, len(prune_item_set) + 1):
            for sub_set in combinations(prune_item_set, k):
                if sub_set not in rt:
                    rt[sub_set] = count
                else:
                    rt[sub_set] += count
    return rt
def solution(data_file, result_file, sigma, row_size=0):
    matrix = []
    if row_size != 0:
        stop = 0
        for row in open(data_file):
            if stop == row_size:
                break
            item = row.strip().split(' ')
            if len(item) >= 3:
                item = [int(one_item) for one_item in item]
                matrix.append(item)
            stop += 1
    else:
        for row in open(data_file):
            item = row.strip().split(' ')
            if len(item) >= 3:
                item = [int(one_item) for one_item in item]
                matrix.append(item)
    with open(result_file, 'w') as csvfile:
        fieldnames = ['set_size', 'frequency', 'items']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    L1, C1 = {}, {}
    start_time = time.time()
    for transaction in matrix:
        for item in transaction:
            item_key = (item,)
            if item_key not in C1:
                C1[item_key] = 1
            else:
                C1[item_key] += 1
    for item in C1:
        if C1[item] >= sigma:
            L1[item] = C1[item]
    sorted_x = [i[0] for i in sorted(L1.items(), key=operator.itemgetter(1), reverse=True)]
    sort_dict = {key: value for key, value in zip(sorted_x, range(len(sorted_x)))}
    root = Node(None)
    for transaction in matrix:
        tree = root
        L_transaction = {key: sort_dict[key] for key in transaction if key in sort_dict}
        L_transaction = [item_tuple[0] for item_tuple in sorted(L_transaction.items(), key=operator.itemgetter(1))]
        for item in L_transaction:
            if item not in tree.children_value:
                sub_tree = Node({item: 1})
                tree.add_child(sub_tree, item)
            else:
                sub_tree_idx = tree.children_value[item]
                sub_tree = tree.children[sub_tree_idx]
                sub_tree.data[item] += 1
            tree = sub_tree
    header_table = {item: [None, None] for item in sorted_x}
    bft = root.children
    while True:
        temp_bft = []
        for child in bft:
            temp_bft += child.children
            process(child, header_table)
        bft = temp_bft
        if len(bft) < 1:
            break
    fp_length = len(sorted_x)
    count = 0.1
    for idx in range(fp_length - 1, -1, -1):
        percent = (1 - float(idx) / fp_length)
        if percent > count:
            print('%%%d on progress' % (int(percent * 100)))
            count += 0.1
        suffix = sorted_x[idx]
        head = header_table[suffix][0]
        condition_pattern_base = {}
        while head is not None and head.val is not None:
            temp_fp_tree = head.val
            basic_freq_count = temp_fp_tree.data[suffix]
            tree_pattern = []
            temp_fp_tree = temp_fp_tree.parent
            while temp_fp_tree.data is not None:
                higher_pattern = list(temp_fp_tree.data.keys())[0]
                tree_pattern.append(higher_pattern)
                temp_fp_tree = temp_fp_tree.parent
            if len(tree_pattern) > 1:
                condition_pattern_base[tuple(tree_pattern)] = basic_freq_count
            head = head.next
        frequent_pattern = generate_freq_pattern(condition_pattern_base, sigma)
        if len(frequent_pattern.keys()) < 1:
            continue
        with open(result_file, 'a') as csvfile:
            fieldnames = ['set_size', 'frequency', 'items']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for key in frequent_pattern:
                if frequent_pattern[key] < sigma:
                    continue
                writer.writerow({'set_size': len(key) + 1,
                                 'frequency': frequent_pattern[key],
                                 'items': str(suffix) + ' ' + ' '.join([str(item) for item in key])
                                 })
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    result_file = 'result.csv'
    sigma = 4
    row_size = 0
    data_file = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            data_file = sys.argv[1]
            result_file = sys.argv[2]
            sigma = int(sys.argv[3])
            row_size = int(sys.argv[4])
        except IndexError:
            pass
    solution(data_file, result_file, sigma, row_size)