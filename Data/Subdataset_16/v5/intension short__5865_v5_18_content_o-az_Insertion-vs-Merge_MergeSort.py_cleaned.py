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
def fonk2(left, right):
    global a1
    b4 = []
    b5 = j = 0
    while b5 < len(left) and j < len(right):
        a1 += 1
        if left[b5] < right[j]:
            b4.append(left[b5])
            b5 += 1
        else:
            b4.append(right[j])
            j += 1
    b4.extend(left[b5:])
    b4.extend(right[j:])
    return b4
def fonk3(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def fonk4(b6, description):
    global a1
    print(f'Testing on {description}')
    a1 = 0
    print(f'{description} sorted')
    fonk1(b6.copy())
    print('Number of comparisons:', a1)
    a1 = 0
    print(f'{description} reversed')
    fonk1(list(reversed(b6)))
    print('Number of comparisons:', a1)
    a1 = 0
    print(f'{description} random')
    random.shuffle(b6)
    fonk1(b6.copy())
    print('Number of comparisons:', a1)
    print('-------------\n')
def fonk5():
    b6 = fonk3('b6.txt')
    b7 = len(b6)
    print(f'Total b6: {b7}\n')
    b8 = [
        (b6[0:10], "10 b6"),
        (b6[0:30], "30 b6"),
        (b6[0:100], "100 b6"),
        (b6[0:300], "300 b6"),
        (b6[0:1000], "1000 b6"),
        (b6[0:3000], "3000 b6"),
        (b6[0:10000], "10000 b6"),
        (b6, "all b6"),
    ]
    for case, description in b8:
        fonk4(case, description)
if b9 = = "__main__":
    fonk5()