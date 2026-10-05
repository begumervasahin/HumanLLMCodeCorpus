import csv
import time
import sys
import CSVtoLIST_def as cs
import am
import utils
def main():
    '''
    Usage: $ python scriptname filename.csv minsup min_confidence
    Ex: $ python testclass.py groceries_small.csv 3 0.5
    '''
    start_time = time.clock()
    n_itemlist = []
    count = 0
    a = []
    result = []
    test_dict = {}
    Mapper_list =[]
    Transaction_list = []
    ReverseList = []
    support_data = {}
    final = []
    dict_list = []
    filename = sys.argv[1]
    minsup = int(sys.argv[2])
    min_confidence = float(sys.argv[3])
    print('Script Name = ', sys.argv[0], '\n', 'Filename = ', sys.argv[1], '\n', 'Minsup = ', sys.argv[2], '\n', 'Min Confidence = ', sys.argv[3])
    n_itemlist, count = cs.readCSV(filename)
    print('Total Transactions = ', count)
    a = cs.manyToOne(n_itemlist)
    result = cs.removeDuplicates(a)
    test_dict = cs.createDictionary(result)
    Mapper_list = cs.mapper(n_itemlist,test_dict)
    Transaction_list = cs.binaryTransactionListBuilder(Mapper_list, result)
    list2 = []
    temp_list1 = []
    Transaction_list2 = []
    b = []
    Transaction_list2 = am.countTransactions(Transaction_list)
    b = am.remDupSortReverseList(Transaction_list2)
    temp_list1 = am.addCountersTransactions(b)
    not_to_be_pruned_items, to_be_pruned_items_list, list1, list2, support_data = am.antiMirroring(temp_list1,minsup)
    rules = am.rules_generator(list2, minsup, min_confidence, support_data)
    cleanRules = am.cleanRules(rules)
    result = am.reversed(cleanRules, final, test_dict)
    answer = am.formattedRules(result)
    print(' ')
    print(' ')
    print('Association Rules \n')
    i = 1
    for items in answer:
        print(i, '.',items)
        i+=1
    print(' ')
    print(' ')
    print('---- PROGRAM OVER in %s seconds ----' % (time.clock() - start_time))
if __name__ == '__main__':
    main()