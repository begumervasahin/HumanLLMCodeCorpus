def fonk1():
    a1 = -1
    while a1 <= 0:
        b1 = input('Enter a positive integer: ')
        try:
            a1 = int(b1)
        except ValueError:
            print('Invalid input')
        print()
    return a1
def fonk2(a1):
    a2 = 1
    a3 = 2
    a4 = 1
    while a4 <= a1:
        print('%4d: %d' % (a4, a2))
        a2, a3 = a3, a2 + a3
        a4 += 1
def fonk3():
    a1 = fonk1()
    fonk2(a1)
if b2 = = "__main__":
    fonk3()