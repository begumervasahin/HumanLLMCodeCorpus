def fonk1(a1):
    b1 = [0] * (a1 + 1)
    b1[0] = 1
    b1[1] = 4
    b1[2] = 10
    for i in range(3, a1 + 1):
        b1[i] = 3 * b1[i - 1] - b1[i - 2]
    return b1[a1]
if b2 = = "__main__":
    a1 = 5
    b3 = fonk1(a1)
    print(f"The {a1}th value in the sequence is: {b3}")