import csv
import itertools
import math
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = {}
def fonk1(filename):
    with open(filename, "r") as file:
        b7 = csv.b7(file)
        a1 = 0
        for row in b7:
            b1.append(row)
            a1 += 1
    print("CREATED LIST ITEMS WITH DUPLICATES:\n", a1, len(b1), b1)
    return b1, a1
def fonk2(a1):
    b8 = math.exp(-0.4 * a1 - 0.2) + 0.2
    b9 = b8 * a1 / 100
    return b8, b9
def fonk3(b1):
    for sublist in b1:
        b2.extend(sublist)
    print("ONLY ONE LIST with duplicates:\n", len(b2), b2)
    return b2
def fonk4(seq, b10 = None):
    if b10 is None:
       def fonk5(x): return x
    b11 = {}
    for item in seq:
       b12 = fonk5(item)
       if b12 in b11:
           continue
       b11[b12] = 1
       b3.append(item)
    print("DUPLICATES REMOVED LIST:\n", len(b3), b3)
    return b3
def fonk6(b3):
    b6 = {item: index + 1 for index, item in enumerate(b3)}
    print('b13 = ', b6)
    for key in sorted(b6.keys()):
        print("%s: %s" % (key, b6[key]))
    return b6
def fonk7(b1, b6):
    for sublist in b1:
        b14 = [b6[item] for item in sublist]
        b4.append(b14)
    print("MAPPER LIST:\n", b4)
    return b4
def fonk8(b4, b3):
    for sublist in b4:
        b15 = [0] * len(b3)
        for item_index in sublist:
            b15[item_index - 1] = 1
        b5.append(b15)
    print("b5:\n", b5)
    return b5
