
def fonk1(a1):
    if a1 <= 1:
        return a1
    return fonk1(a1 - 1) + fonk1(a1 - 2)
def fonk2(a2, b1):
    if b1 = = 0:
        return a2
    return fonk2(b1, a2 % b1)
def fonk3(b2, b3):
    if not b2 and not b3:
        return 0
    if not b2:
        return -1
    if not b3:
        return 1
    if b2[0] < b3[0]:
        return -1
    if b2[0] > b3[0]:
        return 1
    return fonk3(b2[1:], b3[1:])
def fonk4():
    a1 = 10
    print(f'Fibonacci of {a1}: {fonk1(a1)}')
    a2 = 48
    b1 = 18
    print(f'GCD of {a2} and {b1}: {fonk2(a2, b1)}')
    b2 = "apple"
    b3 = "apricot"
    b4 = fonk3(b2, b3)
    if b4 < 0:
        print(f'"{b2}" is less than "{b3}"')
    elif b4 > 0:
        print(f'"{b2}" is greater than "{b3}"')
    else:
        print(f'"{b2}" is equal to "{b3}"')
if b5 = = '__main__':
    fonk4()