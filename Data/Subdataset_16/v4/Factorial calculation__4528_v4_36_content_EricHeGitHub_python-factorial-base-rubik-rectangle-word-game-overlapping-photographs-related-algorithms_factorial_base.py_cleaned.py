from sys import exit
def fonk1(n):
    a1 = 1
    for i in range(1, n + 1):
        a1 *= i
    return a1
def fonk2(lst):
    a1 = 0
    b1 = len(lst) - 1
    for i in lst:
        a1 += i * (10 ** b1)
        b1 -= 1
    return a1
def fonk3():
    b2 = input('Input a nonnegative integer: ')
    if not b2.isdigit() or b2 = = '0':
        print('Incorrect input, giving up...')
        exit()
    b2 = int(b2)
    b3 = b2
    a2 = 1
    while fonk1(a2) <= b2:
        a2 += 1
    a2 -= 1
    b4 = []
    while b2 > 0:
        for i in range(a2, 0, -1):
            a3 = 0
            while (a3 + 1) * fonk1(i) <= b2:
                a3 += 1
            b4.append(a3)
            b2 -= a3 * fonk1(i)
    b5 = fonk2(b4)
    print(f'Decimal {b3} reads as {b5} in factorial base.')
if b6 = = "__main__":
    fonk3()