import csv
import math
n_itemlist = []
a = []
result = []
Mapper_list = []
Transaction_list = []
ReverseList = []
test_dict = {}
def readCSV(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            count = 0
            for row in reader:
                n_itemlist.append(row)
                count += 1
            print("CREATED LIST ITEMS WITH DUPLICATES: \n", count, len(n_itemlist), n_itemlist)
            return n_itemlist, count
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None, 0
def computeMinimumSupportCount(count):
    minsup = math.exp(-0.4 * count - 0.2) + 0.2
    supcount = minsup * count / 100
    return minsup, supcount
def manyToOne(n_itemlist):
    for sublist in n_itemlist:
        a.extend(sublist)
    print("ONLY ONE LIST with duplicates: \n", len(a), a)
    return a
def removeDuplicates(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        result.append(item)
    print("DUPLICATES REMOVED LIST :\n", len(result), result)
    return result
def createDictionary(result):
    test_dict = dict(zip(result, range(1, len(result) + 1)))
    print('DICTIONARY = ', test_dict)
    for key in sorted(test_dict.keys()):
        print("%s: %s" % (key, test_dict[key]))
    return test_dict
def mapper(n_itemlist, test_dict):
    for sublist in n_itemlist:
        temp_list = []
        for item in sublist:
            print(item)
            print(test_dict[item])
            temp_list.append(test_dict[item])
        Mapper_list.append(temp_list)
    print("MAPPER LIST:\n", Mapper_list)
    return Mapper_list
def binaryTransactionListBuilder(Mapper_list, result):
    for sublist in Mapper_list:
        t_list = [0] * len(result)
        for item_index in sublist:
            t_list[item_index - 1] = 1
        Transaction_list.append(t_list)
    print("Transaction_list:\n", Transaction_list)
    return Transaction_list
def reverseMapper(item, dict_list):
    mapper_key = 'Null'
    for itemset in dict_list:
        if item in itemset:
            mapper_key = itemset[0]
            break
    return mapper_key
if __name__ == "__main__":
    filename = "groceries_small.csv"
    n_itemlist, count = readCSV(filename)
    minsup, supcount = computeMinimumSupportCount(count)
    a = manyToOne(n_itemlist)
    result = removeDuplicates(a)
    test_dict = createDictionary(result)
    Mapper_list = mapper(n_itemlist, test_dict)
    Transaction_list = binaryTransactionListBuilder(Mapper_list, result)