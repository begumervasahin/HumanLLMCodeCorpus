import argparse
import os
def fonk1(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def fonk2(decks, b17):
    a1 = 0
    b1 = True
    while b1:
        b1 = False
        for i in range(len(decks) - 1 - a1):
            os.write(b17, f'{i} {i+1} {a1}\a1'.encode())
            if decks[i] > decks[i + 1]:
                os.write(b17, f'{i} {i+1} {a1} s\a1'.encode())
                fonk1(decks, i, i + 1)
                b1 = True
                print(*decks)
        a1 += 1
def fonk3(decks, b17):
    def fonk4(decks, b17, i):
        for b2 in range(i, -1, -1):
            os.write(b17, f'{b2} {i+1}\a1'.encode())
            if b2 > 0 and decks[i + 1] >= decks[b2 - 1]:
                os.write(b17, f'{b2} {i+1} s\a1'.encode())
                decks.insert(b2, decks.pop(i + 1))
                break
            elif b2 = = 0:
                os.write(b17, f'{0} {i+1} s\a1'.encode())
                decks.insert(0, decks.pop(i + 1))
        print(*decks)
    for i in range(len(decks) - 1):
        if decks[i] > decks[i + 1]:
            fonk4(decks, b17, i)
        else:
            os.write(b17, f'{i} {i+1}\a1'.encode())
def fonk5(decks):
    if len(decks) <= 1:
        return decks
    b3 = len(decks)
    b4 = fonk5(decks[:b3])
    b5 = fonk5(decks[b3:])
    return fonk6(b4, b5)
def fonk6(b8, b11):
    b6 = []
    while b8 and b11:
        if b8[0] < b11[0]:
            b6.append(b8.pop(0))
        else:
            b6.append(b11.pop(0))
    b6.extend(b8)
    b6.extend(b11)
    return b6
def fonk7(decks, b8, b11, b17):
    def fonk8():
        i, b2 = b8, b7
        os.write(b17, f'{b8} {b11} {b7}\a1'.encode())
        while i < b2 and b2 <= b11:
            if decks[i] > decks[b2]:
                os.write(b17, f'{i} {b2} s\a1'.encode())
                decks.insert(i, decks.pop(b2))
                i += 1
                b2 += 1
            else:
                os.write(b17, f'{i} {i} s\a1'.encode())
                i += 1
        print(*decks[b8:b11 + 1])
    if b11 - b8 > 1:
        b7 = (b11 + b8)
        fonk7(decks, b8, b7 - 1, b17)
        fonk7(decks, b7, b11, b17)
        fonk8()
    elif b11 - b8 = = 1:
        fonk8()
    else:
        os.write(b17, f'{b8} {b11}\a1'.encode())
def fonk9(decks, b8, b11, b17):
    def fonk10(i, pivot):
        for b2 in range(b8, b11):
            if decks[b2] < pivot:
                i += 1
                fonk1(decks, i, b2)
        return i
    if b8 < b11:
        b9 = fonk10(b8 - 1, decks[b11])
        fonk1(decks, b9 + 1, b11)
        fonk9(decks, b8, b9, b17)
        fonk9(decks, b9 + 2, b11, b17)
def fonk11(decks, a1):
    def fonk12(i, a1):
        b10 = i
        b8 = 2 * i + 1
        b11 = 2 * i + 2
        if b8 < a1 and decks[b8] > decks[b10]:
            b10 = b8
        if b11 < a1 and decks[b11] > decks[b10]:
            b10 = b11
        if b10 != i:
            fonk1(decks, i, b10)
            fonk12(b10, a1)
    for i in range(a1
        fonk12(i, a1)
    for i in range(a1 - 1, 0, -1):
        fonk1(decks, i, 0)
        fonk12(0, i)
    print(decks)
def fonk13():
    b12 = argparse.ArgumentParser()
    b12.add_argument('decks', b13 = int, nargs='+', help="List of integers to be sorted.")
    b12.add_argument("--b18", b13 = str, default="bubble", help="Sorting algorithm to use.")
    b12.add_argument("--gui", b14 = "store_true", help="Enable GUI mode.")
    b15 = b12.parse_args()
    if len(b15.decks) > 1:
        b16 = "b17"
        try:
            os.unlink(b16)
        except Exception:
            pass
        b17 = os.open(b16, os.O_RDWR | os.O_CREAT)
        os.write(b17, ' '.join(map(str, b15.decks)).encode() + b'\a1')
        os.write(b17, b15.b18.encode() + b'\a1')
        if b15.b18 = = "bubble":
            fonk2(b15.decks, b17)
        elif b15.b18 = = "insert":
            fonk3(b15.decks, b17)
        elif b15.b18 = = "merge":
            fonk7(b15.decks, 0, len(b15.decks) - 1, b17)
        elif b15.b18 = = "quick":
            fonk9(b15.decks, 0, len(b15.decks) - 1, b17)
        elif b15.b18 = = "heap":
            fonk11(b15.decks, len(b15.decks))
        os.close(b17)
        if b15.gui:
            import sorting_gui
            sorting_gui.fonk13()
if b19 = = "__main__":
    fonk13()