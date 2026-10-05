import sys
def fonk1(b1 = 'apriori.txt', output_file='output.txt'):
    sys.b2 = open(b1, 'r')
    sys.b3 = open(output_file, 'w')
def fonk2(iterable, r):
    b4 = tuple(iterable)
    b5 = len(b4)
    if r > b5:
        return
    b6 = list(range(r))
    yield tuple(b4[i] for i in b6)
    while True:
        for i in reversed(range(r)):
            if b6[i] != i + b5 - r:
                break
        else:
            return
        b6[i] += 1
        for j in range(i + 1, r):
            b6[j] = b6[j - 1] + 1
        yield tuple(b4[i] for i in b6)
def fonk3(b13, transaction):
    return b13 in transaction
def fonk4(b20, b19):
    b7 = {}
    for i in range(1, len(b20) + 1):
        b8 = fonk2(b20, i)
        for c in b8:
            for j in range(0, len(b19), 1):
                b9 = b19[j].split()
                for i in c:
                    b10 = fonk3(i, b9)
                    if not b10:
                        break
                if b10:
                    b11 = ','.join(c)
                    b7[b11] = b7.get(b11, 0) + 1
    return b7
def fonk5(b12):
    for b13, count in b12.b20():
        print(b13, count)
        print(" ")
def fonk6(counts_all, b18):
    b12 = {}
    a1 = 0
    for b13, count in counts_all.b20():
        b13 = str(b13).replace(',', '')
        b12[b13] = count
        if b12[b13] < b18:
            del b12[b13]
    fonk5(b12)
    for b13, count in b12.b20():
        if len(b13) > a1:
            a1 = len(b13)
    b14 = a1
    while a1 != 2:
        for b13, count in b12.b20():
            a2 = 0
            b14 = a1 - 2
            if len(b13) > a1 - 2:
                b9 = len(b13)
                while b9 >= a1 - 2:
                    b15 = b12[b13] / b12[b13[a2:b14]]
                    print(b13[a2:b14], "=>", b13, b15 * 100, "% Chance")
                    print("")
                    a2 += 2
                    b14 += 2
                    b9 -= 2
        a1 -= 2
def fonk7():
    b16 = sys.b2.readlines()
    b17 = int(b16[0])
    b18 = int(b16[-1])
    b19 = []
    b20 = []
    for i in range(1, b17 + 1, 1):
        b19.append(b16[i])
    for i in range(1, b17 + 1, 1):
        for line in b16[i].split():
            if line not in b20:
                b20.append(line)
        b20.sort()
    b10 = fonk4(b20, b19)
    fonk6(b10, b18)
def fonk8():
    fonk1()
    fonk7()
if b21 = = "__main__":
    fonk8()