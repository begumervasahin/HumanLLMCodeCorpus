
def fonk1(a1):
    if a1 <= 1:
        return a1
    else:
        return fonk1(a1 - 1) + fonk1(a1 - 2)
def fonk2(a2, b1):
    if b1 = = 0:
        return a2
    else:
        return fonk2(b1, a2 % b1)
def fonk3(b3, b4):
    if not b3 and not b4:
        return 0
    if not b3:
        return -1
    if not b4:
        return 1
    if b3[0] < b4[0]:
        return -1
    if b3[0] > b4[0]:
        return 1
    return fonk3(b3[1:], b4[1:])
if b2 = = '__main__':
    a1 = 10
    print(f'Fibonacci of {a1}: {fonk1(a1)}')
    a2 = 48
    b1 = 18
    print(f'GCD of {a2} and {b1}: {fonk2(a2, b1)}')
    b3 = "apple"
    b4 = "apricot"
    b5 = fonk3(b3, b4)
    if b5 < 0:
        print(f'"{b3}" is less than "{b4}"')
    elif b5 > 0:
        print(f'"{b3}" is greater than "{b4}"')
    else:
        print(f'"{b3}" is equal to "{b4}"')