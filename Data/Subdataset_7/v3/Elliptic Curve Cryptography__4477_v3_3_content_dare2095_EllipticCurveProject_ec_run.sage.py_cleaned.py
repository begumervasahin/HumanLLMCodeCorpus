from sage.all import *
a1 = 29579385439865947694694684968492467204765870577
b1 = [32934893483948394, 593439483948394349]
b2 = '/home/landondare/EllipticCurveProject/data.txt'
a2 = 2000000000
a3 = 100000000
with open(b2, 'r') as file:
    b3 = file.readlines()
e, x1, b14, b15, b4 = map(int, b3[-1].split())
b5 = GF(a1)
b6 = EllipticCurve(GF(a1), b1)
b7 = b6.lift_x(x1)
b8 = e * b7
print("Input values:")
print(f"\b9 = {e}")
print(f"\b10 = {x1}")
print(f"\b11 = {b14}")
print(f"\b12 = {b15}")
print(f"\b13 = {b4}")
while e < a2:
    if b8[1] < b15:
        b14 = b8[0]
        b15 = b8[1]
        b4 = e
        print("New lowest y2 found:")
        print(b8)
        print(e)
        with open(b2, "a") as data_file:
            data_file.write("\n\nNew lowest found: " + str(e) + "\n")
            data_file.write(f"{e} {x1} {b14} {b15} {b4}")
    if e % a3 = = 0:
        with open(b2, "a") as data_file:
            data_file.write(f"\n\nBlock {e}\n")
            data_file.write(f"{e} {x1} {b14} {b15} {b4}")
    e += 1
    b8 += b7