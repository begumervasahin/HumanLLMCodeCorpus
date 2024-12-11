from timeit import default_timer
def fonk1(b3):
    b1 = []
    a1 = 2
    while a1 * a1 <= b3:
        if b3 % a1 != 0:
            a1 += 1
        else:
            b3
            b1.append(a1)
    if b3 > 1:
        b1.append(b3)
    return b1
def fonk2():
    print("Project Euler Problem 12 -- Highly Divisible Triangular Number")
    b2 = default_timer()
    b3 = 500 * 2
    while True:
        b4 = (b3 * (b3 + 1))
        b5 = fonk1(b4)
        a2 = 1
        for factor in set(b5):
            a2 *= (b5.count(factor) + 1)
        if a2 > 500:
            break
        b3 += 1
    b6 = default_timer()
    b7 = (b6 - b2) * 1000
    print("   Triangle Number x with over 500 b1:   %d" % b4)
    print("   Computation Time:                          %.3fms" % b7)
if b8 = = '__main__':
    fonk2()