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
def fonk3(b9, num_words):
    global a1
    print(f'Testing on {num_words} words')
    print(f'{num_words} words sorted')
    b5 = b9[:num_words]
    fonk1(b5)
    print('Number of comparisons:', a1)
    print(f'{num_words} words reversed')
    a1 = 0
    b6 = list(reversed(b5))
    fonk1(b6)
    print('Number of comparisons:', a1)
    print(f'{num_words} words random')
    a1 = 0
    b7 = random.randint(0, len(b9) - num_words)
    b8 = b9[b7:b7 + num_words]
    random.shuffle(b8)
    fonk1(b8)
    print('Number of comparisons:', a1)
    print('-------------')
def fonk4():
    with open('words.txt') as file:
        b9 = [line.strip() for line in file]
    print(f'Total words: {len(b9)}')
    b10 = [10, 30, 100, 300, 1000, 3000, 10000, len(b9)]
    for num_words in b10:
        fonk3(b9, num_words)
if b11 = = "__main__":
    fonk4()