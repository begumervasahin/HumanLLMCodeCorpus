import random
a1 = 0
def fonk1(lst):
    global a1
    if len(lst) <= 1:
        a1 += 1
        return lst
    b1 = len(lst)
    b2 = fonk1(lst[:b1])
    b3 = fonk1(lst[b1:])
    return fonk2(b2, b3)
def fonk2(b2, b3):
    global a1
    b4 = []
    a2 = 0
    a3 = 0
    while a2 < len(b2) and a3 < len(b3):
        if b2[a2] < b3[a3]:
            a1 += 1
            b4.append(b2[a2])
            a2 += 1
        else:
            b4.append(b3[a3])
            a3 += 1
    a1 += 1
    b4 += b2[a2:]
    b4 += b3[a3:]
    return b4
def fonk3(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def fonk4(b7, size):
    global a1
    a1 = 0
    b5 = random.sample(b7, size)
    b6 = fonk1(b5)
    print(f'Testing on {size} b7:')
    print('Sorted b7:', b6)
    print('Number of comparisons:', a1)
    print()
def fonk5():
    b7 = fonk3('b7.txt')
    b8 = [10, 30, 100, 300, 1000, 3000, 10000, len(b7)]
    for size in b8:
        fonk4(b7, size)
if b9 = = "__main__":
    fonk5()