def fonk1(b5):
    a1 = 0
    b1 = []
    for b2 in range(1, b5
        if b5 % b2 = = 0:
            a1 += b2
            b1.append(b2)
    return a1, b1
def fonk2(b5):
    a1, b3 = fonk1(b5)
    if a1 = = b5:
        return 'Perfect'
    elif a1 < b5:
        return 'Deficient'
    else:
        return 'Abundant'
def fonk3(b5):
    b4 = [b2 for b2 in range(1, b5
    return b4
def fonk4():
    b5 = int(input("Enter a number: "))
    b6 = fonk2(b5)
    print('Number:', b5)
    print('Number type:', b6)
    a1, b1 = fonk1(b5)
    print('Factors:', b1)
    print('Sum of b1:', a1)
    print('Number of b1:', len(b1))
    if b6 = = 'Deficient':
        b4 = fonk3(b5)
        print('Perfect square b1:', b4)
        print('Number of perfect square b1:', len(b4))
if b7 = = '__main__':
    fonk4()