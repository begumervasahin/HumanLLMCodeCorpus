from random import randint
import random
import time
from prettytable import PrettyTable
import sys
from algorithms import *
sys.setrecursionlimit(9000)
b1 = []
b2 = []
a1 = 0
b3 = True
a2 = 0
a3 = 0
b4 = PrettyTable(["Elementos","Mergesort", "Quicksort", "Selection", "Native"])
b4.align["Elementos"], = "l"
b4.align["Mergesort"], = "l"
b4.align["Quicksort"], = "r"
b4.align["Selection"], = "r"
b4.align["Native"], = "r"
while (b3):
        if a1 < 2000:
            random.shuffle(b2)
            a1 += 1
            b3 = randint(1,10000)
            b2.append(b3)
        else:
            a2 += 2000
            b1.append(b2)
            b5 = time.time()
            quicksort(b2)
            b6 = time.time()
            b7 = b5-b6
            b5 = time.time()
            mergesort(b2)
            b6 = time.time()
            b8 = b5-b6
            b5 = time.time()
            selection(b2)
            b6 = time.time()
            b9 = b5-b6
            b5 = time.time()
            b2.sort()
            b6 = time.time()
            b10 = b5-b6
            b4.add_row([a2, "%.2f" % abs(b8), "%.2f" % abs(b7), "%.2f" % abs(b9) , "%.2f" % abs(b10)])
            a1 = 0
            b3 = (True, False)[b9 <= -30.00]
            print(len(b2))
print(b4)