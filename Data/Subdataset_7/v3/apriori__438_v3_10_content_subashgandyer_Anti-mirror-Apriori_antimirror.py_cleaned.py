import csv
import time
import sys
import CSVtoLIST_def as cs
import am
import utils
def fonk1():
    fonk2()
    b1 = time.clock()
    b2 = []
    a1 = 0
    b3 = []
    b4 = []
    b5 = {}
    b6 = []
    b7 = []
    b8 = {}
    b9 = []
    b10 = sys.argv[1]
    b11 = int(sys.argv[2])
    b12 = float(sys.argv[3])
    fonk3(b10, b11, b12)
    b2, a1 = cs.readCSV(b10)
    print('Total Transactions:', a1)
    b3 = cs.manyToOne(b2)
    b4 = cs.removeDuplicates(b3)
    b5 = cs.createDictionary(b4)
    b6 = cs.mapper(b2, b5)
    b7 = cs.binaryTransactionListBuilder(b6, b4)
    b13 = am.countTransactions(b7)
    b14 = am.remDupSortReverseList(b13)
    b15 = am.addCountersTransactions(b14)
    not_to_be_pruned_items, to_be_pruned_items_list, list1, list2, b8 = am.antiMirroring(b15, b11)
    b16 = am.rules_generator(list2, b11, b12, b8)
    b17 = am.b17(b16)
    b4 = am.reversed(b17, b9, b5)
    b18 = am.formattedRules(b4)
    fonk4(b18)
    fonk5(b1)
def fonk2():
    print("Usage: $ python scriptname b10.csv b11 b12")
    print("Ex: $ python testclass.py groceries_small.csv 3 0.5")
def fonk3(b10, b11, b12):
    print('Script Name:', sys.argv[0])
    print('Filename:', b10)
    print('Minsup:', b11)
    print('Min Confidence:', b12)
def fonk4(b18):
    print(' ')
    print(' ')
    print('Association Rules:')
    for idx, items in enumerate(b18, b19 = 1):
        print(f'{idx}. {items}')
    print(' ')
    print(' ')
def fonk5(b1):
    print(f'---- PROGRAM OVER in {time.clock() - b1} seconds ----')
if b20 = = '__main__':
    fonk1()