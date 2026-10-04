import csv
from bondartsev_nikita.classes import paramClasses, Context, Object
b1 = ["RealParam"] * 14
b2 = "hw3.csv"
def fonk1(b1, dataLine, b3 = '') -> 'Object':
    b4 = []
    for ind, value in enumerate(dataLine):
        b5 = getattr(paramClasses, b1[ind])
        b4.append(b5.instantiate(value))
    return Object(b4, b3)
with open(b2, 'r') as f:
    b6 = csv.b6(f)
    b7 = list(b6)
b8 = fonk1(b1, ['__head' for _ in b1]).dash()
b9 = Context(b8)
a1 = 0
for dataLine in b7:
    a1 += 1
    b10 = fonk1(b1, dataLine, str(a1))
    b9.addObject(b10)
def fonk2(b11):
    b11 = list(b11)
    b11.sort(b12 = lambda x: str(x))
    for b10 in b11:
        print(f'o{b10}', b13 = ',')
def fonk3(b11: set, toUse: set) -> int:
    if not toUse:
        b14 = None
        for b10 in b11:
            if b14 is None:
                b14 = b10.dash()
            else:
                b14 = b14.intersect(b10.dash())
        if b14 is None:
            return 0
        b15 = b9.dash(b14)
        if len(b15) == len(b11):
            fonk2(b11)
            print('')
            return 1
        else:
            return 0
    b16 = toUse.pop()
    b17 = b11.copy()
    b17.add(b16)
    return fonk3(b11.copy(), toUse.copy()) + fonk3(b17, toUse.copy())
fonk3(set(), set(b9.getObjects()))
b18 = list(b9.getObjects())
print('\n')
fonk2([b18[0], b18[1]])
print()
fonk2(b9.dash(b18[0].dash().intersect(b18[1].dash())))