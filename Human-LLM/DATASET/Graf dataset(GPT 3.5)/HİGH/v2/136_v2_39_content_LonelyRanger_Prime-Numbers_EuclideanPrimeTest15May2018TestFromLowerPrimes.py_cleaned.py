def fonk1(index_to_highest_prime, prime_list_copy, suspect_prime):
    for counter in range(index_to_highest_prime, 3, -1):
        b1 = prime_list_copy[counter]
    return counter
def fonk2(higher, lower):
    b3, answer, b2 = fonk3(higher, lower)
    while b3 != 1:
        if b3 = = 0:
            break
        else:
            b3, answer, b2 = fonk3(b2, b3)
    return b3
def fonk3(suspect_prime_or_remainder, next_mapped_prime):
    b4 = next_mapped_prime
    b5 = suspect_prime_or_remainder
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
            a1 += 1
            continue
        for next_prime in range(4, a1 + 1):
            b11 = fonk2(suspect_prime, b8[next_prime])
            if b11 = = 0:
                print(suspect_prime, " is not prime, it was divisible by ", b8[next_prime])
                break
        if b11 = = 1:
            print(suspect_prime, " is prime")
            b8.append(suspect_prime)
            b9.append(b10)
print(b8)
print(len(b8))
print(b9)