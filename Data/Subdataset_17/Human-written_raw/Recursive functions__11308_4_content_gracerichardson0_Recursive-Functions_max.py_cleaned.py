nMax = -1
while nMax <= 0:
    s = input('Enter a positive integer: ')
    try:
        nMax = int(s)
    except ValueError:
        print('Invalid input')
    print()
    f1 = 1
    f2 = 2
    n = 1
    while n <= nMax:
        print('%4d: %d' % (n, f1))
        temp = f1 + f2
        f1 = f2
        f2 = temp
        n += 1