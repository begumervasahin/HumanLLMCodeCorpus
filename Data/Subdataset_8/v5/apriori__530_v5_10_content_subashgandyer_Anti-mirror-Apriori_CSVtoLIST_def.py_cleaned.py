import csv
import itertools
import math
n_itemlist = []
a = []
result = []
Mapper_list = []
Transaction_list = []
test_dict = {}
def read_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            n_itemlist.append(row)
            count += 1
    print("CREATED LIST ITEMS WITH DUPLICATES:\n", count, len(n_itemlist), n_itemlist)
    return n_itemlist, count
def compute_minimum_support_count(count):
    minsup = math.exp(-0.4 * count - 0.2) + 0.2
    supcount = minsup * count / 100
    return minsup, supcount
def many_to_one(n_itemlist):
    for sublist in n_itemlist:
        a.extend(sublist)
    print("ONLY ONE LIST with duplicates:\n", len(a), a)
    return a
def remove_duplicates(seq, idfun=None):
    if idfun is None:
       def idfun(x): return x
    seen = {}
    for item in seq:
       marker = idfun(item)
       if marker in seen:
           continue
       seen[marker] = 1
       result.append(item)
    print("DUPLICATES REMOVED LIST:\n", len(result), result)
    return result
def create_dictionary(result):
    test_dict = {item: index + 1 for index, item in enumerate(result)}
    print('DICTIONARY = ', test_dict)
    for key in sorted(test_dict.keys()):
        print("%s: %s" % (key, test_dict[key]))
    return test_dict
def mapper(n_itemlist, test_dict):
    for sublist in n_itemlist:
        temp_list = [test_dict[item] for item in sublist]
        Mapper_list.append(temp_list)
    print("MAPPER LIST:\n", Mapper_list)
    return Mapper_list
def binary_transaction_list_builder(Mapper_list, result):
    for sublist in Mapper_list:
        t_list = [0] * len(result)
        for item_index in sublist:
            t_list[item_index - 1] = 1
        Transaction_list.append(t_list)
    print("Transaction_list:\n", Transaction_list)
    return Transaction_list
