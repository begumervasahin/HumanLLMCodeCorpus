import csv
import time
import sys
import CSVtoLIST_def as cs
import am
import utils
def fonk1():
    '''
    Usage: $ python scriptname b12.csv b13 b14
    Ex: $ python testclass.py groceries_small.csv 3 0.5
    '''
    b1 = time.clock()
    b2 = []
    a1 = 0
    b3 = []
    b4 = []
    b5 = {}
    b6 = []
    b7 = []
    b8 = []
    b9 = {}
    b10 = []
    b11 = []
    b12 = sys.argv[1]
    b13 = int(sys.argv[2])
    b14 = float(sys.argv[3])
    print('Script b15 = ', sys.argv[0], '\n', 'Filename = ', sys.argv[1], '\n', 'Minsup = ', sys.argv[2], '\n', 'Min Confidence = ', sys.argv[3])
    b2, a1 = cs.readCSV(b12)
    print('Total b16 = ', a1)
    b3 = cs.manyToOne(b2)
    b4 = cs.removeDuplicates(b3)
    b5 = cs.createDictionary(b4)
    b6 = cs.mapper(b2,b5)
    b7 = cs.binaryTransactionListBuilder(b6, b4)
    b17 = []
    b18 = []
    b19 = []
    b20 = []
    b19 = am.countTransactions(b7)
    b20 = am.remDupSortReverseList(b19)
    b18 = am.addCountersTransactions(b20)
    not_to_be_pruned_items, to_be_pruned_items_list, list1, b17, b9 = am.antiMirroring(b18,b13)
    b21 = am.rules_generator(b17, b13, b14, b9)
    b22 = am.b22(b21)
    b4 = am.reversed(b22, b10, b5)
    b23 = am.formattedRules(b4)
    print(' ')
    print(' ')
    print('Association Rules \n')
    a2 = 1
    for items in b23:
        print(a2, '.',items)
        a2+=1
    print(' ')
    print(' ')
    print('---- PROGRAM OVER in %s seconds ----' % (time.clock() - b1))
if b24 = = '__main__':
    fonk1()