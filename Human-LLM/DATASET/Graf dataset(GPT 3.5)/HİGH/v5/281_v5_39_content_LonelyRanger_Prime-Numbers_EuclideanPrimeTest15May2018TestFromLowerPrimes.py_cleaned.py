
b1 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
b2 = [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209, 2809]
def fonk1(index_to_highest_prime, copy_of_prime_list, suspect_prime):
    for counter in range(index_to_highest_prime, 3, -1):
        b3 = copy_of_prime_list[counter]
    return counter
def fonk2(higher, lower):
    b5, answer, b4 = fonk3(higher, lower)
    while b5 != 1:
        if b5 = = 0:
            break
        else:
            b5, answer, b4 = fonk3(b4, b5)
        continue
        if b5 = = 0:
            break
    return b5
def fonk3(suspect_prime_or_remainder, next_mapped_prime):
    b6 = next_mapped_prime
    b7 = suspect_prime_or_remainder
    b8 = b7
    b9 = b7 % b6
    return b9, b8, b6
for suspect_prime in range(59, 2001, 2):
    if suspect_prime % 3 != 0 and suspect_prime % 5 != 0 and suspect_prime % 7 != 0:
        b10 = suspect_prime * suspect_prime
        a1 = 1
        while b2[a1] < suspect_prime:
            a1 += 1
            continue
        for nextprime in range(4, a1 + 1, 1):
            b11 = fonk2(suspect_prime, b1[nextprime])
            if b11 = = 0:
                print(suspect_prime, " is not prime, it was divisible by ", b1[nextprime])
                break
        if b11 = = 1:
            print(suspect_prime, " is prime")
            b1.append(suspect_prime)
            b2.append(b10)
print(b1)
print(len(b1))
print(b2)