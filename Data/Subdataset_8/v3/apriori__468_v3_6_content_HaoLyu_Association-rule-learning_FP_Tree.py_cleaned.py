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
        if not self.children:
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
    d = {}
    rt = {}
    for key in condition_pattern_base:
        count = condition_pattern_base[key]
        for item in key:
            d[item] = d.get(item, 0) + count
    d = {key: value for key, value in d.items() if value >= sigma}
    for key in condition_pattern_base:
        count = condition_pattern_base[key]
        item_set = [x for x in key if x in d]
        if len(item_set) < 2:
            continue
        item_set = sorted(item_set)
        for k in range(2, len(item_set) + 1):
            for sub_set in combinations(item_set, k):
                rt[sub_set] = rt.get(sub_set, 0) + count
    return rt
def read_data(data_file, row_size=0):
    matrix = []
    with open(data_file) as file:
        for idx, row in enumerate(file):
            if row_size and idx == row_size:
                break
            items = [int(item) for item in row.strip().split() if item]
            if len(items) >= 3:
                matrix.append(items)
    return matrix
def write_results(result_file, fieldnames, frequent_pattern):
    with open(result_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for key in frequent_pattern:
            if frequent_pattern[key] >= sigma:
                writer.writerow({
                    'set_size': len(key) + 1,
                    'frequency': frequent_pattern[key],
                    'items': f"{str(suffix)} {' '.join([str(item) for item in key])}"
                })
def mine_patterns(root, header_table, sorted_items, sigma, result_file, fieldnames):
    fp_length = len(sorted_items)
    count = 0.1
    for idx in range(fp_length - 1, -1, -1):
        percent = (1 - float(idx) / fp_length)
        if percent > count:
            print(f"%%%{int(percent * 100)} on progress")
            count += 0.1
        suffix = sorted_items[idx]
        head = header_table[suffix][0]
        condition_pattern_base = {}
        while head and head.val:
            temp_fp_tree = head.val
            basic_freq_count = temp_fp_tree.data[suffix]
            tree_pattern = []
            temp_fp_tree = temp_fp_tree.parent
            while temp_fp_tree.data:
                higher_pattern = list(temp_fp_tree.data.keys())[0]
                tree_pattern.append(higher_pattern)
                temp_fp_tree = temp_fp_tree.parent
            if len(tree_pattern) > 1:
                condition_pattern_base[tuple(tree_pattern)] = basic_freq_count
            head = head.next
        frequent_pattern = generate_freq_pattern(condition_pattern_base, sigma)
        if frequent_pattern:
            write_results(result_file, fieldnames, frequent_pattern)
def create_header_table(sorted_items):
    return {item: [None, None] for item in sorted_items}
def build_fp_tree(matrix, sorted_items):
    root = Node(None)
    header_table = create_header_table(sorted_items)
    for transaction in matrix:
        tree = root
        sorted_transaction = {key: idx for idx, key in enumerate(transaction) if key in sorted_items}
        sorted_transaction = [item for item, _ in sorted(sorted_transaction.items(), key=operator.itemgetter(1))]
        for item in sorted_transaction:
            if item not in tree.children_value:
                sub_tree = Node({item: 1})
                tree.add_child(sub_tree, item)
            else:
                sub_tree_idx = tree.children_value[item]
                sub_tree = tree.children[sub_tree_idx]
                sub_tree.data[item] += 1
            tree = sub_tree
    return root, header_table
def main():
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
    matrix = read_data(data_file, row_size)
    fieldnames = ['set_size', 'frequency', 'items']
    root, header_table = build_fp_tree(matrix, sorted_items)
    mine_patterns(root, header_table, sorted_items, sigma, result_file, fieldnames)
if __name__ == '__main__':
    main()