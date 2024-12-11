import random
def fonk1(n):
    a1 = 10
    a2 = 2
    while a2 < n:
        if all(a1 % a4 != 0 for a4 in range(2, a1)):
            a2 += 1
        a1 += 1
        b1 = 2**a2 - 1
    return a1 - 1, b1
def fonk2():
    b2 = [a4 + 1 for a4 in range(10) if a4 % 2 == 0]
    print(b2)
def fonk3():
    a3 = 0
    a4 = 1
    while True:
        a3 += a4
        a4 += 1
        if a3 > 10:
            break
    print('a4 = {}, sum = {}'.format(a4, a3))
def fonk4():
    a4 = 1
    while(a4 % 3):
        print(a4, b3 = ' ')
        if (a4 >= 10):
            break
        a4 += 1
def fonk5(num, base):
    if(num >= base):
        fonk5(num
    print(num % base, b3 = ' ')
