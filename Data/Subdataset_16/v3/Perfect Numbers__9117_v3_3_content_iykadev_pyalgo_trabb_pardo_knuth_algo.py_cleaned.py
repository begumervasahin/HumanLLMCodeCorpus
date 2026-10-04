import math
def fonk1(x):
    return math.sqrt(abs(x)) + 5 * x ** 3
def fonk2():
    while True:
        try:
            b1 = input('\nEnter 11 b1: ').strip().split()
            if len(b1) != 11:
                print("Please enter exactly 11 b1.")
                continue
            return [float(y) for y in b1]
        except ValueError:
            print("Please enter valid b1.")
def fonk3():
    b1 = fonk2()
    b1.reverse()
    for x in b1:
        b2 = fonk1(x)
        if b2 > 400:
            print(f' {x}: TOO LARGE!', b3 = '')
        else:
            print(f' {x}: {b2}', b3 = '')
    print('')
if b4 = = '__main__':
    fonk3()