import csv
import time
import sys
import CSVtoLIST_def as cs
import am
import utils
def main():
    start_time = time.clock()
    n_itemlist = []
    count = 0
    a = []
    result = []
    test_dict = {}
    Mapper_list =[]
    Transaction_list = []
    support_data = {}
    final = []
    filename = sys.argv[1]
    minsup = int(sys.argv[2])
    min_confidence = float(sys.argv[3])
    print('Script Name:', sys.argv[0])
    print('Filename:', filename)
    print('Minsup:', minsup)
    print('Min Confidence:', min_confidence)
    n_itemlist, count = cs.readCSV(filename)
    print('Total Transactions:', count)
    a = cs.manyToOne(n_itemlist)
    result = cs.removeDuplicates(a)
    test_dict = cs.createDictionary(result)
    Mapper_list = cs.mapper(n_itemlist, test_dict)
    Transaction_list = cs.binaryTransactionListBuilder(Mapper_list, result)
    Transaction_list2 = am.countTransactions(Transaction_list)
    b = am.remDupSortReverseList(Transaction_list2)
    temp_list1 = am.addCountersTransactions(b)
    not_to_be_pruned_items, to_be_pruned_items_list, list1, list2, support_data = am.antiMirroring(temp_list1, minsup)
    rules = am.rules_generator(list2, minsup, min_confidence, support_data)
    cleanRules = am.cleanRules(rules)
    result = am.reversed(cleanRules, final, test_dict)
    answer = am.formattedRules(result)
    print(' ')
    print(' ')
    print('Association Rules:')
    for idx, items in enumerate(answer, start=1):
        print(f'{idx}. {items}')
    print(' ')
    print(' ')
    print(f'---- PROGRAM OVER in {time.clock() - start_time} seconds ----')
if __name__ == '__main__':
    main()