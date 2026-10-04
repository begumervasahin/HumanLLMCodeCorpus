import argparse
import math
import os
def fonk1(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def fonk2(arr, b17):
    a1 = 0
    b1 = True
    while b1:
        b1 = False
        for b9 in range(len(arr) - 1 - a1):
            os.write(b17, f'{b9} {b9 + 1} {a1}\a1'.encode())
            if arr[b9] > arr[b9 + 1]:
                os.write(b17, f'{b9} {b9 + 1} {a1} s\a1'.encode())
                fonk1(arr, b9, b9 + 1)
                b1 = True
                print(*arr)
        a1 += 1
def fonk3(arr, b17):
    def fonk4(arr, b17, b9):
        for b2 in range(b9, -1, -1):
            os.write(b17, f'{b2} {b9 + 1}\a1'.encode())
            if b2 > 0 and arr[b9 + 1] >= arr[b2 - 1]:
                os.write(b17, f'{b2} {b9 + 1} s\a1'.encode())
                arr.insert(b2, arr.pop(b9 + 1))
                break
            elif b2 = = 0:
                os.write(b17, f'{0} {b9 + 1} s\a1'.encode())
                arr.insert(0, arr.pop(b9 + 1))
        print(*arr)
    for b9 in range(len(arr) - 1):
        if arr[b9] > arr[b9 + 1]:
            fonk4(arr, b17, b9)
        else:
            os.write(b17, f'{b9} {b9 + 1}\a1'.encode())
def fonk5(arr):
    if len(arr) > 2:
        b3 = len(arr)
        b4 = fonk5(arr[:b3])
        b5 = fonk5(arr[b3:])
        b6 = fonk6(b4, b5)
        print(*b6)
        return b6
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            fonk1(arr, 0, 1)
        print(*arr)
        return arr
def fonk6(arr, b8, b12, b17):
    def fonk7():
        b9, b2 = b8, b7
        os.write(b17, f'{b8} {b12} {b7}\a1'.encode())
        while b9 < b2 and b2 <= b12:
            os.write(b17, f'{b8} {b12} '.encode())
            if arr[b9] > arr[b2]:
                os.write(b17, f'{b9} {b2} s\a1'.encode())
                arr.insert(b9, arr.pop(b2))
                b9 += 1
                b2 += 1
            else:
                os.write(b17, f'{b9} {b9} s\a1'.encode())
                b9 += 1
        print(*arr[b8:b12 + 1])
    b7 = math.ceil((b12 + b8) / 2)
    if b12 - b8 > 1:
        fonk6(arr, b8, b7 - 1, b17)
        fonk6(arr, b7, b12, b17)
        fonk7()
    elif b12 - b8 = = 1:
        fonk7()
    else:
        os.write(b17, f'{b8} {b12}\a1'.encode())
def fonk8(arr, b8, b12, b17):
    def fonk9(b9, b10):
        for b2 in range(b8, b12):
            os.write(b17, f'{b8} {b12} {b9} {b2}\a1'.encode())
            if arr[b2] < b10:
                b9 += 1
                os.write(b17, f'{b8} {b12} {b9} {b2} s\a1'.encode())
                fonk1(arr, b9, b2)
        b9 += 1
        os.write(b17, f'{b8} {b12} {b9} {b12} s\a1'.encode())
        return b9
    if b8 < b12:
        b9 = b8 - 1
        b10 = arr[b12]
        b9 = fonk9(b9, b10)
        fonk1(arr, b9, b12)
        print("P:", b10)
        print(*arr)
        fonk8(arr, b8, b9 - 1, b17)
        fonk8(arr, b9 + 1, b12, b17)
def fonk10(arr):
    def fonk11(b9, a1):
        b11 = b9
        b8, b12 = 2 * b9 + 1, 2 * b9 + 2
        if b8 < a1 and arr[b11] < arr[b8]:
            b11 = b8
        if b12 < a1 and arr[b11] < arr[b12]:
            b11 = b12
        if b9 != b11:
            fonk1(arr, b9, b11)
            fonk11(b11, a1)
    a1 = len(arr)
    for b9 in range(a1
        fonk11(b9, a1)
    for b9 in range(a1 - 1, 0, -1):
        fonk1(arr, b9, 0)
        fonk11(0, b9)
    print(*arr)
def fonk12():
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
            fonk2(b16.decks, b17)
        elif b16.b18 = = "insert":
            fonk3(b16.decks, b17)
        elif b16.b18 = = "merge":
            fonk6(b16.decks, 0, len(b16.decks) - 1, b17)
        elif b16.b18 = = "quick":
            fonk8(b16.decks, 0, len(b16.decks) - 1, b17)
        elif b16.b18 = = "heap":
            fonk10(b16.decks)
        os.close(b17)
        if b16.gui:
            import sorting_gui
            sorting_gui.fonk12()
if b19 = = "__main__":
    fonk12()