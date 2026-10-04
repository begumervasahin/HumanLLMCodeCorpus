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
    print(f"Prime factors: {b1}")
    print(f"Number of prime factors: {len(b1)}, Sum of prime factors: {sum(b1)}")
    b3 = set()
    b4 = len(b1)
    for a1 in range(b4):
        for j in range(a1 + 1, b4):
            b5 = b1[a1] * b1[j]
            b3.add(b5)
            b6 = b5
            for k in range(j + 1, b4):
                b6 *= b1[k]
                b3.add(b6)
    b7 = set(b1).union(b3)
    return [1] + sorted(b7)
if b8 = = '__main__':
    b9 = time.time()
    b10 = fonk1(33550336)
    print(f"Factors: {b10}")
    print(f"Execution time: {time.time() - b9} seconds")