import time
def fonk1(b2):
    b1 = []
    a1 = 2
    while a1 <= b2:
        if b2 % a1 = = 0:
            b1.append(a1)
            b2 = b2
        else:
            a1 += 1
    return b1
def fonk2(prime_factors):
    b3 = set()
    b4 = len(prime_factors)
    for a1 in range(b4):
        for j in range(a1 + 1, b4):
            b5 = prime_factors[a1] * prime_factors[j]
            b3.add(b5)
            b6 = b5
            for k in range(j + 1, b4):
                b6 *= prime_factors[k]
                b3.add(b6)
    return b3
def fonk3(b2):
    b7 = fonk1(b2)
    print(f"Prime b1: {b7}")
    print(f"Number of prime b1: {len(b7)}, Sum of prime b1: {sum(b7)}")
    b3 = fonk2(b7)
    b8 = set(b7).union(b3)
    return [1] + sorted(b8)
if b9 = = '__main__':
    b10 = time.time()
    b11 = fonk3(33550336)
    print(f"Factors: {b11}")
    print(f"Execution time: {time.time() - b10} seconds")