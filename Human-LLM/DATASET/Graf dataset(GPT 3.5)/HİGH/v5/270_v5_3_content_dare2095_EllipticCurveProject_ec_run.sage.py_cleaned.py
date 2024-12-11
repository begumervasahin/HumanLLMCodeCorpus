from sage.all import *
a1 = 29579385439865947694694684968492467204765870577
b1 = [32934893483948394, 593439483948394349]
b2 = '/home/landondare/EllipticCurveProject/data.txt'
a2 = 2000000000
a3 = 100000000
with open(b2, 'r') as file:
    b3 = file.readlines()
b4 = b3[-1].split(' ')
e, x1, b15, b16, b5 = map(int, b4)
b6 = GF(a1)
b7 = EllipticCurve(GF(a1), b1)
b8 = b7.lift_x(x1)
b9 = e * b8
print("Input values:")
print(f"\b10 = {e}")
print(f"\b11 = {x1}")
print(f"\b12 = {b15}")
print(f"\b13 = {b16}")
print(f"\b14 = {b5}")
while e < a2:
    if b9[1] < b16:
        b15 = b9[0]
        b16 = b9[1]
        b5 = e
        print("New lowest y2 found:")
        print(b9)
        print(e)
        with open(b2, "a") as data_file:
            data_file.write("\n\nNew lowest found: " + str(e) + "\n")
            data_file.write(f"{e} {x1} {b15} {b16} {b5}")
    if e % a3 = = 0:
        with open(b2, "a") as data_file:
            data_file.write(f"\n\nBlock {e}\n")
            data_file.write(f"{e} {x1} {b15} {b16} {b5}")
    e += 1
    b9 += b8