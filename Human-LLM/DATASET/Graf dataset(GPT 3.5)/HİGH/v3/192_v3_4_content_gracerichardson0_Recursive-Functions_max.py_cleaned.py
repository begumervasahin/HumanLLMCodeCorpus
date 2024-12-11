def fonk1(prompt):
    while True:
        b1 = input(prompt)
        try:
            b2 = int(b1)
            if b2 > 0:
                return b2
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a positive integer.')
b3 = fonk1('Enter a positive integer: ')
a1 = 1
a2 = 2
b2 = 1
while b2 <= b3:
    print(f'{b2:4d}: {a1}')
    b4 = a1 + a2
    a1 = a2
    a2 = b4
    b2 += 1
