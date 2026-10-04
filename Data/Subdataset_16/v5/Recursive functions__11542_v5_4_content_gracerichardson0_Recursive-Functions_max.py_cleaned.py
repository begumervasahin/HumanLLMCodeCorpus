def fonk1():
    a1 = -1
    while a1 <= 0:
        b1 = input('Enter a positive integer: ')
        try:
            a1 = int(b1)
            if a1 <= 0:
                print('Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid positive integer.')
        print()
    f1, b2 = 1, 2
    for n in range(1, a1 + 1):
        print(f'{n:4d}: {f1}')
        f1, b2 = b2, f1 + b2
if b3 = = '__main__':
    fonk1()