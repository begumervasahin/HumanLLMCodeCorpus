def gcd_test_for_primes(index_to_highest_prime, prime_list_copy, suspect_prime):
    for counter in range(index_to_highest_prime, 3, -1):
        next_dividend = prime_list_copy[counter]
    return counter
def gcd_iteration_test(higher, lower):
    remains, answer, next_divisor = modular_division(higher, lower)
    while remains != 1:
        if remains == 0:
            break
        else:
            remains, answer, next_divisor = modular_division(next_divisor, remains)
    return remains
def modular_division(suspect_prime_or_remainder, next_mapped_prime):
    divisor = next_mapped_prime
    dividend = suspect_prime_or_remainder
    quotient = dividend
    remainder = dividend % divisor
    return remainder, quotient, divisor
primes_so_far = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
squares_of_primes_so_far = [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209, 2809]
for suspect_prime in range(59, 2001, 2):
    if suspect_prime % 3 != 0 and suspect_prime % 5 != 0 and suspect_prime % 7 != 0:
        suspect_squared = suspect_prime * suspect_prime
        count_squared = 1
        while squares_of_primes_so_far[count_squared] < suspect_prime:
            count_squared += 1
            continue
        for next_prime in range(4, count_squared + 1):
            gcd_outcome = gcd_iteration_test(suspect_prime, primes_so_far[next_prime])
            if gcd_outcome == 0:
                print(suspect_prime, " is not prime, it was divisible by ", primes_so_far[next_prime])
                break
        if gcd_outcome == 1:
            print(suspect_prime, " is prime")
            primes_so_far.append(suspect_prime)
            squares_of_primes_so_far.append(suspect_squared)
print(primes_so_far)
print(len(primes_so_far))
print(squares_of_primes_so_far)