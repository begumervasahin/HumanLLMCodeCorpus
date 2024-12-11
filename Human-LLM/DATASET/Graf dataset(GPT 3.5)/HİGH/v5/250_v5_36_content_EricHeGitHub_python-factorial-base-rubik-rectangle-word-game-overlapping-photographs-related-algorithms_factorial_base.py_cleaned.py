from sys import exit
def fonk1(n):
    a1 = 1
    for i in range(1, n + 1):
        a1 *= i
    return a1
def fonk2(lst):
    a1 = 0
    b1 = len(lst) - 1
    for digit in lst:
        if not str(digit).isdigit():
            return None
        a1 += digit * 10 ** b1
        b1 -= 1
    return a1
def fonk3():
    b2 = input('Input a nonnegative integer: ')
    return int(b2) if b2.isdigit() and b2[0] != '0' else None
def fonk4():
    b2 = fonk3()
    if b2 is None:
        print('Incorrect input, giving up...')
        exit()
    a2 = 1
    while fonk1(a2) <= b2:
        a2 += 1
    a2 -= 1
    a3 = 0
    b3 = []
    b4 = b2
    while b2:
        for i in range(a2, 0, -1):
            while a3 * fonk1(i) < b2:
                a3 += 1
            if a3 * fonk1(i) > b2:
                a3 -= 1
            else:
                pass
            b3.append(a3)
            b2 -= a3 * fonk1(i)
            a3 = 0
    print('Decimal {} reads as {} in factorial base.'.format(b4, fonk2(b3)))
if b5 = = "__main__":
    fonk4()