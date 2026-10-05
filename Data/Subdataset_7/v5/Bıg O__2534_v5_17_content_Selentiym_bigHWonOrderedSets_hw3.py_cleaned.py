import csv
from bondartsev_nikita.classes import *
b1 = ["RealParam"] * 14
b2 = "hw3.csv"
def fonk1(filename):
    with open(filename, 'r') as file:
        b3 = csv.b3(file)
        return list(b3)
def fonk2(b1, data_line, b4 = ''):
    b5 = []
    for index, value in enumerate(data_line):
        b6 = getattr(paramClasses, b1[index])
        b5.append(b6.instantiate(value))
    return Object(b5, b4)
def fonk3(b19):
    b7 = sorted(b19, key=lambda b18: str(b18))
    for b18 in b7:
        print('o' + str(b18), b8 = ',')
def fonk4(used, to_use, b17):
    if len(to_use) == 0:
        b5 = None
        for b18 in used:
            b5 = b18.dash() if b5 is None else b5.intersect(b18.dash())
        try:
            b9 = b17.dash(b5)
            if len(b9) == len(used):
                fonk3(used)
                print('')
                return 1
            else:
                return 0
        except UnboundLocalError:
            return 0
    b10 = to_use.pop()
    b11 = used.copy()
    b12 = used.copy()
    b11.add(b10)
    b13 = to_use.copy()
    b14 = to_use.copy()
    return fonk4(b12, b13, b17) + fonk4(b11, b14, b17)
def fonk5():
    b15 = fonk1(b2)
    b16 = fonk2(b1, ['__head' for _ in range(len(b1))]).dash()
    b17 = Context(b16)
    a1 = 0
    for data_line in b15:
        a1 += 1
        b18 = fonk2(b1, data_line, str(a1))
        b17.addObject(b18)
    b19 = set(b17.getObjects())
    fonk4(set(), b19.copy(), b17)
    print()
    print()
    fonk3([b19[0], b19[1]])
    print()
    b20 = b19[0].dash().intersect(b19[1].dash())
    fonk3(b17.dash(b20))
if b21 = = "__main__":
    fonk5()