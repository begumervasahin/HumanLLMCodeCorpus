def fonk1(n):
    b1 = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if b1[i]:
            b1[i * i::2 * i] = [False] * ((n - i * i - 1)
    return [2] + [i for i in range(3, n, 2) if b1[i]]
def fonk2(n):
    b1 = [True] * (n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if b1[i
            b1[i * i
    return [2] + [2 * i + 1 for i in range(1, n
if b2 = = "__main__":
    a1 = 2000000000
    b3 = fonk2(a1)
    print(f"There are {len(b3)} primes from 0 to {a1}")