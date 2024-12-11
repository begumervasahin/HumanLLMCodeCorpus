def fonk1(n):
    a1 = 0
    b1 = []
    a2 = 1
    while a2 <= (n + 1) / 2:
        if n % a2 = = 0:
            a1 += a2
            b1.append(a2)
        a2 += 1
    return a1, b1
def fonk2(n):
    a1, b2 = fonk1(n)
    if a1 = = n:
        return 'Perfect'
    elif a1 < n:
        return 'Deficient'
    else:
        return 'Abundant'
def fonk3(n):
    b1 = []
    a2 = 1
    while a2 <= (n + 1) / 2:
        b3 = a2 ** 2
        if n % b3 = = 0:
            b1.append(a2)
        a2 += 1
    return b1
if b4 = = "__main__":
    b5 = int(input("Enter a b5: "))
    print("Classifying b5...")
    b6 = fonk2(b5)
    print(f"Classification: {b6}")
    if b6 in ['Perfect', 'Deficient']:
        factors_sum, b1 = fonk1(b5)
        print(f"Factors: {b1}")
        print(f"Sum of b1: {factors_sum}")
        print(f"Number of b1: {len(b1)}")
    else:
        b7 = fonk3(b5)
        print(f"Perfect square b1: {b7}")
        print(f"Number of perfect square b1: {len(b7)}")