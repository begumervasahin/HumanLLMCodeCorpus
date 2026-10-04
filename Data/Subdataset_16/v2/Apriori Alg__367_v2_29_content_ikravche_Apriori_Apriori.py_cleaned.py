import numpy as np
import itertools as it
a1 = 3
a2 = 0.7
a3 = 1
b1 = {}
b2 = {}
b3 = [
    ['a', 'b'],
    ['a', 'c', 'd', 'e'],
    ['a', 'b', 'c', 'e'],
    ['c', 'd'],
    ['b', 'c', 'd', 'e'],
    ['a', 'd', 'e'],
    ['c', 'd', 'e']
]
b4 = set(item for sublist in b3 for item in sublist)
def fonk1():
    a4 = 0
    for key, value in b1.items():
        if len(key) == a3 - 1 and value > a4:
            a4 = value
    return a4 >= a1 or a3 = = 1
def fonk2():
    global a3
    if fonk1():
        b5 = list(it.b5(b4, a3))
        fonk3(b5)
    else:
        fonk6()
def fonk3(b5):
    global a3
    for element in b5:
        for row in b3:
            fonk4(element, row)
    a3 += 1
    fonk2()
def fonk4(element, row):
    b6 = ''.join(sorted(element))
    b7 = ''.join(sorted(row))
    b8 = fonk5(b6, b7)
    if b6 in b8:
        if b6 in b1:
            b1[b6] += 1
        else:
            b1[b6] = 1
def fonk5(element, row):
    return ''.join([char for char in row if char in element])
def fonk6():
    print("Frequent Itemsets:")
    for key, value in b1.items():
        if value >= a1:
            print(f'Elements: {key}, Support: {value}')
if b9 = = "__main__":
    fonk2()