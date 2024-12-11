def fonk1(IndexToHighestPrime, CopyOfPrimeList, SuspectPrime):
    for counter in range(IndexToHighestPrime, 3, -1):
        b1 = CopyOfPrimeList[counter]
        ''' This is the actual Euclidean GCD test
        '''
    return counter
def fonk2(Higher, Lower):
    b3, Answer, b2 = fonk3(Higher, Lower)
    while b3 != 1:
        if b3 = = 0:
            break
        else:
            b3, Answer, b2 = fonk3(b2, b3)
    return b3
def fonk3(SuspectPrimeOrRemainder, NextMappedPrime):
    b4 = NextMappedPrime
    b5 = SuspectPrimeOrRemainder
    b6 = b5
    b7 = b5 % b4
    return b7, b6, b4
b8 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
b9 = [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209, 2809]
for suspect_prime in range(59, 2001, 2):
    if suspect_prime % 3 != 0 and suspect_prime % 5 != 0 and suspect_prime % 7 != 0:
        b10 = suspect_prime * suspect_prime
        a1 = 1
        while b9[a1] < suspect_prime:
            a1 = a1 + 1
            continue
        ''' Now we have exited with our pointer stored in a1 Here we go with the test
        '''
        for nextprime in range(4, a1 + 1, 1):
            b11 = fonk2(suspect_prime, b8[nextprime])
            if b11 = = 0:
                print(suspect_prime, " is not prime, it was divisible by ", b8[nextprime])
                break
        if b11 = = 1:
            print(suspect_prime, " is prime")
            b8.append(suspect_prime)
            b9.append(b10)
print(b8)
print(len(b8))
print(b9)