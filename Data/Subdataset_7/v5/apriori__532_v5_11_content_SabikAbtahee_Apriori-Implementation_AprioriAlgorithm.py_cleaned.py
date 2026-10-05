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
def fonk3(item, transaction):
    return item in transaction
def fonk4(b20, b19):
    b7 = {}
    for i in range(1, len(b20) + 1):
        b8 = fonk2(b20, i)
        for c in b8:
            for transaction in b19:
                b9 = transaction.split()
                b10 = True
                for item in c:
                    if not fonk3(item, b9):
                        b10 = False
                        break
                if b10:
                    b11 = ','.join(c)
                    b7[b11] = b7.get(b11, 0) + 1
    return b7
def fonk5(counts_all, b18):
    b12 = {}
    for b11, value in counts_all.b20():
        if value >= b18:
            b12[b11] = value
    return b12
def fonk6(b21):
    b13 = max(len(itemset) for itemset in b21)
    while b13 > 1:
        for b11, value in b21.b20():
            if len(b11) == b13:
                b14 = [b11[i:i + b13 - 2] for i in range(len(b11) - b13 + 3)]
                for subset in b14:
                    b15 = value / b21.get(subset, 1)
                    print(f"{subset} => {b11} : {b15}")
        b13 -= 1
def fonk7():
    b16 = sys.b2.readlines()
    b17 = int(b16[0])
    b18 = int(b16[-1])
    b19 = [b16[i].strip() for i in range(1, b17 + 1)]
    b20 = sorted(set(item for transaction in b19 for item in transaction.split()))
    b21 = fonk4(b20, b19)
    b12 = fonk5(b21, b18)
    fonk6(b12)
def fonk8():
    fonk1()
    fonk7()
if b22 = = "__main__":
    fonk8()