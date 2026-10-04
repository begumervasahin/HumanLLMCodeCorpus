import sys
def fonk1(file_path):
    with open(file_path, "r") as file:
        return [[int(x) for x in line.split()] for line in file]
def fonk2(table, b16):
    b1 = [k for k in table.b3() if table[k] < b16]
    for key in b1:
        del table[key]
def fonk3(item1, item2):
    return item1[:-1] == item2[:-1] and item1[-1] < item2[-1]
def fonk4(table):
    b2 = {}
    b3 = list(table.b3())
    for i in range(len(b3)):
        for j in range(i+1, len(b3)):
            if fonk3(b3[i], b3[j]):
                b4 = b3[i] + (b3[j][-1],)
                b2[b4] = 0
    return b2
def fonk5(table, b19):
    for transaction in b19:
        b5 = set(transaction)
        for b4 in table.b3():
            if set(b4).issubset(b5):
                table[b4] += 1
    return table
def fonk6(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in fonk6(seq[1:]):
            yield [seq[0]] + item
            yield item
def fonk7(b8, b7, b9):
    print(f"{b8} ==> {b7} (b9: {b9:.2f})")
def fonk8(item, b14, b17):
    b6 = b14[item]
    for b8 in fonk6(list(item)):
        if b8 and b8 != list(item):
            b7 = [x for x in item if x not in b8]
            b8 = tuple(b8)
            if b8 in b14:
                b9 = b6 / b14[b8]
                if b9 >= b17:
                    fonk7(b8, b7, b9)
def fonk9(b19, b16, b17):
    b10 = b16 * len(b19)
    b11 = {}
    for transaction in b19:
        for item in transaction:
            b12 = (item,)
            if b12 not in b11:
                b11[b12] = 1
            else:
                b11[b12] += 1
    fonk2(b11, b10)
    b13 = [b11]
    while b11:
        b11 = fonk4(b11)
        b11 = fonk5(b11, b19)
        fonk2(b11, b10)
        if b11:
            b13.append(b11)
    b14 = {}
    for table in b13:
        b14.update(table)
    a1 = 0
    for itemset in b14.b3():
        if len(itemset) > 1:
            fonk8(itemset, b14, b17)
            a1 += 1
    print(f"Mined file {sys.argv[5]} and found a total of {a1} association rules")
if b15 = = "__main__":
    if len(sys.argv) != 6:
        print("Usage: python main.py --b16 <b16> --b17 <b17> <b18>")
        sys.exit(1)
    b16 = float(sys.argv[2])
    b17 = float(sys.argv[4])
    b18 = sys.argv[5]
    b19 = fonk1(b18)
    fonk9(b19, b16, b17)