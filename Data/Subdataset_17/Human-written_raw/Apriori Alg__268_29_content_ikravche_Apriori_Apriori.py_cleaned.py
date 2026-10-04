29. Repository: ikravche/Apriori
   File: Apriori.py
   URL: https:
   Code Content:
import numpy as np
import itertools as it
min_supp = 3
min_confidence = 0.7
combinations_counter = 1
dict_for_result = {}
dict_for_stop = {}
transaction_list = [['a', 'b'],
                    ['a', 'c', 'd', 'e'],
                    ['a', 'b', 'c', 'e'],
                    ['c', 'd'],
                    ['b', 'c', 'd', 'e'],
                    ['a', 'd', 'e'],
                    ['c', 'd', 'e']]
products_set = set([item for sublist in transaction_list for item in
                    sublist])
def last_maxsupport_ckeck():
    max_value = 0
    for key, value in dict_for_result.iteritems():
        if len(key) == combinations_counter - 1:
            if value > max_value:
                max_value = value
    if np.logical_and(max_value < min_supp, combinations_counter > 1):
        return False
    else:
        return True
def make_combitanion():
    if last_maxsupport_ckeck():
        combinations = list(it.combinations(products_set, combinations_counter))
        count_appearances(combinations)
    else:
        print(dict_for_result)
        for key, value in dict_for_result.iteritems():
            if value >= min_supp:
                print('Elements: ' + str(key) + ' support ' + str(value))
def count_appearances(comb):
    global combinations_counter
    comb_set = set(comb)
    print(comb_set)
    for element in comb:
        for row in transaction_list:
            check_for_appearances(element, row)
    combinations_counter += 1
    make_combitanion()
def check_for_appearances(el, ro):
    element = ''.join(sorted(el))
    row = ''.join(sorted(ro))
    row = throw_useless(element, row)
    if np.logical_and(element in row, element in dict_for_result):
        dict_for_result[element] += 1
    elif element in row:
        dict_for_result[element] = 1
def throw_useless(el, ro):
    row = ro[:]
    for row_char in ro:
        if row_char not in el:
            row = row.replace(row_char, '')
    return row
make_combitanion()
   README Content:
Implementation of Apriori Algorithm
Apriori is an algorithm for frequent item set mining and association rule learning over transactional databases.
It proceeds by identifying the frequent individual items in the database and extending them to larger and larger
item sets as long as those item sets appear sufficiently often in the database.
The frequent item sets determined by Apriori can be used to determine association rules
which highlight general trends in the database:
this has applications in domains such as market basket analysis.
