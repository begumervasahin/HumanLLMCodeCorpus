from sage.all import *
a1 = 29579385439865947694694684968492467204765870577
b1 = GF(a1)
b2 = EllipticCurve(GF(a1), [32934893483948394, 593439483948394349])
b3 = '/home/landondare/EllipticCurveProject/data.txt'
a2 = 2000000000
a3 = 100000000
with open(b3, 'r') as file:
    b4 = file.readlines()
b5 = b4[-1].split(' ')
b6 = int(b5[1])
b7 = b2.lift_x(b6)
b8 = int(b5[0])
b9 = b8 * b7
b10 = int(b5[2])
b11 = int(b5[3])
b12 = int(b5[4])
print("All values read in as the following:")
print(f"\b13 = {b5[0]}")
print(f"\b14 = {b5[1]}")
print(f"\b15 = {b5[2]}")
print(f"\b16 = {b5[3]}")
print(f"\b17 = {b5[4]}")
while b8 < a2:
    if b9[1] < b11:
        b10 = b9[0]
        b11 = b9[1]
        b12 = b8
        print("!!!!!!!found new y2")
        print(b9)
        print(b8)
        with open(b3, "a") as data_file:
            data_file.write("\n\n!!!!!!!!!!!!!!!!!! NEW LOWEST FOUND " + str(b8) + " !!!!!!!!!!!!!!!!!!\n")
            data_file.write(f"{b8} {b6} {b10} {b11} {b12}")
    if b8 % a3 = = 0:
        with open(b3, "a") as data_file:
            data_file.write(f"\n\n
            data_file.write(f"{b8} {b6} {b10} {b11} {b12}")
    b8 += 1
    b9 += b7