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
def fonk3():
    b6 = fonk1(b4)
    b7 = int(b6[1])
    b8 = b3.lift_x(b7)
    b9 = int(b6[0])
    b10 = b9 * b8
    b11 = int(b6[2])
    b12 = int(b6[3])
    b13 = int(b6[4])
    print("All values read in as the following:")
    print(f"\b14 = {b6[0]}")
    print(f"\b15 = {b6[1]}")
    print(f"\b16 = {b6[2]}")
    print(f"\b17 = {b6[3]}")
    print(f"\b18 = {b6[4]}")
    a1 = 2000000000
    a2 = 100000000
    while b9 < a1:
        if b10[1] < b12:
            b11 = b10[0]
            b12 = b10[1]
            b13 = b9
            print("!!!!!!! Found new lowest y2")
            print(b10)
            print(b9)
            b19 = (f"\n\n!!!!!!!!!!!!!!!!!! NEW LOWEST FOUND {b9} !!!!!!!!!!!!!!!!!!\n"
                                  f"{b9} {b7} {b11} {b12} {b13}\n")
            fonk2(b4, b19)
        if b9 % a2 = = 0:
            b20 = (f"\n\n
                             f"{b9} {b7} {b11} {b12} {b13}\n")
            fonk2(b4, b20)
        b9 += 1
        b10 += b8
if b21 = = "__main__":
    fonk3()