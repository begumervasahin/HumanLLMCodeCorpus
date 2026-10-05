def fonk1(b2):
    a1 = 0
    for j in range(len(b2) - 1):
        print("\n\n", "-" * 50, "Iteration", j)
        for i in range(len(b2) - 1 - j):
            a1 += 1
            print("\n", "*" * 80, "\ncomparing", b2[i], b2[i + 1])
            if b2[i] > b2[i + 1]:
                b2[i], b2[i + 1] = b2[i + 1], b2[i]
                print("swapped", b2[i], b2[i + 1])
                print("array is now", b2)
            else:
                print("no need to swap", b2[i], b2[i + 1])
    print("Number of b1 = ", a1)
    return b2
def fonk2():
    b2 = [1, 5, 3, 2, 0, 8]
    b3 = fonk1(b2)
    print("Sorted array:", b3)
if b4 = = "__main__":
    fonk2()