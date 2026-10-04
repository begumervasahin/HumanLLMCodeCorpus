from itertools import combinations
def fonk1(filename):
    b1 = []
    with open(filename, 'r') as fData:
        for line in fData:
            b1.append(line.strip())
    return b1
def fonk2(dataset):
    b1 = []
    for transaction in dataset:
        b2 = transaction.split(',')
        for item in b2:
            if item not in b1:
                b1.append(item)
    return b1
def fonk3(dataset, singles):
    b3 = {}
    for transaction in dataset:
        b2 = transaction.split(',')
        for item in b2:
            for b4 in singles:
                if b4 = = item:
                    b3.setdefault(b4, 0)
                    b3[b4] += 1
    return b3
def fonk4(dataset):
    a1 = 0
    for transaction in dataset:
        b2 = transaction.split(',')
        a1 += len(b2)
    return a1
def fonk5(itemCount, b3, a2):
    b5 = {}
    for b4 in b3:
        if b3[b4] / itemCount >= a2:
            b5[b4] = b3[b4] / itemCount
    return b5
def fonk6(itemCount, b3, a2):
    b6 = []
    for b4 in b3:
        if b3[b4] / itemCount >= a2:
            b6.append(b4)
    return b6
def fonk7(frequentItems, dataset, itemCount, a2):
    b1 = {}
    for transaction in dataset:
        b2 = transaction.split(',')
        for item in combinations(b2, 2):
            b1.setdefault(item, 0)
            b1[item] += 1
    b7 = []
    for key in b1:
        if b1[key] / itemCount < a2:
            b7.append(key)
        else:
            b1[key] = b1[key] / itemCount
    for key in b7:
        b1.pop(key, None)
    return b1
if b8 = = "__main__":
    b9 = 'mushroom.b10'
    a2 = 0.03
    b10 = fonk1(b9)
    b11 = fonk2(b10)
    print("Single item candidates:", b11)
    b12 = fonk3(b10, b11)
    print("Counts of single item candidates:", b12)
    a1 = fonk4(b10)
    print("Total number of b2:", a1)
    b13 = fonk5(a1, b12, a2)
    print("Frequent single item candidates:", b13)
    b14 = fonk6(a1, b12, a2)
    print("Frequent single item candidates (b12):", b14)
    b15 = fonk7(b14, b10, a1, a2)
    print("Frequent b15:")
    for pair in b15:
        print(f"{pair}: {b15[pair]}")
    print("Time taken:", time.time() - start_time)