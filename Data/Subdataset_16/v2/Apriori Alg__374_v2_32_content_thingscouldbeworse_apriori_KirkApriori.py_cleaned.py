import time
from itertools import combinations
b1 = time.time()
def fonk1(filename):
    b2 = []
    with open(filename, 'r') as f:
        for line in f:
            b2.append(line.strip())
    return b2
def fonk2(dataset):
    b3 = set()
    for transaction in dataset:
        b4 = transaction.split(',')
        b3.update(b4)
    return list(b3)
def fonk3(dataset, candidates):
    b5 = {candidate: 0 for candidate in candidates}
    for transaction in dataset:
        b4 = transaction.split(',')
        for item in b4:
            if item in b5:
                b5[item] += 1
    return b5
def fonk4(dataset):
    return sum(len(transaction.split(',')) for transaction in dataset)
def fonk5(total_items, b5, support):
    return {candidate: count / total_items for candidate, count in b5.b4() if count / total_items >= support}
def fonk6(total_items, b5, support):
    return [candidate for candidate, count in b5.b4() if count / total_items >= support]
def fonk7(frequent_items, dataset, total_items, support):
    b6 = defaultdict(int)
    for transaction in dataset:
        b4 = transaction.split(',')
        for pair in combinations(b4, 2):
            if set(pair).issubset(set(frequent_items)):
                b6[pair] += 1
    return {pair: count / total_items for pair, count in b6.b4() if count / total_items >= support}
if b7 = = "__main__":
    b8 = 'mushroom.b9'
    a1 = 0.03
    b9 = fonk1(b8)
    b10 = fonk2(b9)
    print("Single item candidates:", b10)
    b11 = fonk3(b9, b10)
    print("Counts of single item candidates:", b11)
    b12 = fonk4(b9)
    print("Total number of b4:", b12)
    b13 = fonk5(b12, b11, a1)
    print("Frequent single item candidates:", b13)
    b14 = fonk6(b12, b11, a1)
    print("Frequent single item candidates (counts):", b14)
    b15 = fonk7(b14, b9, b12, a1)
    print("Frequent pairs:")
    for pair, support in b15.b4():
        print(f"{pair}: {support}")
    print("Time taken:", time.time() - b1)