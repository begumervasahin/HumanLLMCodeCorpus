import csv
from bondartsev_nikita.classes import paramClasses, Context, Object
b1 = ["RealParam"] * 14
b2 = "hw3.csv"
def fonk1(b1, data_line, b3 = '') -> 'Object':
    b4 = []
    for ind, value in enumerate(data_line):
        b5 = getattr(paramClasses, b1[ind])
        b4.append(b5.instantiate(value))
    return Object(b4, b3)
with open(b2, 'r') as f:
    b6 = csv.b6(f)
    b7 = list(b6)
b8 = fonk1(b1, ['__head' for _ in b1]).dash()
b9 = Context(b8)
a1 = 0
for data_line in b7:
    a1 += 1
    b10 = fonk1(b1, data_line, str(a1))
    b9.addObject(b10)
def fonk2(objects):
    b11 = sorted(objects, key=lambda x: str(x))
    for b10 in b11:
        print(f'o{b10}', b12 = ',')
    print()
def fonk3(used: set, to_use: set) -> int:
    if not to_use:
        b13 = None
        for b10 in used:
            if b13 is None:
                b13 = b10.dash()
            else:
                b13 = b13.intersect(b10.dash())
        if b13 is None:
            return 0
        b14 = b9.dash(b13)
        if len(b14) == len(used):
            fonk2(used)
            return 1
        else:
            return 0
    b15 = to_use.pop()
    b16 = used.copy()
    b16.add(b15)
    return fonk3(used.copy(), to_use.copy()) + fonk3(b16, to_use.copy())
fonk3(set(), set(b9.getObjects()))
b17 = list(b9.getObjects())
print('\n')
fonk2([b17[0], b17[1]])
print()
fonk2(b9.dash(b17[0].dash().intersect(b17[1].dash())))