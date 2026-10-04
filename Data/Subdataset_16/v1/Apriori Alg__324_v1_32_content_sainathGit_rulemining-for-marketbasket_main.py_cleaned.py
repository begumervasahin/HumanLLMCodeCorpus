import sys
b1 = float(sys.argv[1])
b2 = float(sys.argv[2])
b3 = sys.argv[3]
b4 = []
with open(b3, "r") as tf:
    for line in tf:
        b4.append([int(x) for x in line.split()])
b1 = b1 * len(b4)
def fonk1(b13):
    b5 = [a1 for a1 in b13.keys() if b13[a1] < b1]
    for i in b5:
        del b13[i]
def fonk2(l1, l2):
    b6 = []
    b7 = len(l1) - 1
    b6.extend(l1[:b7])
    b6.append(l1[b7])
    b6.append(l2[b7])
    return tuple(b6)
def fonk3(l1, l2):
    b7 = len(l1) - 1
    for i in range(b7):
        if l1[i] != l2[i]:
            return False
    if l1[b7] >= l2[b7]:
        return False
    return True
def fonk4(b13):
    b8 = {}
    for l1 in b13.keys():
        for l2 in b13.keys():
            if fonk3(l1, l2):
                b8[fonk2(l1, l2)] = 0
    return b8
def fonk5(b13):
    for a1 in b13.keys():
        for t in b4:
            if set(a1).issubset(set(t)):
                b13[a1] += 1
def fonk6(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in fonk6(seq[1:]):
            yield [seq[0]] + item
            yield item
def fonk7(b9, b10, b11):
    print(f"{b9} ==> {b10}              {b11}")
def fonk8(item, b14):
    global a2
    for b9 in fonk6(list(item)):
        if b9 = = [] or b9 == list(item):
            continue
        b10 = [x for x in item if x not in b9]
        b11 = b14[item] / b14[tuple(b9)]
        if b11 > b2:
            fonk7(b9, b10, b11)
            a2 += 1
b12 = []
b13 = {}
for t in b4:
    for x in t:
        if (x,) not in b13.keys():
            b13[(x,)] = 1
        else:
            b13[(x,)] += 1
fonk1(b13)
b12.append(b13)
a1 = 1
while len(b12[a1-1]) != 0:
    b13 = fonk4(b12[a1-1])
    fonk5(b13)
    fonk1(b13)
    b12.append(b13)
    a1 += 1
b12.pop()
b14 = {}
for a1 in range(len(b12)):
    b14.update(b12[a1])
a2 = 0
for item in b14.keys():
    if len(item) > 1:
        fonk8(item, b14)
print(f"mined file {b3}")
print(f"and found a total of {a2} association rules")