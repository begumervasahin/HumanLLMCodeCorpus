def fonk1(a1):
    if a1 < 0:
        raise ValueError("a1 must be a non-negative integer")
    b1 = [0] * (a1 + 1)
    b2 = {0: 1, 1: 4, 2: 10}
    for i in range(min(3, a1 + 1)):
        b1[i] = b2[i]
    for i in range(3, a1 + 1):
        b1[i] = 3 * b1[i - 1] - b1[i - 2]
    return b1[a1]
if b3 = = "__main__":
    a1 = 5
    b4 = fonk1(a1)
    print(f"The {a1}th value in the sequence is: {b4}")