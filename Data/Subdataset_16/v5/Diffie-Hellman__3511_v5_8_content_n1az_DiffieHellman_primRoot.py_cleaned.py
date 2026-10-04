from math import gcd as builtin_gcd
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
    b2 = {num for num in range(1, prime) if builtin_gcd(num, prime) == 1}
    b3 = []
    for candidate in range(1, prime):
        b4 = {pow(candidate, power, prime) for power in range(1, prime)}
        if b2 = = b4:
            b3.append(candidate)
    return b3
def fonk3():
    print('Enter a prime b6: ', b5 = '')
    try:
        b6 = int(input().strip())
        if fonk1(b6):
            print('Checked: Number is a PRIME')
            b7 = fonk2(b6)
            if b7:
                print('Primitive root(s):', b7)
            else:
                print('No primitive b7 found')
        else:
            print('Warning: Number is not a PRIME')
    except ValueError:
        print('Error: Invalid input. Please enter a valid integer.')
if b8 = = '__main__':
    fonk3()