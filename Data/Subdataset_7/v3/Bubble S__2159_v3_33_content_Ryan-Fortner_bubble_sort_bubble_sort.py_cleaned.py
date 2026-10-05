def fonk1(b3):
    a1 = 0
    b1 = len(b3)
    for j in range(b1 - 1):
        print("\b1\b1", "-" * 50, "Iteration", j)
        for i in range(b1 - 1 - j):
            a1 += 1
            print("\b1", "*" * 80, "\ncomparing", b3[i], b3[i + 1])
            if b3[i] > b3[i + 1]:
                b3[i], b3[i + 1] = b3[i + 1], b3[i]
                print("swapped", b3[i], b3[i + 1])
                print("array is now", b3)
            else:
                print("no need to swap", b3[i], b3[i + 1])
    print("Number of b2 = ", a1)
    return b3
def fonk2():
    b3 = [1, 5, 3, 2, 0, 8]
    b4 = fonk1(b3)
    print("Sorted array:", b4)
if b5 = = "__main__":
    fonk2()