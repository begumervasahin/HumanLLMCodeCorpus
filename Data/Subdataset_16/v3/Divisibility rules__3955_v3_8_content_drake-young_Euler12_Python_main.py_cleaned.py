from timeit import default_timer
def fonk1(a3):
    a1 = 2
    b1 = []
    while a1 * a1 <= a3:
        if a3 % a1:
            a1 += 1
        else:
            a3
            b1.append(a1)
    if a3 > 1:
        b1.append(a3)
    return b1
def fonk2(b3):
    a2 = 1
    for factor in set(b3):
        a2 *= b3.count(factor) + 1
    return a2
def fonk3(a4):
    a3 = 1
    while True:
        b2 = a3 * (a3 + 1)
        b3 = fonk1(b2)
        if fonk2(b3) > a4:
            return b2
        a3 += 1
def fonk4():
    print("Project Euler Problem 12 -- Highly Divisible Triangular Number")
    b4 = default_timer()
    a4 = 500
    b5 = fonk3(a4)
    b6 = default_timer()
    b7 = (b6 - b4) * 1000
    print(f"   Triangle Number with over {a4} b1: {b5}")
    print(f"   Computation Time: {b7:.3f} ms")
if b8 = = '__main__':
    fonk4()