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
def fonk4(b19, b18):
    b7 = {}
    for i in range(1, len(b19) + 1):
        b8 = fonk2(b19, i)
        for c in b8:
            for transaction in b18:
                b9 = transaction.split()
                b10 = all(fonk3(item, b9) for item in c)
                if b10:
                    b11 = ','.join(c)
                    b7[b11] = b7.get(b11, 0) + 1
    return b7
def fonk5(counts_dictionary):
    for itemset, count in counts_dictionary.b19():
        print(itemset, count)
        print(" ")
def fonk6(b20, b17):
    return {itemset: count for itemset, count in b20.b19() if count >= b17}
def fonk7(b20):
    b12 = max(len(itemset) for itemset in b20)
    while b12 != 2:
        for itemset, count in b20.b19():
            if len(itemset) == b12:
                b13 = [itemset[i:i + b12 - 2] for i in range(len(itemset) - b12 + 3)]
                for subset in b13:
                    b14 = count / b20.get(subset, 1)
                    print(subset, "=>", itemset, b14 * 100, "% Chance")
                    print("")
        b12 -= 2
def fonk8():
    b15 = sys.b2.readlines()
    b16 = int(b15[0])
    b17 = int(b15[-1])
    b18 = [b15[i].strip() for i in range(1, b16 + 1)]
    b19 = sorted(set(item for transaction in b18 for item in transaction.split()))
    b20 = fonk4(b19, b18)
    b21 = fonk6(b20, b17)
    fonk7(b21)
def fonk9():
    fonk1()
    fonk8()
if b22 = = "__main__":
    fonk9()