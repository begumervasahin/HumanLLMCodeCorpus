def fonk1(b1):
    a1 = 0
    for iteration in range(len(b1) - 1):
        print("\n", "-" * 50, "Iteration", iteration)
        for i in range(len(b1) - 1 - iteration):
            a1 += 1
            print("\n", "*" * 80, "\nComparing", b1[i], b1[i + 1])
            if b1[i] > b1[i + 1]:
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
                print("Swapped", b1[i], b1[i + 1])
                print("Array is now", b1)
            else:
                print("No need to swap", b1[i], b1[i + 1])
    print("Number of a1 = ", a1)
    return b1
b1 = [1, 5, 3, 2, 0, 8]
print(fonk1(b1))