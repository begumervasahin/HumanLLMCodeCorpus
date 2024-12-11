from timeit import default_timer
def fonk1(b3):
    b1 = []
    a1 = 2
    while a1 * a1 <= b3:
        if b3 % a1 = = 0:
            b1.append(a1)
            b3
        else:
            a1 += 1
    if b3 > 1:
        b1.append(b3)
    return b1
def fonk2():
    print("Project Euler Problem 12 -- Highly Divisible Triangular Number")
    b2 = default_timer()
    a2 = 500
    b3 = 2 * a2
    while True:
        b4 = (b3 * (b3 + 1))
        b5 = fonk1(b4)
        a3 = 1
        for factor in set(b5):
            a3 *= (b5.count(factor) + 1)
        if a3 > a2:
            break
        b3 += 1
    b6 = default_timer()
    b7 = (b6 - b2) * 1000
    print("   Triangle Number x with over 500 b1:   %d" % b4)
    print("   Computation Time:                          %.3fms" % b7)
if b8 = = '__main__':
    fonk2()