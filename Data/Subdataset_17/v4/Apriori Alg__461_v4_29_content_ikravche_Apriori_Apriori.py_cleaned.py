import numpy as np
import itertools as it
min_supp = 3
min_confidence = 0.7
combinations_counter = 1
frequent_itemsets = {}
candidates = {}
transaction_list = [
    ['a', 'b'],
    ['a', 'c', 'd', 'e'],
    ['a', 'b', 'c', 'e'],
    ['c', 'd'],
    ['b', 'c', 'd', 'e'],
    ['a', 'd', 'e'],
    ['c', 'd', 'e']
]
products_set = set(item for sublist in transaction_list for item in sublist)
def check_last_max_support():
    max_value = 0
    for key, value in frequent_itemsets.items():
        if len(key) == combinations_counter - 1:
            if value > max_value:
                max_value = value
    return max_value >= min_supp or combinations_counter == 1
def generate_combinations():
    if check_last_max_support():
        combinations = list(it.combinations(products_set, combinations_counter))
        count_appearances(combinations)
    else:
        print_results()
def count_appearances(combinations):
    global combinations_counter
    for combination in combinations:
        for transaction in transaction_list:
            update_frequent_itemsets(combination, transaction)
    combinations_counter += 1
    generate_combinations()
def update_frequent_itemsets(combination, transaction):
    element = ''.join(sorted(combination))
    row = ''.join(sorted(transaction))
    filtered_row = filter_relevant_items(element, row)
    if element in filtered_row:
        if element in frequent_itemsets:
            frequent_itemsets[element] += 1
        else:
            frequent_itemsets[element] = 1
def filter_relevant_items(element, row):
    return ''.join([char for char in row if char in element])
def print_results():
    for key, value in frequent_itemsets.items():
        if value >= min_supp:
            print(f'Elements: {key} support {value}')
if __name__ == "__main__":
    generate_combinations()