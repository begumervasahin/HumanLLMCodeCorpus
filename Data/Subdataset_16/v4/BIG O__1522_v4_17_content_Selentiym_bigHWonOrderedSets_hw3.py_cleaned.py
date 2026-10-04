from bondartsev_nikita.classes import *
import csv
b1 = ["RealParam"] * 14
b2 = "hw3.csv"
def fonk1(b1, dataLine, b3 = '') -> 'AObject':
    b4 = []
    for ind, value in enumerate(dataLine):
        b5 = getattr(paramClasses, b1[ind])
        b4.append(b5.instantiate(value))
    return Object(b4, b3)
with open(b2, 'r') as f:
    b6 = csv.b6(f)
    b7 = list(b6)
b8 = fonk1(b1, ['__head'] * len(b1)).dash()
b9 = Context(b8)
for counter, dataLine in enumerate(b7, b10 = 1):
    b11 = fonk1(b1, dataLine, str(counter))
    b9.addObject(b11)
def fonk2(b12):
    b12 = sorted(b12, key=lambda x: str(x))
    for b11 in b12:
        print('o' + str(b11), b13 = ',')
    print()
def fonk3(b12: set, toUse: set) -> int:
    if not toUse:
        b14 = None
        for b11 in b12:
            b14 = b11.dash() if b14 is None else b14.intersect(b11.dash())
        if b14:
            b15 = b9.dash(b14)
            if len(b15) == len(b12):
                fonk2(b12)
                return 1
        return 0
    b16 = toUse.pop()
    return (
        fonk3(b12.copy(), toUse.copy()) +
        fonk3(b12 | {b16}, toUse.copy())
    )
fonk3(set(), set(b9.getObjects()))
b17 = list(b9.getObjects())
print("\n")
fonk2([b17[0], b17[1]])
fonk2(b9.dash(b17[0].dash().intersect(b17[1].dash())))