from sage.all import *
import os
b1 = RealNumber('29579385439865947694694684968492467204765870577.')
b2 = GF(b1)
b3 = EllipticCurve(b2, [32934893483948394, 593439483948394349])
b4 = 'data.txt'
def fonk1(filepath):
    with open(filepath, 'r') as file:
        b5 = file.read().splitlines()
    return b5[-1].split(' ')
def fonk2(filepath, content):
    with open(filepath, "a") as file:
        file.write(content)
def fonk3(values):
    print("All values read in as the following:")
    print(f"\b6 = {values[0]}")
    print(f"\b7 = {values[1]}")
    print(f"\b8 = {values[2]}")
    print(f"\b9 = {values[3]}")
    print(f"\b10 = {values[4]}")
def fonk4():
    b11 = fonk1(b4)
    b12 = int(b11[1])
    b13 = b3.lift_x(b12)
    b14 = int(b11[0])
    b15 = b14 * b13
    b16 = int(b11[2])
    b17 = int(b11[3])
    b18 = int(b11[4])
    fonk3(b11)
    a1 = 2000000000
    a2 = 100000000
    while b14 < a1:
        if b15[1] < b17:
            b16 = b15[0]
            b17 = b15[1]
            b18 = b14
            print("!!!!!!! Found new lowest y2")
            print(b15)
            print(b14)
            b19 = (f"\n\n!!!!!!!!!!!!!!!!!! NEW LOWEST FOUND {b14} !!!!!!!!!!!!!!!!!!\n"
                                  f"{b14} {b12} {b16} {b17} {b18}\n")
            fonk2(b4, b19)
        if b14 % a2 = = 0:
            b20 = (f"\n\n
                             f"{b14} {b12} {b16} {b17} {b18}\n")
            fonk2(b4, b20)
        b14 += 1
        b15 += b13
if b21 = = "__main__":
    fonk4()