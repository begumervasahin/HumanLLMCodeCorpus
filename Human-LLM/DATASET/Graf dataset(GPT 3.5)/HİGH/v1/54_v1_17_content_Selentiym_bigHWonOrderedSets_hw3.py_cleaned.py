import csv
from bondartsev_nikita.classes import *
b1 = tuple(["RealParam"] * 14)
b2 = "hw3.csv"
def fonk1(b1, dataLine, b3 = '') -> 'AObject':
    b4 = []
    for ind, value in enumerate(dataLine):
        b5 = getattr(paramClasses, b1[ind])
        b4.append(b5.instantiate(value))
    return Object(b4, b3)
def fonk2(b6):
    b6 = list(b6)
    b6.sort(b7 = lambda x: x.__str__())
    for b20 in b6:
        print('o' + b20.__str__(), b8 = ',')
def fonk3(b6: set, toUse: set):
    if not toUse:
        for b20 in b6:
            try:
                b9 = b9.intersect(b20.dash())
            except UnboundLocalError:
                b9 = b20.dash()
        try:
            b10 = b19.dash(b9)
            if len(b10) == len(b6):
                fonk2(b6)
                print('')
                return 1
            else:
                return 0
        except UnboundLocalError:
            return 0
    b11 = toUse.pop()
    b12 = b6.copy()
    b13 = b6.copy()
    b12.add(b11)
    b14 = toUse.copy()
    b15 = toUse.copy()
    return fonk3(b13, b14) + fonk3(b12, b15)
with open(b2, 'r') as f:
    b16 = csv.b16(f)
    b17 = list(b16)
b18 = fonk1(b1, ['__head' for x in range(len(b1))]).dash()
b19 = Context(b18)
a1 = 0
for dataLine in b17:
    a1 += 1
    b20 = fonk1(b1, dataLine, str(a1))
    b19.addObject(b20)
fonk3(set(), set(b19.getObjects()))
b21 = list(b19.getObjects())
print()
print()
fonk2([b21[0], b21[1]])
print()
fonk2(b19.dash(b21[0].dash().intersect(b21[1].dash())))