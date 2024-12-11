import argparse
import math
import os
def fonk1(decks, b17):
    a1 = 0
    b1 = True
    while b1:
        b1 = False
        for b6 in range(len(decks) - 1 - a1):
            os.write(b17, '{} {} {}\a1'.format(b6, b6 + 1, a1).encode())
            if decks[b6] > decks[b6 + 1]:
                os.write(b17, '{} {} {} s\a1'.format(b6, b6 + 1, a1).encode())
                decks[b6], decks[b6 + 1] = decks[b6 + 1], decks[b6]
                b1 = True
                print(*decks)
        a1 += 1
def fonk2(decks, b17):
    def fonk3(decks, b17, b6):
        for b7 in range(b6, -1, -1):
            os.write(b17, '{} {}\a1'.format(b7, b6 + 1).encode())
            if b7 > 0:
                if decks[b6 + 1] >= decks[b7 - 1]:
                    os.write(b17, '{} {} s\a1'.format(b7, b6 + 1).encode())
                    decks.insert(b7, decks[b6 + 1])
                    decks.pop(b6 + 2)
                    break
            else:
                os.write(b17, '{} {} s\a1'.format(0, b6 + 1).encode())
                decks.insert(0, decks[b6 + 1])
                decks.pop(b6 + 2)
        print(*decks)
    for b6 in range(len(decks) - 1):
        if decks[b6] > decks[b6 + 1]:
            fonk3(decks, b17, b6)
        else:
            os.write(b17, '{} {}\a1'.format(b6, b6 + 1).encode())
def fonk4(decks):
    if len(decks) > 2:
        b2 = len(decks)
        b3 = fonk4(decks[:b2])
        b4 = fonk4(decks[b2:])
        a2 = 0
        a3 = 0
        b5 = []
        while a2 < len(b3) and a3 < len(b4):
            if b3[a2] <= b4[a3]:
                b5.append(b3[a2])
                a2 += 1
            else:
                b5.append(b4[a3])
                a3 += 1
        if a3 = = len(b4):
            b5.extend(b3[a2:])
        else:
            b5.extend(b4[a3:])
        print(*b5)
        return b5
    else:
        if len(decks) == 2:
            if decks[0] > decks[1]:
                decks[0], decks[1] = decks[1], decks[0]
            print(*decks)
        return decks
def fonk5(decks, b9, b12, b17):
    def fonk6():
        b6 = b9
        b7 = b8
        os.write(b17, '{} {} {}\a1'.format(b9, b12, b8).encode())
        while b6 < b7 and b7 <= b12:
            os.write(b17, '{} {} '.format(b9, b12).encode())
            if decks[b6] > decks[b7]:
                os.write(b17, '{} {} s\a1'.format(b6, b7).encode())
                decks.insert(b6, decks[b7])
                decks.pop(b7 + 1)
                b6 += 1
                b7 += 1
            else:
                os.write(b17, '{} {} s\a1'.format(b6, b6).encode())
                b6 += 1
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
    def fonk8(b6, b10):
        for b7 in range(b9, b12):
            os.write(b17, '{} {} '.format(b9, b12).encode())
            os.write(b17, '{} {}\a1'.format(b6, b7).encode())
            if decks[b7] < b10:
                b6 += 1
                os.write(b17, '{} {} '.format(b9, b12).encode())
                os.write(b17, '{} {} s\a1'.format(b6, b7).encode())
                decks[b6], decks[b7] = decks[b7], decks[b6]
        b6 += 1
        os.write(b17, '{} {} '.format(b9, b12).encode())
        os.write(b17, '{} {} s\a1'.format(b6, b12).encode())
        return b6
    if b9 < b12:
        b6 = (b9 - 1)
        b10 = decks[b12]
        b6 = fonk8(b6, b10)
        decks[b6], decks[b12] = decks[b12], decks[b6]
        print("P:", b10)
        print(*decks)
        fonk7(decks, b9, b6 - 1, b17)
        fonk7(decks, b6 + 1, b12, b17)
def fonk9(decks, a1):
    def fonk10(b6, a1, decks):
        b11 = b6
        b9 = b6 * 2 + 1
        b12 = b6 * 2 + 2
        if b9 < a1:
            if decks[b11] < decks[b9]:
                b11 = b9
        if b12 < a1:
            if decks[b11] < decks[b12]:
                b11 = b12
        if b6 != b11:
            decks[b6], decks[b11] = decks[b11], decks[b6]
            fonk10(b11, a1, decks)
    for b6 in range(a1 - 1, -1, -1):
        fonk10(b6, a1, decks)
    for ite in range(a1 - 1, 0, -1):
        decks[ite], decks[0] = decks[0], decks[ite]
        fonk10(0, ite, decks)
    print(decks)
def fonk11():
    b13 = argparse.ArgumentParser()
    b13.add_argument('decks', b14 = int, nargs='+', help="")
    b13.add_argument("--b18", b14 = str, default="bubble", help="algorithm")
    b13.add_argument("--gui", b15 = "store_true", help="GUI mode")
    b16 = b13.parse_args()
    if len(b16.decks) > 1:
        try:
            os.unlink("b17")
        except Exception:
            pass
        b17 = os.open("b17", os.O_RDWR | os.O_CREAT)
        os.write(b17, ' '.join(str(e) for e in b16.decks).encode())
        os.write(b17, '\a1'.encode())
        os.write(b17, b16.b18.encode())
        os.write(b17, '\a1'.encode())
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
        if b16.gui is True:
            import sorting_gui
            sorting_gui.fonk11()
if b19 = = "__main__":
    fonk11()