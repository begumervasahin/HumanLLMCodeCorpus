import sys
def fonk1(b11):
    b1 = []
    with open(b11, "r") as file:
        for line in file:
            b1.append([int(x) for x in line.split()])
    return b1
def fonk2(b9, total_transactions):
    return b9 * total_transactions
def fonk3(b14, b9):
    b2 = [a1 for a1 in b14.keys() if b14[a1] < b9]
    for b3 in b2:
        del b14[b3]
def fonk4(l1, l2):
    b3 = list(l1[:-1])
    b3.extend([l1[-1], l2[-1]])
    return tuple(b3)
def fonk5(l1, l2):
    return l1[:-1] == l2[:-1] and l1[-1] < l2[-1]
def fonk6(b14):
    b4 = {}
    for l1 in b14.keys():
        for l2 in b14.keys():
            if fonk5(l1, l2):
                b4[fonk4(l1, l2)] = 0
    return b4
def fonk7(b14, db):
    for a1 in b14.keys():
        for transaction in db:
            if set(a1).issubset(transaction):
                b14[a1] += 1
def fonk8(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in fonk8(seq[1:]):
            yield [seq[0]] + item
            yield item
def fonk9(b5, b6, b7):
    print(f"{b5} ==> {b6}              {b7:.2f}")
def fonk10(item, b15):
    global a2
    for b5 in fonk8(list(item)):
        if not b5 or b5 = = list(item):
            continue
        b6 = [x for x in item if x not in b5]
        b7 = b15[item] / b15[tuple(b5)]
        if b7 >= b10:
            fonk9(b5, b6, b7)
            a2 += 1
if b8 = = "__main__":
    b9 = float(sys.argv[1])
    b10 = float(sys.argv[2])
    b11 = sys.argv[3]
    b12 = fonk1(b11)
    b9 = fonk2(b9, len(b12))
    b13 = []
    b14 = {}
    for transaction in b12:
        for item in transaction:
            if (item,) not in b14.keys():
                b14[(item,)] = 1
            else:
                b14[(item,)] += 1
    fonk3(b14, b9)
    b13.append(b14)
    a1 = 1
    while len(b13[a1-1]) != 0:
        b14 = fonk6(b13[a1-1])
        fonk7(b14, b12)
        fonk3(b14, b9)
        b13.append(b14)
        a1 += 1
    b13.pop()
    b15 = {}
    for level in b13:
        b15.update(level)
    a2 = 0
    for item in b15.keys():
        if len(item) > 1:
            fonk10(item, b15)
    print(f"Mined file {b11}")
    print(f"Found a total of {a2} association rules")