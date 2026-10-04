
b1 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
b2 = [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209, 2809]
def fonk1(higher, lower):
    b4, _, b3 = fonk2(higher, lower)
    while b4 != 1:
        if b4 = = 0:
            break
        b4, _, b3 = fonk2(b3, b4)
        if b4 = = 0:
            break
    return b4
def fonk2(dividend, divisor):
    b5 = dividend
    b4 = dividend % divisor
    return b4, b5, divisor
for suspect_prime in range(59, 2001, 2):
    if suspect_prime % 3 != 0 and suspect_prime % 5 != 0 and suspect_prime % 7 != 0:
        b6 = suspect_prime * suspect_prime
        a1 = 1
        while b2[a1] < suspect_prime:
            a1 += 1
        b7 = True
        for nextprime in range(4, a1 + 1):
            b8 = fonk1(suspect_prime, b1[nextprime])
            if b8 = = 0:
                print(f"{suspect_prime} is not prime, it was divisible by {b1[nextprime]}")
                b7 = False
                break
        if b7:
            print(f"{suspect_prime} is prime")
            b1.append(suspect_prime)
            b2.append(b6)
print(b1)
print(len(b1))
print(b2)