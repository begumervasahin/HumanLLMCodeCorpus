from bondartsev_nikita.classes import *
b1 = []
for j in range(0, 14):
    b1.append("RealParam")
b1 = tuple(b1)
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
b8 = fonk1(b1,['__head' for x in range(0, b1.__len__())]).dash()
b9 = Context(b8)
a1 = 0
for dataLine in b7:
    a1 += 1
    b10 = fonk1(b1,dataLine, str(a1))
    b9.addObject(b10)
def fonk2(b11):
    b11 = list(b11)
    b11.sort(b12 = lambda x: x.__str__())
    for b10 in b11:
        print('o' + b10.__str__(), b13 = ',')
def fonk3(b11: Set, toUse: Set):
    if toUse.__len__() == 0:
        for b10 in b11:
            try:
                b14 = b14.intersect(b10.dash())
            except UnboundLocalError:
                b14 = b10.dash()
        try:
            b15 = b9.dash(b14)
            if b15.__len__() == b11.__len__():
                fonk2(b11)
                print('')
                return 1
            else:
                return 0
        except UnboundLocalError:
            return 0
    b16 = toUse.pop()
    b17 = b11.copy()
    b18 = b11.copy()
    b17.add(b16)
    b19 = toUse.copy()
    b20 = toUse.copy()
    return fonk3(b18, b19) + fonk3(b17, b20)
fonk3(set(),set(b9.getObjects()))
b21 = list(b9.getObjects())
print()
print()
fonk2([b21[0],b21[1]])
print()
fonk2(b9.dash(b21[0].dash().intersect(b21[1].dash())))