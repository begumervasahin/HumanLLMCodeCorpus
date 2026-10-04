
a1 = 5
b1 = [0 for _ in range(a1 + 1)]
def fonk1(a1):
    b1[0] = 1
    b1[1] = 4
    b1[2] = 10
    for i in range(3, a1 + 1):
        b1[i] = 3 * b1[i - 1] - b1[i - 2]
    return b1[a1]
print(fonk1(a1))