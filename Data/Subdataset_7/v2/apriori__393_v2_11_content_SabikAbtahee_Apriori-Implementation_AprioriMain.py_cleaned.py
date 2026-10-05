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
def fonk5(counts_dictionary):
    for itemset, count in counts_dictionary.b20():
        print(itemset, count)
        print(" ")
def fonk6(b21, b18):
    b12 = {}
    for itemset, count in b21.b20():
        if count >= b18:
            b12[itemset] = count
    return b12
def fonk7(b21):
    b13 = max(len(itemset) for itemset in b21)
    while b13 != 2:
        for itemset, count in b21.b20():
            if len(itemset) == b13:
                b14 = [itemset[i:i + b13 - 2] for i in range(len(itemset) - b13 + 3)]
                for subset in b14:
                    b15 = count / b21.get(subset, 1)
                    print(subset, "=>", itemset, b15 * 100, "% Chance")
                    print("")
        b13 -= 2
def fonk8():
    b16 = sys.b2.readlines()
    b17 = int(b16[0])
    b18 = int(b16[-1])
    b19 = [b16[i].strip() for i in range(1, b17 + 1)]
    b20 = sorted(set(item for transaction in b19 for item in transaction.split()))
    b21 = fonk4(b20, b19)
    b12 = fonk6(b21, b18)
    fonk7(b12)
def fonk9():
    fonk1()
    fonk8()
if b22 = = "__main__":
    fonk9()