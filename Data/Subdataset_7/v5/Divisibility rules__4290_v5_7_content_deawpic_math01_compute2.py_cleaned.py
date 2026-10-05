def fonk1(num):
    if num <= 1:
        return False
    for b1 in range(2, int(num**0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(start, end):
    return [number for number in range(start, end + 1) if fonk1(number)]
def fonk3(prime_list, limit):
    b2 = [1]
    for i in range(len(prime_list)):
        b3 = prime_list[i] * prime_list[i]
        if b3 < limit:
            b2.append(b3)
            for j in range(i, len(prime_list)):
                b4 = prime_list[i] * prime_list[j]
                if b4 < limit:
                    b2.append(b4)
                else:
                    break
        else:
            break
    return b2
def fonk4():
    b5 = fonk2(9, 200)
    b6 = fonk3(b5, 201)
    b7 = sorted(b5 + b6)
    print("Combined list of primes, squares, and products:", b7)
    print("Sorted list of primes:", b5)
    print("Number of prime numbers:", len(b5))
if b8 = = "__main__":
    fonk4()