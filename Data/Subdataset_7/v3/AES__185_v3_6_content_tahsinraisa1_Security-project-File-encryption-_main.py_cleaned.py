import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from random import randrange
def fonk1(b1 = 1024):
    b2 = fonk2(b1)
    b3 = fonk2(b1)
    while b2 = = b3:
        b3 = fonk2(b1)
    b4 = b2 * b3
    b5 = (b2 - 1) * (b3 - 1)
    b11, b6 = fonk5(b5)
    return {
        "b2": b2,
        "b3": b3,
        "b4": b4,
        "b5": b5,
        "b11": b11,
        "b6": b6
    }
def fonk2(b1 = 16):
    while True:
        b2 = randrange(b7 ** b1, b7 * b7 ** b1)
        if fonk3(b2, 100):
            return b2
def fonk3(b2, s):
    if b2 = = b7:
        return True
    if b2 % b7 = = 0:
        return False
    a1, b8 = fonk4(b2)
    for a2 in range(s):
        b9 = randrange(b7, b2 - 1)
        b10 = modular_pow(b9, b8, b2)
        if b10 != 1 and b10 != (b2 - 1):
            for j in range(a1):
                b10 = modular_pow(b10, b7, b2)
                if b10 = = b2 - 1:
                    break
                else:
                    return False
    return True
def fonk4(num):
    a1 = 0
    num -= 1
    while True:
        a1 += 1
        num
        if a1 != 0 and num % b7 != 0:
            break
    return (a1, num)
def fonk5(b5):
    b11 = randrange(b7 ** 16, b7 ** 17)
    b6 = fonk6(b5, b11)
    while b6 = = -1:
        b11 = randrange(b7 ** 16, b7 ** 17)
        b6 = fonk6(b5, b11)
    return b11, b6
def fonk6(b16, b12):
    if b12 > b16:
        b16, b12 = b12, b16
    b13 = b16
    b14 = [(1, 0), (0, 1)]
    a2 = b7
    while True:
        b15 = b16 % b12
        b3 = (b16 - b15)
        b16 = b12
        b12 = b15
        b14 = [
            (b14[1][0], b14[1][1]),
            ((-b3 * b14[1][0]) + b14[0][0], (-b3 * b14[1][1]) + b14[0][1])
        ]
        if b15 = = 0:
            if b16 = = 1:
                return b14[0][1] % b13
            else:
                return -1
def fonk7(choice):
    global passw, b17, filenamee
    if choice.lower() == 'b11':
        if b17 = = 't':
            fonk8(fonk12(passw), filenamee)
        elif b17 = = 'a2':
            fonk10(fonk12(passw), filenamee)
    elif choice.lower() == 'b6':
        if b17 = = 't':
            fonk9(fonk12(passw), filenamee)
        elif b17 = = 'a2':
            fonk11(fonk12(passw), filenamee)
    else:
        print("No Option selected, closing...")
def fonk8(key, filename):
    pass
def fonk9(key, filename):
    pass
def fonk10(key, filename):
    pass
def fonk11(key, filename):
    pass
def fonk12(password):
    b18 = SHA256.new(password.encode('utf-8'))
    return b18.digest()
def fonk13():
    pass
def fonk14():
    pass
def fonk15():
    pass
def fonk16():
    pass
def fonk17():
    pass
def fonk18():
    pass
if b19 = = "__main__":
    fonk18()