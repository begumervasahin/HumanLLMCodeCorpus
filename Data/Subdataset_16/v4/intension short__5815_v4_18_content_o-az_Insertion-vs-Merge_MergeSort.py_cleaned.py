import random
a1 = 0
def fonk1(lst):
    global a1
    if len(lst) <= 1:
        return lst
    b1 = len(lst)
    b2 = fonk1(lst[:b1])
    b3 = fonk1(lst[b1:])
    return fonk2(b2, b3)
def fonk2(b2, b3):
    global a1
    b4 = []
    b5 = j = 0
    while b5 < len(b2) and j < len(b3):
        a1 += 1
        if b2[b5] < b3[j]:
            b4.append(b2[b5])
            b5 += 1
        else:
            b4.append(b3[j])
            j += 1
    b4.extend(b2[b5:])
    b4.extend(b3[j:])
    return b4
def fonk3(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def fonk4(b7, description):
    global a1
    print(f'Testing on {description}')
    print(f'{description} sorted')
    fonk1(b7)
    print('Number of comparisons:', a1)
    print(f'{description} reversed')
    b6 = list(reversed(b7))
    fonk1(b6)
    print('Number of comparisons:', a1)
    print(f'{description} random')
    random.shuffle(b7)
    fonk1(b7)
    print('Number of comparisons:', a1)
    print('-------------\n')
def fonk5():
    global a1
    b7 = fonk3('b7.txt')
    b8 = len(b7)
    print(f'Total b7: {b8}\n')
    b9 = [
        (b7[0:10], "10 b7"),
        (b7[0:30], "30 b7"),
        (b7[0:100], "100 b7"),
        (b7[0:300], "300 b7"),
        (b7[0:1000], "1000 b7"),
        (b7[0:3000], "3000 b7"),
        (b7[0:10000], "10000 b7"),
        (b7, "all b7"),
    ]
    for case, description in b9:
        a1 = 0
        fonk4(case, description)
if b10 = = "__main__":
    fonk5()