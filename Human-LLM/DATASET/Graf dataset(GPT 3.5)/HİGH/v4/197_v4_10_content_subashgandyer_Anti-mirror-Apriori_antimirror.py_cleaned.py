import CSVtoLIST_def as cs
import csv
import am
import utils
import sys
import time
@profile
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
    b8 = []
    b9 = {}
    b10 = []
    b11 = []
    b12 = sys.argv[1]
    b13 = int(sys.argv[2])
    b14 = float(sys.argv[3])
    fonk3(b12, b13, b14)
    b2, a1 = cs.readCSV(b12)
    print('Total Transactions:', a1)
    b3 = cs.manyToOne(b2)
    b4 = cs.removeDuplicates(b3)
    b5 = cs.createDictionary(b4)
    b6 = cs.mapper(b2, b5)
    b7 = cs.binaryTransactionListBuilder(b6, b4)
    fonk4(b7, b13)
    b15 = am.rules_generator(b18, b13, b14, b9)
    b16 = am.b16(b15)
    b4 = am.reversed(b16, b10, b5)
    b17 = am.formattedRules(b4)
    fonk5(b17)
    fonk6(b1)
def fonk2():
    print("Usage: $ python scriptname b12.csv b13 b14")
    print("Ex: $ python testclass.py groceries_small.csv 3 0.5")
def fonk3(b12, b13, b14):
    print('Script Name:', sys.argv[0])
    print('Filename:', b12)
    print('Minsup:', b13)
    print('Min Confidence:', b14)
def fonk4(b7, b13):
    b18 = []
    b19 = []
    b20 = []
    b21 = []
    b20 = am.countTransactions(b7)
    b21 = am.remDupSortReverseList(b20)
    b19 = am.addCountersTransactions(b21)
    not_to_be_pruned_items, to_be_pruned_items_list, list1, b18, b9 = am.antiMirroring(b19, b13)
def fonk5(b17):
    print(' ')
    print(' ')
    print('Association Rules:')
    for idx, items in enumerate(b17, b22 = 1):
        print(f'{idx}. {items}')
    print(' ')
    print(' ')
def fonk6(b1):
    print(f'---- PROGRAM OVER in {time.clock() - b1} seconds ----')
if b23 = = '__main__':
    fonk1()