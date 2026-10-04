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
products_set = set([item for sublist in transaction_list for item in sublist])
def last_maxsupport_check():
    max_value = 0
    for key, value in dict_for_result.items():
        if len(key) == combinations_counter - 1:
            if value > max_value:
                max_value = value
    if np.logical_and(max_value < min_supp, combinations_counter > 1):
        return False
    else:
        return True
def make_combination():
    global combinations_counter
    if last_maxsupport_check():
        combinations = list(it.combinations(products_set, combinations_counter))
        count_appearances(combinations)
    else:
        print_results()
def count_appearances(comb):
    global combinations_counter
    comb_set = set(comb)
    for element in comb:
        for row in transaction_list:
            check_for_appearances(element, row)
    combinations_counter += 1
    make_combination()
def check_for_appearances(el, ro):
    element = ''.join(sorted(el))
    row = ''.join(sorted(ro))
    row = throw_useless(element, row)
    if element in row:
        if element in dict_for_result:
            dict_for_result[element] += 1
        else:
            dict_for_result[element] = 1
def throw_useless(el, ro):
    row = ro[:]
    for row_char in ro:
        if row_char not in el:
            row = row.replace(row_char, '')
    return row
def print_results():
    print(dict_for_result)
    for key, value in dict_for_result.items():
        if value >= min_supp:
            print(f'Elements: {key} support {value}')
if __name__ == "__main__":
    make_combination()