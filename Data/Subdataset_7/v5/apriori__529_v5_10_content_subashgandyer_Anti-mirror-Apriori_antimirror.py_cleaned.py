import CSVtoLIST_def as cs
import am
import sys
import time
def fonk1():
    fonk2()
    b1 = time.clock()
    b7, b8, b2 = fonk3()
    fonk4(b7, b8, b2)
    n_itemlist, b3 = cs.readCSV(b7)
    print('Total Transactions:', b3)
    b10, b11, b12, b4 = fonk5(n_itemlist)
    list2, b5 = fonk6(b4, b8)
    b6 = fonk7(list2, b8, b2, b5, b10, b11)
    fonk8(b6)
    fonk9(b1)
def fonk2():
    print("Usage: $ python scriptname b7.csv b8 b2")
    print("Ex: $ python testclass.py groceries_small.csv 3 0.5")
def fonk3():
    try:
        b7 = sys.argv[1]
        b8 = int(sys.argv[2])
        b2 = float(sys.argv[3])
        return b7, b8, b2
    except IndexError:
        print("Please provide the required command line arguments.")
        sys.exit(1)
def fonk4(b7, b8, b2):
    print('Script Name:', sys.argv[0])
    print('Filename:', b7)
    print('Minsup:', b8)
    print('Min Confidence:', b2)
def fonk5(n_itemlist):
    b9 = cs.manyToOne(n_itemlist)
    b10 = cs.removeDuplicates(b9)
    b11 = cs.createDictionary(b10)
    b12 = cs.mapper(n_itemlist, b11)
    b4 = cs.binaryTransactionListBuilder(b12, b10)
    return b10, b11, b12, b4
def fonk6(b4, b8):
    b13 = am.countTransactions(b4)
    b14 = am.remDupSortReverseList(b13)
    b15 = am.addCountersTransactions(b14)
    not_to_be_pruned_items, to_be_pruned_items_list, list1, list2, b5 = am.antiMirroring(b15, b8)
    return list2, b5
def fonk7(list2, b8, b2, b5, b10, b11):
    b16 = am.rules_generator(list2, b8, b2, b5)
    b17 = am.b17(b16)
    b10 = am.reversed(b17, [], b11)
    b6 = am.formattedRules(b10)
    return b6
def fonk8(b6):
    print(' ')
    print(' ')
    print('Association Rules:')
    for idx, items in enumerate(b6, b18 = 1):
        print(f'{idx}. {items}')
    print(' ')
    print(' ')
def fonk9(b1):
    print(f'---- PROGRAM OVER in {time.clock() - b1} seconds ----')
if b19 = = '__main__':
    fonk1()