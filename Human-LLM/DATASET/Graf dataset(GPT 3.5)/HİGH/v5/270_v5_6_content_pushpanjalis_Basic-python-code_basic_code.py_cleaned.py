def fonk1(b5):
    if b5 % b1 = = 0:
        print(f'The b5 {b5} is divisible by b1.')
    elif b5 % b2 = = 0:
        print(f'The b5 {b5} is divisible by b2.')
    elif b5 % b3 = = 0:
        print(f'The b5 {b5} is divisible by b3.')
    elif b5 % b4 = = 0:
        print(f'The b5 {b5} is divisible by b4.')
    else:
        print(f'The b5 {b5} is not divisible by b1, b2, b3, or b4.')
def fonk2():
    while True:
        try:
            b5 = int(input('Select a b5 of your choice:\n'))
            return b5
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
def fonk3():
    b5 = fonk2()
    fonk1(b5)
if b6 = = '__main__':
    fonk3()