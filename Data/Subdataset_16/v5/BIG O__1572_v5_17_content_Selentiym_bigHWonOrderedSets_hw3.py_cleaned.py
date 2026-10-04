from bondartsev_nikita.classes import *
import csv
b1 = ["RealParam"] * 14
b2 = "hw3.csv"
def fonk1(b1, data_line, b3 = '') -> 'AObject':
    b4 = [
        getattr(paramClasses, b1[ind]).instantiate(value)
        for ind, value in enumerate(data_line)
    ]
    return Object(b4, b3)
with open(b2, 'r') as file:
    b5 = csv.b5(file)
    b6 = list(b5)
b7 = fonk1(b1, ['__head'] * len(b1)).dash()
b8 = Context(b7)
for counter, data_line in enumerate(b6, b9 = 1):
    b10 = fonk1(b1, data_line, str(counter))
    b8.addObject(b10)
def fonk2(b15):
    b11 = sorted(b15, key=lambda x: str(x))
    print(','.join('o' + str(b10) for b10 in b11))
def fonk3(used: set, to_use: set) -> int:
    if not to_use:
        b12 = None
        for b10 in used:
            b12 = b10.dash() if b12 is None else b12.intersect(b10.dash())
        if b12:
            b13 = b8.dash(b12)
            if len(b13) == len(used):
                fonk2(used)
                return 1
        return 0
    b14 = to_use.pop()
    return (
        fonk3(used.copy(), to_use.copy()) +
        fonk3(used | {b14}, to_use.copy())
    )
fonk3(set(), set(b8.getObjects()))
b15 = list(b8.getObjects())
print("\n")
fonk2([b15[0], b15[1]])
fonk2(b8.dash(b15[0].dash().intersect(b15[1].dash())))