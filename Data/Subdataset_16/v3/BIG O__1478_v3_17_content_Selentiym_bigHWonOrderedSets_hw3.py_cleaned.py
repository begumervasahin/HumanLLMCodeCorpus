import csv
from bondartsev_nikita.classes import paramClasses, Context, Object
b1 = ["RealParam"] * 14
b2 = "hw3.csv"
def fonk1(b1, data_line, b3 = '') -> 'Object':
    b4 = [getattr(paramClasses, b1[ind]).instantiate(value) for ind, value in enumerate(data_line)]
    return Object(b4, b3)
def fonk2(filename):
    with open(filename, 'r') as f:
        b5 = csv.b5(f)
        return list(b5)
def fonk3(b1, b15):
    b6 = fonk1(b1, ['__head' for _ in b1]).dash()
    b7 = Context(b6)
    for counter, data_line in enumerate(b15, b8 = 1):
        b9 = fonk1(b1, data_line, str(counter))
        b7.addObject(b9)
    return b7
def fonk4(objects):
    b10 = sorted(objects, key=lambda x: str(x))
    print(','.join(f'o{b9}' for b9 in b10))
def fonk5(used: set, to_use: set, b7: Context) -> int:
    if not to_use:
        b11 = None
        for b9 in used:
            if b11 is None:
                b11 = b9.dash()
            else:
                b11 = b11.intersect(b9.dash())
        if b11 is None:
            return 0
        b12 = b7.dash(b11)
        if len(b12) == len(used):
            fonk4(used)
            return 1
        return 0
    b13 = to_use.pop()
    b14 = used.copy()
    b14.add(b13)
    return fonk5(used.copy(), to_use.copy(), b7) + fonk5(b14, to_use.copy(), b7)
def fonk6():
    b15 = fonk2(b2)
    b16 = fonk3(b1, b15)
    fonk5(set(), set(b16.getObjects()), b16)
    b17 = list(b16.getObjects())
    print('\n')
    fonk4([b17[0], b17[1]])
    print()
    fonk4(b16.dash(b17[0].dash().intersect(b17[1].dash())))
if b18 = = "__main__":
    fonk6()