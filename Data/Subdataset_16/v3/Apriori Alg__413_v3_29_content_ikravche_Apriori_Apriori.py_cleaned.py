import itertools as it
a1 = 3
a2 = 0.7
a3 = 1
b1 = {}
b2 = [
    ['a', 'b'],
    ['a', 'c', 'd', 'e'],
    ['a', 'b', 'c', 'e'],
    ['c', 'd'],
    ['b', 'c', 'd', 'e'],
    ['a', 'd', 'e'],
    ['c', 'd', 'e']
]
b3 = set(item for sublist in b2 for item in sublist)
def fonk1():
    b4 = max((value for key, value in b1.items() if len(key) == a3 - 1), default=0)
    return b4 >= a1 or a3 = = 1
def fonk2():
    global a3
    if fonk1():
        b5 = list(it.b5(b3, a3))
        fonk3(b5)
    else:
        fonk6()
def fonk3(b5):
    global a3
    for combination in b5:
        for transaction in b2:
            fonk4(combination, transaction)
    a3 += 1
    fonk2()
def fonk4(combination, transaction):
    b6 = ''.join(sorted(combination))
    b7 = ''.join(sorted(transaction))
    b8 = fonk5(b6, b7)
    if b6 in b8:
        if b6 in b1:
            b1[b6] += 1
        else:
            b1[b6] = 1
def fonk5(combination, transaction):
    return ''.join([char for char in transaction if char in combination])
def fonk6():
    print("Frequent Itemsets:")
    for combination, support in b1.items():
        if support >= a1:
            print(f'Combination: {combination}, Support: {support}')
if b9 = = "__main__":
    fonk2()