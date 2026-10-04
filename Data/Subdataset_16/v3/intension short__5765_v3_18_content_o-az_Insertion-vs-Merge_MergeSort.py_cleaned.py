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
    i, b5 = 0, 0
    while i < len(b2) and b5 < len(b3):
        if b2[i] < b3[b5]:
            b4.append(b2[i])
            i += 1
        else:
            b4.append(b3[b5])
            b5 += 1
        a1 += 1
    b4.extend(b2[i:])
    b4.extend(b3[b5:])
    a1 += 1
    return b4
def fonk3(b10, num_words):
    global a1
    print(f'\nTesting on {num_words} words')
    print(f'{num_words} words sorted')
    b6 = b10[:num_words]
    fonk1(b6)
    print('Number of comparisons:', a1)
    a1 = 0
    print(f'{num_words} words reversed')
    b7 = list(reversed(b6))
    fonk1(b7)
    print('Number of comparisons:', a1)
    a1 = 0
    print(f'{num_words} words random')
    b8 = random.randint(0, len(b10) - num_words)
    b9 = b10[b8:b8 + num_words]
    random.shuffle(b9)
    fonk1(b9)
    print('Number of comparisons:', a1)
def fonk4():
    with open('words.txt') as file:
        b10 = [line.strip() for line in file]
    print(f'Total words: {len(b10)}')
    b11 = [10, 30, 100, 300, 1000, 3000, 10000, len(b10)]
    for num_words in b11:
        fonk3(b10, num_words)
if b12 = = "__main__":
    fonk4()