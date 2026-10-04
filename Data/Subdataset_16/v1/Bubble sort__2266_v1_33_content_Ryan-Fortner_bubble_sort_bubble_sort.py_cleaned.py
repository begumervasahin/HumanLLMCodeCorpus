b1 = [1, 5, 3, 2, 0, 8]
def fonk1(b1):
    a1 = 0
    for j in range(len(b1) - 1):
        print("\n\n", "-" * 50, "Iteration", j)
        for i in range(len(b1) - 1 - j):
            a1 += 1
            print("\n", "*" * 80, "\ncomparing", b1[i], b1[i + 1])
            if b1[i] > b1[i + 1]:
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
                print("swapped", b1[i], b1[i + 1])
                print("array is now", b1)
            else:
                print("no need to swap", b1[i], b1[i + 1])
    print("Number of b2 = ", a1)
    return b1
print(fonk1(b1))