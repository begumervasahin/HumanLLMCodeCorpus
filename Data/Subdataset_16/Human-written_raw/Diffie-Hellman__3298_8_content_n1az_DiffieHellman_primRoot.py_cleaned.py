from math import gcd as bltin_gcd
def fonk1(b6) :
    if (b6 <= 1) :
        return False
    if (b6 <= 3) :
        return True
    if (b6 % b1 = = 0 or b6 % 3 == 0) :
        return False
    a1 = 5
    while(a1 * a1 <= b6) :
        if (b6 % a1 = = 0 or b6 % (a1 + b1) == 0) :
            return False
        a1 = a1 + 6
    return True
def fonk2(_inprime):
    b2 = {num for num in range(1, _inprime) if bltin_gcd(num, _inprime) }
    return [g for g in range(1, _inprime) if b2 = = {pow(g, powers, _inprime)
            for powers in range(1, _inprime)}]
if b3 = = '__main__':
    print('Enter a prime number: ')
    b4 = int(input())
    b5 = 'Checked : Number is a PRIME'
    b6 = 'Warning : Number is not a PRIME'
    if (fonk1(b4)):
        print(b5)
        print('Primitive root/roots : ')
        print(fonk2(b4))
    else :
        print(b6)