import csv
from bondartsev_nikita.classes import *
b1 = tuple(["RealParam"] * 14)
b2 = "hw3.csv"
def fonk1(config, data_line, b3 = '') -> 'AObject':
    b4 = [getattr(paramClasses, config[ind]).instantiate(value) for ind, value in enumerate(data_line)]
    return Object(b4, b3)
def fonk2(b19):
    b5 = sorted(b19, key=lambda x: x.__str__())
    for b18 in b5:
        print('o' + b18.__str__(), b6 = ',')
def fonk3(used: set, to_use: set) -> int:
    if not to_use:
        b7 = None
        for b18 in used:
            try:
                b7 = b7.intersect(b18.dash())
            except UnboundLocalError:
                b7 = b18.dash()
        try:
            b8 = b17.dash(b7)
            if len(b8) == len(used):
                fonk2(used)
                print('')
                return 1
            else:
                return 0
        except UnboundLocalError:
            return 0
    b9 = to_use.pop()
    b10 = used.copy()
    b11 = used.copy()
    b10.add(b9)
    b12 = to_use.copy()
    b13 = to_use.copy()
    return fonk3(b11, b12) + fonk3(b10, b13)
with open(b2, 'r') as file:
    b14 = csv.b14(file)
    b15 = list(b14)
b16 = fonk1(b1, ['__head' for _ in range(len(b1))]).dash()
b17 = Context(b16)
a1 = 0
for data_line in b15:
    a1 += 1
    b18 = fonk1(b1, data_line, str(a1))
    b17.addObject(b18)
fonk3(set(), set(b17.getObjects()))
b19 = list(b17.getObjects())
print()
print()
fonk2([b19[0], b19[1]])
print()
fonk2(b17.dash(b19[0].dash().intersect(b19[1].dash())))