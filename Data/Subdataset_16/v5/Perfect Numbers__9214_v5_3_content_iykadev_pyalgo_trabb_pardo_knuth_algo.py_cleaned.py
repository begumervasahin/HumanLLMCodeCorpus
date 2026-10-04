import math
def fonk1(x):
    return math.sqrt(abs(x)) + 5 * x ** 3
def fonk2():
    b1 = input('\nEnter 11 b2 separated by spaces: ')
    return [float(num) for num in b1.strip().split()[:11]]
def fonk3():
    b2 = fonk2()
    b2.reverse()
    for x in b2:
        b3 = fonk1(x)
        if b3 > 400:
            print(f'{x}: TOO LARGE!', b4 = ' ')
        else:
            print(f'{x}: {b3}', b4 = ' ')
    print('')
if b5 = = '__main__':
    fonk3()