from sage.all import *
import os
b1 = RealNumber('29579385439865947694694684968492467204765870577.')
b2 = GF(b1)
b3 = EllipticCurve(b2, [32934893483948394, 593439483948394349])
b4 = 'data.txt'
with open(b4, 'r') as file:
    b5 = file.read().splitlines()
b6 = b5[-1].split(' ')
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
        with open(b4, "a") as dataFile:
            dataFile.write(f"\n\n!!!!!!!!!!!!!!!!!! NEW LOWEST FOUND {b9} !!!!!!!!!!!!!!!!!!\n")
            dataFile.write(f"{b9} {b7} {b11} {b12} {b13}\n")
    if b9 % a2 = = 0:
        with open(b4, "a") as dataFile:
            dataFile.write(f"\n\n
            dataFile.write(f"{b9} {b7} {b11} {b12} {b13}\n")
    b9 += 1
    b10 = b10 + b8