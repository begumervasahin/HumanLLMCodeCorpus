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
b4 = set([item for sublist in b3 for item in sublist])
def fonk1():
    a4 = 0
    for key, value in b1.items():
        if len(key) == a3 - 1:
            if value > a4:
                a4 = value
    if np.logical_and(a4 < a1, a3 > 1):
        return False
    else:
        return True
def fonk2():
    global a3
    if fonk1():
        b5 = list(it.b5(b4, a3))
        fonk3(b5)
    else:
        fonk6()
def fonk3(comb):
    global a3
    b6 = set(comb)
    for b7 in comb:
        for b8 in b3:
            fonk4(b7, b8)
    a3 += 1
    fonk2()
def fonk4(el, ro):
    b7 = ''.join(sorted(el))
    b8 = ''.join(sorted(ro))
    b8 = fonk5(b7, b8)
    if b7 in b8:
        if b7 in b1:
            b1[b7] += 1
        else:
            b1[b7] = 1
def fonk5(el, ro):
    b8 = ro[:]
    for row_char in ro:
        if row_char not in el:
            b8 = b8.replace(row_char, '')
    return b8
def fonk6():
    print(b1)
    for key, value in b1.items():
        if value >= a1:
            print(f'Elements: {key} support {value}')
if b9 = = "__main__":
    fonk2()