def fonk1(b3):
    a1 = 0
    b1 = []
    for b2 in range(1, (b3
        if b3 % b2 = = 0:
            a1 += b2
            b1.append(b2)
    return a1, b1
def fonk2(b3):
    a1, b1 = fonk1(b3)
    if a1 = = b3:
        return 'Perfect'
    elif a1 < b3:
        return 'Deficient'
    else:
        return 'Abundant'
def fonk3(b3):
    b1 = [b2 for b2 in range(1, (b3
    return b1
def fonk4():
    b3 = int(input("Enter a number: "))
    b4 = fonk2(b3)
    print('Number:', b3)
    print('Number type:', b4)
    a1, b1 = fonk1(b3)
    print('Factors:', b1)
    print('Sum of b1:', a1)
    print('Number of b1:', len(b1))
    if b4 = = 'Deficient':
        b5 = fonk3(b3)
        print('Perfect square b1:', b5)
        print('Number of perfect square b1:', len(b5))
if b6 = = '__main__':
    fonk4()