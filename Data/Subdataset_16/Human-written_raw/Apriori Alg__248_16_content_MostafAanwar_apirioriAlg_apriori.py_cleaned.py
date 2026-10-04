16. Repository: MostafAanwar/apirioriAlg
   File: apriori.py
   URL: https:
   Code Content:
import collections
from idlelib.multicall import r
import numpy as np
import pandas as pd
from collections import Counter
import itertools
from itertools import chain
from itertools import permutations
from tkinter import *
from itertools import *
import imaplib
'''
b1 = Tk()
b2 = Label(b1, text="Read %", fg="green")
b3 = Entry(b1)
b4 = Label(b1, text="Min support", fg="green")
b5 = Entry(b1)
b6 = Label(b1, text="Min confidence", fg="green")
b7 = Entry(b1)
b2.grid(b8 = 0, sticky=E)
b3.grid(b8 = 0, column=1)
b4.grid(b8 = 1, sticky=E)
b5.grid(b8 = 1, column=1)
b6.grid(b8 = 2, sticky=E)
b7.grid(b8 = 2, column=1)
b9 = Button(b1, text="Submit")
b9.grid(b10 = 2)
b1.mainloop()
'''
b11 = open("CarSales.txt", "r")
b12 = sum(1 for line in open('CarSales.txt'))
b13 = int(input("How many % of b16 you want to read?"))
b14 = int(input("What is the minimum support?"))
b15 = int(input("What is the % of the minimum confidence"))
b16 = int((b13 / 100) * b12)
b17 = pd.read_csv("CarSales.txt", sep=' ', header=None, nrows=b16).values
b18 = dict()
for quad in b17:
    b19 = []
    for b29 in range(1, 5):
        for a in itertools.b19(quad, b29):
            b19.append(a)
    for comb in b19:
        if comb in b18:
            b18[comb] = b18[comb] + 1
        else:
            b18[comb] = 1
b20 = dict(b18)
for (key, value) in b20.items():
    if value < b14:
        del b18[key]
print("Dic after", b18)
b21 = max(len(x) for x in b18)
b22 = (lambda k: [l for l in b18 if len(l) == k])(len(max(b18, key=len)))
b23 = [b18[b29] for b29 in b22]
b24 = []
for x in range(0, len(b22)):
    for y in range(0, len(b22[0])):
        if b22[x][y] in b24:
            continue
        else:
            b24.append(b22[x][y])
b25 = []
for quad in b22:
    for b29 in range(1, 3):
        for a in itertools.b19(quad, b29):
            b25.append(a)
b26 = list(permutations(b24, b21))
b27 = []
for b29 in list(b24):
    b28 = [b29]
    for j in list(b24):
        if b29 = = j:
            continue
        else:
            b28.append(j)
    b27.append(b28)
    b27.append(b28[::-1])
   README Content:
Apriori is an algorithm for frequent item set mining and association rule learning over relational databases. It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets as long as those item sets appear sufficiently often in the database.
