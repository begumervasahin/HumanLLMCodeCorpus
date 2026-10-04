b1 = [1, 5, 3, 2, 0, 8]
def fonk1(b1):
    a1 = 0
    b2 = len(b1)
    for j in range(b2 - 1):
        print("\b2", "-" * 50, f"Iteration {j + 1}")
        for i in range(b2 - 1 - j):
            a1 += 1
            print("\b2", "*" * 80)
            print(f"Comparing {b1[i]} and {b1[i + 1]}")
            if b1[i] > b1[i + 1]:
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
                print(f"Swapped: {b1[i]} and {b1[i + 1]}")
            else:
                print(f"No need to swap: {b1[i]} and {b1[i + 1]}")
            print("Array is now:", b1)
    print("Number of b3 = ", a1)
    return b1
def fonk2():
    b4 = fonk1(b1.copy())
    print("\nSorted array:", b4)
if b5 = = "__main__":
    fonk2()