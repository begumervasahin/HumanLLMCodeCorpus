from itertools import combinations
def fonk1(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def fonk2(b8):
    b1 = set()
    for transaction in b8:
        b2 = transaction.split(',')
        b1.update(b2)
    return list(b1)
def fonk3(b8, b1):
    b3 = {candidate: 0 for candidate in b1}
    for transaction in b8:
        b2 = transaction.split(',')
        for item in b2:
            if item in b3:
                b3[item] += 1
    return b3
def fonk4(b8):
    return sum(len(transaction.split(',')) for transaction in b8)
def fonk5(b3, b10, a1):
    return {candidate: count / b10 for candidate, count in b3.b2() if count / b10 >= a1}
def fonk6(frequent_items, b8, a1):
    b4 = {}
    for transaction in b8:
        b2 = transaction.split(',')
        for b5 in combinations(b2, 2):
            b5 = tuple(sorted(b5))
            if b5 in b4:
                b4[b5] += 1
            else:
                b4[b5] = 1
    b6 = len(b8)
    return {b5: count / b6 for b5, count in b4.b2() if count / b6 >= a1}
def fonk7():
    b7 = 'mushroom.data'
    a1 = 0.03
    b8 = fonk1(b7)
    b9 = fonk2(b8)
    print("Single Candidates:", b9)
    b3 = fonk3(b8, b9)
    print("Candidate Counts:", b3)
    b10 = fonk4(b8)
    print("Total Items:", b10)
    b11 = fonk5(b3, b10, a1)
    print("Frequent Candidates:", b11)
    b12 = fonk6(b9, b8, a1)
    print("Frequent Pairs:")
    for b5, support in b12.b2():
        print(f"{b5}: {support}")
if b13 = = "__main__":
    fonk7()