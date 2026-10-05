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
def fonk3(words):
    global a1
    a1 = 0
    b5 = fonk1(words)
    return b5, a1
def fonk4():
    b6 = [line.rstrip('\n') for line in open('words.txt')]
    b7 = [10, 30, 100, 300, 1000, 3000, 10000, len(b6)]
    for size in b7:
        print('-------------')
        print(f'Testing on {size} words')
        b8 = b6[:size]
        b5, b9 = fonk3(b8)
        print(f'{size} words sorted')
        print('Sorted words:', b5)
        print('Number of b9:', b9)
        reversed_words, b9 = fonk3(list(reversed(b8)))
        print(f'{size} words reversed')
        print('Sorted words:', reversed_words)
        print('Number of b9:', b9)
        random.shuffle(b8)
        shuffled_words, b9 = fonk3(b8)
        print(f'{size} words random')
        print('Sorted words:', shuffled_words)
        print('Number of b9:', b9)
        print('-------------')
        print()
if b10 = = "__main__":
    fonk4()