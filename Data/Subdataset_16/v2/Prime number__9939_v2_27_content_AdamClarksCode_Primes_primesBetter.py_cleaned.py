def fonk1(a1):
    b1 = [True] * a1
    b1[0] = b1[1] = False
    for num in range(3, int(a1 ** 0.5) + 1, 2):
        if b1[num]:
            b1[num * num::2 * num] = [False] * ((a1 - num * num - 1)
    return [2] + [num for num in range(3, a1, 2) if b1[num]]
def fonk2(a1):
    b1 = [True] * (a1
    for num in range(3, int(a1 ** 0.5) + 1, 2):
        if b1[num
            b1[num * num
    return [2] + [2 * num + 1 for num in range(1, a1
if b2 = = "__main__":
    a1 = 2000000000
    b3 = fonk2(a1)
    print(f"There are {len(b3)} primes from 0 to {a1}")