import numpy as np
import itertools as it
min_supp = 3
min_confidence = 0.7
combinations_counter = 1
dict_for_result = {}
dict_for_stop = {}
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
def last_maxsupport_check():
    max_value = 0
    for key, value in dict_for_result.items():
        if len(key) == combinations_counter - 1 and value > max_value:
            max_value = value
    return max_value >= min_supp or combinations_counter == 1
def make_combination():
    global combinations_counter
    if last_maxsupport_check():
        combinations = list(it.combinations(products_set, combinations_counter))
        count_appearances(combinations)
    else:
        print_results()
def count_appearances(combinations):
    global combinations_counter
    for element in combinations:
        for row in transaction_list:
            check_for_appearances(element, row)
    combinations_counter += 1
    make_combination()
def check_for_appearances(element, row):
    element_str = ''.join(sorted(element))
    row_str = ''.join(sorted(row))
    row_filtered = throw_useless(element_str, row_str)
    if element_str in row_filtered:
        if element_str in dict_for_result:
            dict_for_result[element_str] += 1
        else:
            dict_for_result[element_str] = 1
def throw_useless(element, row):
    return ''.join([char for char in row if char in element])
def print_results():
    print("Frequent Itemsets:")
    for key, value in dict_for_result.items():
        if value >= min_supp:
            print(f'Elements: {key}, Support: {value}')
if __name__ == "__main__":
    make_combination()