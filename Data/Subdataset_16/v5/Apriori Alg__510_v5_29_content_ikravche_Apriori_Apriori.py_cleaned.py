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
    a4 = 0
    for itemset, support in b1.items():
        if len(itemset) == a3 - 1:
            if support > a4:
                a4 = support
    return a4 >= a1 or a3 = = 1
def fonk2():
    if fonk1():
        b4 = list(it.b4(b3, a3))
        fonk3(b4)
    else:
        fonk6()
def fonk3(b4):
    global a3
    for combination in b4:
        for transaction in b2:
            fonk4(combination, transaction)
    a3 += 1
    fonk2()
def fonk4(combination, transaction):
    b5 = ''.join(sorted(combination))
    b6 = ''.join(sorted(transaction))
    b7 = fonk5(b5, b6)
    if b5 in b7:
        if b5 in b1:
            b1[b5] += 1
        else:
            b1[b5] = 1
def fonk5(itemset, transaction):
    return ''.join([char for char in transaction if char in itemset])
def fonk6():
    for itemset, support in b1.items():
        if support >= a1:
            print(f'Itemset: {itemset} Support: {support}')
if b8 = = "__main__":
    fonk2()