
def fonk1(a, b1):
    while b1:
        a, b1 = b1, a % b1
    return a
def fonk2(suspect_prime, b2):
    if suspect_prime < 2:
        return False
    for prime in b2:
        if prime * prime > suspect_prime:
            break
        if fonk1(suspect_prime, prime) != 1:
            return False
    return True
def fonk3():
    b2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    b3 = [p * p for p in b2]
    for suspect_prime in range(59, 2001, 2):
        if all(suspect_prime % p != 0 for p in [3, 5, 7]):
            if fonk2(suspect_prime, b2):
                print(f"{suspect_prime} is prime")
                b2.append(suspect_prime)
                b3.append(suspect_prime * suspect_prime)
            else:
                print(f"{suspect_prime} is not prime")
    print("Primes so far:", b2)
    print("Total primes found:", len(b2))
    print("Squares of primes so far:", b3)
if b4 = = "__main__":
    fonk3()