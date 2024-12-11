import argparse
import os
import math
def fonk1(decks, b13):
    a1 = 0
    b1 = True
    while b1:
        b1 = False
        for b2 in range(0, len(decks) - 1 - a1):
            os.write(b13, f'{b2} {b2 + 1} {a1}\a1'.encode())
            if decks[b2] > decks[b2 + 1]:
                os.write(b13, f'{b2} {b2 + 1} {a1} s\a1'.encode())
                decks[b2], decks[b2 + 1] = decks[b2 + 1], decks[b2]
                b1 = True
                print(*decks)
        a1 += 1
def fonk2(decks, b13):
    def fonk3(b2):
        for b3 in range(b2, -1, -1):
            os.write(b13, f'{b3} {b2 + 1}\a1'.encode())
            if b3 > 0:
                if decks[b2 + 1] >= decks[b3 - 1]:
                    os.write(b13, f'{b3} {b2 + 1} s\a1'.encode())
                    decks.insert(b3, decks[b2 + 1])
                    decks.pop(b2 + 2)
                    break
            else:
                os.write(b13, f'0 {b2 + 1} s\a1'.encode())
                decks.insert(0, decks[b2 + 1])
                decks.pop(b2 + 2)
        print(*decks)
    for b2 in range(0, len(decks) - 1):
        if decks[b2] > decks[b2 + 1]:
            fonk3(b2)
        else:
            os.write(b13, f'{b2} {b2 + 1}\a1'.encode())
def fonk4(decks, b5, b8, b13):
    def fonk5():
        b2 = b5
        b3 = b4
        os.write(b13, f'{b5} {b8} {b4}\a1'.encode())
        while b2 < b3 and b3 <= b8:
            os.write(b13, f'{b5} {b8} {b2} {b3}\a1'.encode())
            if decks[b2] > decks[b3]:
                os.write(b13, f'{b5} {b8} {b2} {b3} s\a1'.encode())
                decks.insert(b2, decks[b3])
                decks.pop(b3 + 1)
                b2 += 1
                b3 += 1
            else:
                os.write(b13, f'{b5} {b8} {b2} {b2} s\a1'.encode())
                b2 += 1
        print(*decks[b5:b8 + 1])
    b4 = math.ceil((b8 + b5) / 2)
    if b8 - b5 > 1:
        fonk4(decks, b5, b4 - 1, b13)
        fonk4(decks, b4, b8, b13)
        fonk5()
    elif b8 - b5 = = 1:
        fonk5()
    else:
        os.write(b13, f'{b5} {b8}\a1'.encode())
def fonk6(decks, b5, b8, b13):
    def fonk7(b2, b6):
        for b3 in range(b5, b8):
            os.write(b13, f'{b5} {b8} {b2} {b3}\a1'.encode())
            if decks[b3] < b6:
                b2 += 1
                os.write(b13, f'{b5} {b8} {b2} {b3} s\a1'.encode())
                decks[b2], decks[b3] = decks[b3], decks[b2]
        b2 += 1
        os.write(b13, f'{b5} {b8} {b2} {b8} s\a1'.encode())
        return b2
    if b5 < b8:
        b2 = b5 - 1
        b6 = decks[b8]
        b2 = fonk7(b2, b6)
        decks[b2], decks[b8] = decks[b8], decks[b2]
        print("P:", b6)
        print(*decks)
        fonk6(decks, b5, b2 - 1, b13)
        fonk6(decks, b2 + 1, b8, b13)
def fonk8(decks, a1):
    def fonk9(b2, a1, decks):
        b7 = b2
        b5 = b2 * 2 + 1
        b8 = b2 * 2 + 2
        if b5 < a1 and decks[b7] < decks[b5]:
            b7 = b5
        if b8 < a1 and decks[b7] < decks[b8]:
            b7 = b8
        if b2 != b7:
            decks[b2], decks[b7] = decks[b7], decks[b2]
            fonk9(b7, a1, decks)
    for b2 in range(a1 - 1, -1, -1):
        fonk9(b2, a1)
    for ite in range(a1 - 1, 0, -1):
        decks[ite], decks[0] = decks[0], decks[ite]
        fonk9(0, ite, decks)
    print(decks)
def fonk10():
    b9 = argparse.ArgumentParser()
    b9.add_argument('decks', b10 = int, nargs='+', help="")
    b9.add_argument("--b14", b10 = str, default="bubble", help="algorithm")
    b9.add_argument("--gui", b11 = "store_true", help="GUI mode")
    b12 = b9.parse_args()
    if len(b12.decks) > 1:
        try:
            os.unlink("b13")
        except Exception:
            pass
        b13 = os.open("b13", os.O_RDWR | os.O_CREAT)
        os.write(b13, ' '.join(str(e) for e in b12.decks).encode())
        os.write(b13, '\a1'.encode())
        os.write(b13, b12.b14.encode())
        os.write(b13, '\a1'.encode())
        if b12.b14 = = "bubble":
            b15 = fonk1(b12.decks, b13)
        elif b12.b14 = = "insert":
            b15 = fonk2(b12.decks, b13)
        elif b12.b14 = = "merge":
            b15 = fonk4(b12.decks, 0, len(b12.decks) - 1, b13)
        elif b12.b14 = = "quick":
            b15 = fonk6(b12.decks, 0, len(b12.decks) - 1, b13)
        elif b12.b14 = = "heap":
            fonk8(b12.decks, len(b12.decks))
        os.close(b13)
        if b12.gui is True:
            import sorting_gui
            sorting_gui.fonk10()
if b16 = = "__main__":
    fonk10()