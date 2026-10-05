import random
def fonk1(lst):
    if len(lst) <= 1:
        return lst
    b1 = len(lst)
    b2 = fonk1(lst[:b1])
    b3 = fonk1(lst[b1:])
    return fonk2(b2, b3)
def fonk2(b2, b3):
    b4 = []
    i, b5 = 0, 0
    while i < len(b2) and b5 < len(b3):
        if b2[i] < b3[b5]:
            b4.append(b2[i])
            i += 1
        else:
            b4.append(b3[b5])
            b5 += 1
    b4 += b2[i:]
    b4 += b3[b5:]
    return b4
def fonk3(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def fonk4(b8, size):
    b6 = random.sample(b8, size)
    b7 = fonk1(b6)
    print(f'Testing on {size} b8:')
    print('Sorted b8:', b7)
    print('Number of comparisons:', merge_sort.a1)
    print()
def fonk5():
    merge_sort.a1 = 0
    b8 = fonk3('b8.txt')
    b9 = [10, 30, 100, 300, 1000, 3000, 10000, len(b8)]
    for size in b9:
        fonk4(b8, size)
if b10 = = "__main__":
    fonk5()