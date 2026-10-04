def fonk1():
    while True:
        try:
            b1 = int(input('Enter a positive integer: '))
            if b1 > 0:
                return b1
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
def fonk2(b3):
    f1, b2 = 1, 2
    for b1 in range(1, b3 + 1):
        print(f'{b1:4d}: {f1}')
        f1, b2 = b2, f1 + b2
def fonk3():
    b3 = fonk1()
    fonk2(b3)
if b4 = = '__main__':
    fonk3()