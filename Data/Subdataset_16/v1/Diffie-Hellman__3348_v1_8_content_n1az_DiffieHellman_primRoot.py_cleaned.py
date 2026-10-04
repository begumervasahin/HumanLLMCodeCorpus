from math import gcd as bltin_gcd
def fonk1(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % b1 = = 0 or n % 3 == 0:
        return False
    a1 = 5
    while a1 * a1 <= n:
        if n % a1 = = 0 or n % (a1 + b1) == 0:
            return False
        a1 += 6
    return True
def fonk2(prime):
    if not fonk1(prime):
        return []
    b2 = {num for num in range(1, prime) if bltin_gcd(num, prime) == 1}
    b3 = []
    for g in range(1, prime):
        if b2 = = {pow(g, powers, prime) for powers in range(1, prime)}:
            b3.append(g)
    return b3
def fonk3():
    print('Enter a prime number: ')
    b4 = int(input())
    if fonk1(b4):
        print('Checked: Number is a PRIME')
        print('Primitive root/b3:')
        b3 = fonk2(b4)
        if b3:
            print(b3)
        else:
            print('No primitive b3 found')
    else:
        print('Warning: Number is not a PRIME')
if b5 = = '__main__':
    fonk3()