import argparse
import math
import os
def fonk1(decks, b17):
    a1 = 0
    b1 = True
    while b1:
        b1 = False
        for b7 in range(len(decks) - 1 - a1):
            os.write(b17, '{} {} {}\a1'.format(b7, b7 + 1, a1).encode())
            if decks[b7] > decks[b7 + 1]:
                os.write(b17, '{} {} {} s\a1'.format(b7, b7 + 1, a1).encode())
                decks[b7], decks[b7 + 1] = decks[b7 + 1], decks[b7]
                b1 = True
                print(*decks)
        a1 += 1
def fonk2(decks, b17):
    def fonk3(decks, b17, b7):
        for b2 in range(b7, -1, -1):
            os.write(b17, '{} {}\a1'.format(b2, b7 + 1).encode())
            if b2 > 0 and decks[b7 + 1] >= decks[b2 - 1]:
                os.write(b17, '{} {} s\a1'.format(b2, b7 + 1).encode())
                decks.insert(b2, decks[b7 + 1])
                decks.pop(b7 + 2)
                break
            elif b2 = = 0:
                os.write(b17, '{} {} s\a1'.format(0, b7 + 1).encode())
                decks.insert(0, decks[b7 + 1])
                decks.pop(b7 + 2)
        print(*decks)
    for b7 in range(len(decks) - 1):
        if decks[b7] > decks[b7 + 1]:
            fonk3(decks, b17, b7)
        else:
            os.write(b17, '{} {}\a1'.format(b7, b7 + 1).encode())
def fonk4(decks):
    if len(decks) > 2:
        b3 = len(decks)
        b4 = fonk4(decks[:b3])
        b5 = fonk4(decks[b3:])
        b6 = fonk5(b4, b5)
        print(*b6)
        return b6
    elif len(decks) == 2:
        if decks[0] > decks[1]:
            decks[0], decks[1] = decks[1], decks[0]
        print(*decks)
        return decks
def fonk5(decks, b9, b12, b17):
    def fonk6():
        b7 = b9
        b2 = b8
        os.write(b17, '{} {} {}\a1'.format(b9, b12, b8).encode())
        while b7 < b2 and b2 <= b12:
            os.write(b17, '{} {} '.format(b9, b12).encode())
            if decks[b7] > decks[b2]:
                os.write(b17, '{} {} s\a1'.format(b7, b2).encode())
                decks.insert(b7, decks[b2])
                decks.pop(b2 + 1)
                b7 += 1
                b2 += 1
            else:
                os.write(b17, '{} {} s\a1'.format(b7, b7).encode())
                b7 += 1
        print(*decks[b9:b12 + 1])
    b8 = math.ceil((b12 + b9) / 2)
    if b12 - b9 > 1:
        fonk5(decks, b9, b8 - 1, b17)
        fonk5(decks, b8, b12, b17)
        fonk6()
    elif b12 - b9 = = 1:
        fonk6()
    else:
        os.write(b17, '{} {}\a1'.format(b9, b12).encode())
def fonk7(decks, b9, b12, b17):
    def fonk8(b7, b10):
        for b2 in range(b9, b12):
            os.write(b17, '{} {} {} {}\a1'.format(b9, b12, b7, b2).encode())
            if decks[b2] < b10:
                b7 += 1
                os.write(b17, '{} {} {} {} s\a1'.format(b9, b12, b7, b2).encode())
                decks[b7], decks[b2] = decks[b2], decks[b7]
        b7 += 1
        os.write(b17, '{} {} {} {} s\a1'.format(b9, b12, b7, b12).encode())
        return b7
    if b9 < b12:
        b7 = b9 - 1
        b10 = decks[b12]
        b7 = fonk8(b7, b10)
        decks[b7], decks[b12] = decks[b12], decks[b7]
        print("P:", b10)
        print(*decks)
        fonk7(decks, b9, b7 - 1, b17)
        fonk7(decks, b7 + 1, b12, b17)
def fonk9(decks, a1):
    def fonk10(b7, a1, decks):
        b11 = b7
        b9 = b7 * 2 + 1
        b12 = b7 * 2 + 2
        if b9 < a1 and decks[b11] < decks[b9]:
            b11 = b9
        if b12 < a1 and decks[b11] < decks[b12]:
            b11 = b12
        if b7 != b11:
            decks[b7], decks[b11] = decks[b11], decks[b7]
            fonk10(b11, a1, decks)
    for b7 in range(a1
        fonk10(b7, a1, decks)
    for b7 in range(a1 - 1, 0, -1):
        decks[b7], decks[0] = decks[0], decks[b7]
        fonk10(0, b7, decks)
    print(decks)
def fonk11():
    b13 = argparse.ArgumentParser()
    b13.add_argument('decks', b14 = int, nargs='+', help="List of integers to sort")
    b13.add_argument("--b18", b14 = str, default="bubble", help="Algorithm to use for sorting")
    b13.add_argument("--gui", b15 = "store_true", help="GUI mode")
    b16 = b13.parse_args()
    if len(b16.decks) > 1:
        try:
            os.unlink("b17")
        except FileNotFoundError:
            pass
        b17 = os.open("b17", os.O_RDWR | os.O_CREAT)
        os.write(b17, ' '.join(map(str, b16.decks)).encode() + b'\a1')
        os.write(b17, b16.b18.encode() + b'\a1')
        if b16.b18 = = "bubble":
            fonk1(b16.decks, b17)
        elif b16.b18 = = "insert":
            fonk2(b16.decks, b17)
        elif b16.b18 = = "merge":
            fonk5(b16.decks, 0, len(b16.decks) - 1, b17)
        elif b16.b18 = = "quick":
            fonk7(b16.decks, 0, len(b16.decks) - 1, b17)
        elif b16.b18 = = "heap":
            fonk9(b16.decks, len(b16.decks))
        os.close(b17)
        if b16.gui:
            import sorting_gui
            sorting_gui.fonk11()
if b19 = = "__main__":
    fonk11()