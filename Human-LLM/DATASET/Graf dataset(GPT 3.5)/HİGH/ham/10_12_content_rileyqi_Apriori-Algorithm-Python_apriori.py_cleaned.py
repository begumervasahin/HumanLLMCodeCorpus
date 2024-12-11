12. Repository: rileyqi/Apriori-Algorithm-Python
   File: apriori.py
   URL: https:
   Code Content:
import sys
from collections import defaultdict
from optparse import OptionParser
import csv
def fonk1(b3, Lk_1):
    for item in b3:
        b1 = b3 - frozenset([item])
        if((b1 in Lk_1)==False):
            return True
    return False
def fonk2(Lk_1, a1):
    b2 = []
    for i in Lk_1:
        for j in Lk_1:
            b3 = i.union(j)
            if(len(b3) == a1):
                if(fonk1(b3,Lk_1)==False):
                    b2.append(b3)
    b4 = set(b2)
    return list(b4)
def fonk3(b10, b20):
    b5 = []
    for row in b10:
        b5.append(set(row))
    b6 = defaultdict(int)
    for row in b5:
        for item in row:
            b6[item]+=1
    b7 = len(b10)
    b8 = []
    for key, value in b6.items():
        b9 = []
        if float(value)/b7 >= b20:
            print(key)
            print(float(value)/b7)
            b9.append(key)
            b8.append(frozenset(b9))
    return b8
def fonk4(database, b20):
    b10 = []
    for row in database:
        b10.append(row)
    b5 = []
    for row in b10:
        b5.append(frozenset(row))
    b8 = []
    b8.append(frozenset())
    b8.append(fonk3(b10, b20))
    a1 = 2
    b11 = []
    b11.append(frozenset())
    b11.append(frozenset())
    b12 = len(b5)
    while(len(b8[a1-1])!=0):
        b11.append(fonk2(b8[a1-1],a1))
        b13 = defaultdict(int)
        for b3 in b11[a1]:
            for s in b5:
                if b3.issubset(s):
                    b13[b3] += 1
        b9 = []
        for key, value in b13.items():
            if float(value)/b12 >= b20:
                print(key)
                print(float(value)/b12)
                b9.append(key)
        b8.append(frozenset(b9))
        a1 += 1
    return b8
def fonk5():
    b14 = OptionParser()
    b14.add_option(
        '-f',
        '--inputFile',
        b15 = 'input',
        b16 = 'filename containing csv',
        b17 = None)
    b14.add_option(
        '-s',
        '--minSupport',
        b15 = 'minS',
        b16 = 'minimum support value',
        b17 = 0.15,
        b18 = 'float')
    (options, args) = b14.parse_args()
    b19 = open(options.input, 'r')
    b20 = options.minS
    b21 = csv.reader(b19)
    b8 = fonk4(b21, b20)
    print(b8)
if b22 = = '__main__': fonk5()
   README Content:
The dataset is come from the UCI Adult Census Dataset.
To run the apriori with dataset provided and the minSupport(b17 = 0.5):
python3 apriori.py âf adult.data.csv -s 0.4
