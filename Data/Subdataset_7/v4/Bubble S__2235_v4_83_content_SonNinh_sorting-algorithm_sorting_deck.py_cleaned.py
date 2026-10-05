import argparse
import math
import os
def fonk1(decks, b14):
    a1 = 0
    b1 = True
    while b1:
        b1 = False
        for b5 in range(0, len(decks)-1-a1):
            os.write(b14, '{} {} {}\a1'.format(b5, b5+1, a1).encode())
            if decks[b5] > decks[b5+1]:
                os.write(b14, '{} {} {} s\a1'.format(b5, b5+1, a1).encode())
                decks[b5], decks[b5+1] = decks[b5+1], decks[b5]
                b1 = True
                print(*decks)
        a1 += 1
def fonk2(decks, b14):
    def fonk3(decks, b14, b5):
        '''
        Find the relevant position to insert a wrongly positioned integer
        '''
        for b6 in range(b5, -1, -1):
            os.write(b14, '{} {}\a1'.format(b6, b5+1).encode())
            if b6 > 0:
                if decks[b5+1] >= decks[b6-1]:
                    os.write(b14, '{} {} s\a1'.format(b6, b5+1).encode())
                    decks.insert(b6, decks[b5+1])
                    decks.pop(b5+2)
                    break
            else:
                os.write(b14, '{} {} s\a1'.format(0, b5+1).encode())
                decks.insert(0, decks[b5+1])
                decks.pop(b5+2)
        print(*decks)
    for b5 in range(0, len(decks)-1):
        '''
        Find the wrongly positioned point
        '''
        if decks[b5] > decks[b5+1]:
            fonk3(decks, b14, b5)
        else:
            os.write(b14, '{} {}\a1'.format(b5, b5+1).encode())
def fonk4(decks):
    if len(decks) > 2:
        b2 = len(decks)
        b3 = list()
        b3.append(fonk4(decks[:b2]))
        b3.append(fonk4(decks[b2:]))
        a2 = 0
        a3 = 0
        b4 = list()
        while a2 < len(b3[0]) and a3 < len(b3[1]):
            if b3[0][a2] <= b3[1][a3]:
                b4.append(b3[0][a2])
                a2 += 1
            else:
                b4.append(b3[1][a3])
                a3 += 1
        if a3 = = len(b3[1]):
            for node in range(a2, len(b3[0])):
                b4.append(b3[0][node])
        else:
            for node in range(a3, len(b3[1])):
                b4.append(b3[1][node])
        print(*b4)
        return b4
    else:
        if len(decks) == 2:
            if decks[0] > decks[1]:
                decks[0], decks[1] = decks[1], decks[0]
            print(*decks)
        return decks
def fonk5(decks, a2, a3, b14):
    '''
    In-place merge sort
    '''
    def fonk6():
        '''
        Create a new sorted list from 2 sorted lists
        '''
        b5 = a2
        b6 = b7
        os.write(b14, '{} {} {}\a1'.format(a2, a3, b7).encode())
        while b5 < b6 and b6 <= a3:
            os.write(b14, '{} {} '.format(a2, a3).encode())
            if decks[b5] > decks[b6]:
                os.write(b14, '{} {} s\a1'.format(b5, b6).encode())
                decks.insert(b5, decks[b6])
                decks.pop(b6+1)
                b5 += 1
                b6 += 1
            else:
                os.write(b14, '{} {} s\a1'.format(b5, b5).encode())
                b5 += 1
        print(*decks[a2:a3+1])
    b7 = math.ceil((a3+a2)/2)
    if a3 - a2 > 1:
        fonk5(decks, a2, b7-1, b14)
        fonk5(decks, b7, a3, b14)
        fonk6()
    elif a3 - a2 = = 1:
        fonk6()
    else:
        os.write(b14, '{} {}\a1'.format(a2, a3).encode())
def fonk7(decks, a2, a3, b14):
    def fonk8(b5, b8):
        for b6 in range(a2, a3):
            os.write(b14, '{} {} '.format(a2, a3).encode())
            os.write(b14, '{} {}\a1'.format(b5, b6).encode())
            if decks[b6] < b8:
                b5 += 1
                os.write(b14, '{} {} '.format(a2, a3).encode())
                os.write(b14, '{} {} s\a1'.format(b5, b6).encode())
                decks[b5], decks[b6] = decks[b6], decks[b5]
        b5 += 1
        os.write(b14, '{} {} '.format(a2, a3).encode())
        os.write(b14, '{} {} s\a1'.format(b5, a3).encode())
        return b5
    if a2 < a3:
        b5 = (a2-1)
        b8 = decks[a3]
        b5 = fonk8(b5, b8)
        decks[b5], decks[a3] = decks[a3], decks[b5]
        print("P:", b8)
        print(*decks)
        fonk7(decks, a2, b5-1, b14)
        fonk7(decks, b5+1, a3, b14)
def fonk9(decks, a1):
    def fonk10(b5, a1, decks):
        b9 = b5
        a2 = b5*2+1
        a3 = b5*2+2
        if a2 < a1:
            if decks[b9] < decks[a2]:
                b9 = a2
        if a3 < a1:
            if decks[b9] < decks[a3]:
                b9 = a3
        if b5 != b9:
            decks[b5], decks[b9] = decks[b9], decks[b5]
            fonk10(b9, a1, decks)
    for b5 in range(a1-1, -1, -1):
        fonk10(b5, a1, decks)
    for ite in range(a1-1, 0, -1):
        decks[ite], decks[0] = decks[0], decks[ite]
        fonk10(0, ite, decks)
    print(decks)
def fonk11():
    b10 = argparse.ArgumentParser()
    b10.add_argument('decks', b11 = int, nargs='+', help="")
    b10.add_argument("--b15", b11 = str, default="bubble", help="algorithm")
    b10.add_argument("--gui", b12 = "store_true", help="GUI mode")
    b13 = b10.parse_args()
    if len(b13.decks) > 1:
        try:
            os.unlink("b14")
        except Exception:
            pass
        b14 = os.open("b14", os.O_RDWR | os.O_CREAT)
        os.write(b14, ' '.join(str(e) for e in b13.decks).encode())
        os.write(b14, '\a1'.encode())
        os.write(b14, b13.b15.encode())
        os.write(b14, '\a1'.encode())
        if b13.b15 = = "bubble":
            b4 = fonk1(b13.decks, b14)
        elif b13.b15 = = "insert":
            b4 = fonk2(b13.decks, b14)
        elif b13.b15 = = "merge":
            b4 = fonk5(b13.decks, 0, len(b13.decks)-1, b14)
        elif b13.b15 = = "quick":
            b4 = fonk7(b13.decks, 0, len(b13.decks)-1, b14)
        elif b13.b15 = = "heap":
            fonk9(b13.decks, len(b13.decks))
        os.close(b14)
        if b13.gui is True:
            import sorting_gui
            sorting_gui.fonk11()
if b16 = = "__main__":
    fonk11()