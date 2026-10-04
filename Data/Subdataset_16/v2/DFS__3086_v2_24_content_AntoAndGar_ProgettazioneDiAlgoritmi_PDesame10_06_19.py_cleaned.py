def fonk1(a1):
    b1 = [0] * (a1 + 1)
    b1[0], b1[1], b1[2] = 1, 4, 10
    for i in range(3, a1 + 1):
        b1[i] = 3 * b1[i - 1] - b1[i - 2]
    return b1[a1]
a1 = 5
b2 = fonk1(a1)
print(f"The {a1}th value in the sequence is: {b2}")