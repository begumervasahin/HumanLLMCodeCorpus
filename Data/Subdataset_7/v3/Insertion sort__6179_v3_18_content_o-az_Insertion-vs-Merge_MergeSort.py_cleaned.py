import random
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = len(arr)
    b2 = fonk1(arr[:b1])
    b3 = fonk1(arr[b1:])
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
    b4.extend(b2[i:])
    b4.extend(b3[b5:])
    return b4
def fonk3(arr):
    global a1
    a1 = 0
    def fonk4(arr):
        if len(arr) <= 1:
            return arr
        b1 = len(arr)
        b2 = fonk4(arr[:b1])
        b3 = fonk4(arr[b1:])
        return fonk5(b2, b3)
    def fonk5(b2, b3):
        nonlocal a1
        b4 = []
        i, b5 = 0, 0
        while i < len(b2) and b5 < len(b3):
            a1 += 1
            if b2[i] < b3[b5]:
                b4.append(b2[i])
                i += 1
            else:
                b4.append(b3[b5])
                b5 += 1
        b4.extend(b2[i:])
        b4.extend(b3[b5:])
        return b4
    fonk4(arr)
    return a1
def fonk6():
    b6 = [line.rstrip('\n') for line in open('words.txt')]
    b7 = [10, 30, 100, 300, 1000, 3000, 10000, len(b6)]
    for size in b7:
        print('-------------')
        print(f'Testing on {size} words')
        b8 = b6[:size]
        b9 = fonk1(b8)
        a1 = fonk3(b8)
        print(f'{size} words sorted')
        print('Sorted words:', b9)
        print('Number of a1:', a1)
        b10 = list(reversed(b8))
        a1 = fonk3(b10)
        print(f'{size} words reversed')
        print('Sorted words:', b10)
        print('Number of a1:', a1)
        random.shuffle(b8)
        b9 = fonk1(b8)
        a1 = fonk3(b8)
        print(f'{size} words random')
        print('Sorted words:', b9)
        print('Number of a1:', a1)
        print('-------------')
        print()
if b11 = = "__main__":
    fonk6()