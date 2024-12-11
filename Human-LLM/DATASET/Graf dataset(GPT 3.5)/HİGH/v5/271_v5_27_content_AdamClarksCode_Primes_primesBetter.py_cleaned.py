def fonk1(a1):
    b1 = [True] * (a1 + 1)
    b1[0], b1[1] = False, False
    for i in range(2, int(a1 ** 0.5) + 1):
        if b1[i]:
            for j in range(i * i, a1 + 1, i):
                b1[j] = False
    return [num for num, is_prime in enumerate(b1) if is_prime]
def fonk2(a1):
    b1 = [True] * (a1
    b1[0] = False
    for i in range(3, int(a1 ** 0.5) + 1, 2):
        if b1[i
            for j in range(i * i
                b1[j] = False
    return [2] + [2 * i + 1 for i, is_prime in enumerate(b1) if is_prime]
if b2 = = "__main__":
    a1 = 2000000000
    b3 = fonk2(a1)
    print(f"There are {len(b3)} primes from 0 to {a1}")