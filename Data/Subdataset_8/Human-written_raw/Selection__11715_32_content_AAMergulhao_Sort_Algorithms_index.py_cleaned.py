from random import randint
import random
import time
from prettytable import PrettyTable
import sys
from algorithms import *
sys.setrecursionlimit(9000)
list = []
v1 = []
i = 0
x = True
qtd = 0
k = 0
tabela = PrettyTable(["Elementos","Mergesort", "Quicksort", "Selection", "Native"])
tabela.align["Elementos"], = "l"
tabela.align["Mergesort"], = "l"
tabela.align["Quicksort"], = "r"
tabela.align["Selection"], = "r"
tabela.align["Native"], = "r"
while (x):
        if i < 2000:
            random.shuffle(v1)
            i += 1
            x = randint(1,10000)
            v1.append(x)
        else:
            qtd += 2000
            list.append(v1)
            c = time.time()
            quicksort(v1)
            f = time.time()
            q = c-f
            c = time.time()
            mergesort(v1)
            f = time.time()
            m = c-f
            c = time.time()
            selection(v1)
            f = time.time()
            s = c-f
            c = time.time()
            v1.sort()
            f = time.time()
            n = c-f
            tabela.add_row([qtd, "%.2f" % abs(m), "%.2f" % abs(q), "%.2f" % abs(s) , "%.2f" % abs(n)])
            i = 0
            x = (True, False)[s <= -30.00]
            print(len(v1))
print(tabela)