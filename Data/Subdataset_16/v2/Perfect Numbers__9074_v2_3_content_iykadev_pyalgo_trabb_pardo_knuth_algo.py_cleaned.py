def fonk1(x):
    return abs(x) ** 0.5 + 5 * x ** 3
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
if b2 = = '__main__':
    b1 = fonk2()
    b1.reverse()
    for x in b1:
        b3 = fonk1(x)
        if b3 > 400:
            print(f' {x}: TOO LARGE!', b4 = '')
        else:
            print(f' {x}: {b3}', b4 = '')
    print('')