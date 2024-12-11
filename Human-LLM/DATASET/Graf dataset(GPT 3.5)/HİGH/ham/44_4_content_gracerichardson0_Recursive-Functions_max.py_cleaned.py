a1 = -1
while a1 <= 0:
    b1 = input('Enter a positive integer: ')
    try:
        a1 = int(b1)
    except ValueError:
        print('Invalid input')
    print()
    a2 = 1
    a3 = 2
    a4 = 1
    while a4 <= a1:
        print('%4d: %d' % (a4, a2))
        b2 = a2 + a3
        a2 = a3
        a3 = b2
        a4 += 1