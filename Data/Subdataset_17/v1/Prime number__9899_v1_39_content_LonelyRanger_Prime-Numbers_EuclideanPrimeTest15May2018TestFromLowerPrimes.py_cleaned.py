
Primes_So_Far = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
Squares_of_Primes_So_Far = [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209, 2809]
def GcdIterationTest(Higher, Lower):
    Remains, Answer, NextDivisor = ModularDivision(Higher, Lower)
    while Remains != 1:
        if Remains == 0:
            break
        else:
            Remains, Answer, NextDivisor = ModularDivision(NextDivisor, Remains)
        if Remains == 0:
            break
    return Remains
def ModularDivision(SuspectPrimeOrRemainder, NextMappedPrime):
    Divisor = NextMappedPrime
    Dividend = SuspectPrimeOrRemainder
    Quotient = Dividend
    Remainder = Dividend % Divisor
    return Remainder, Quotient, Divisor
for suspect_prime in range(59, 2001, 2):
    if suspect_prime % 3 != 0 and suspect_prime % 5 != 0 and suspect_prime % 7 != 0:
        suspect_squared = suspect_prime * suspect_prime
        count_squared = 1
        while Squares_of_Primes_So_Far[count_squared] < suspect_prime:
            count_squared += 1
        for nextprime in range(4, count_squared + 1):
            GCDOutcome = GcdIterationTest(suspect_prime, Primes_So_Far[nextprime])
            if GCDOutcome == 0:
                print(f"{suspect_prime} is not prime, it was divisible by {Primes_So_Far[nextprime]}")
                break
        if GCDOutcome == 1:
            print(f"{suspect_prime} is prime")
            Primes_So_Far.append(suspect_prime)
            Squares_of_Primes_So_Far.append(suspect_squared)
print(Primes_So_Far)
print(len(Primes_So_Far))
print(Squares_of_Primes_So_Far)