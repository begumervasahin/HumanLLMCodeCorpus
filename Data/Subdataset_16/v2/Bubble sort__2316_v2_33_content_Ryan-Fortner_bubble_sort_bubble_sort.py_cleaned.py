b1 = [1, 5, 3, 2, 0, 8]
def fonk1(b1):
    a1 = 0
    for j in range(len(b1) - 1):
        print("\n", "-" * 50, f"Iteration {j + 1}")
        for i in range(len(b1) - 1 - j):
            a1 += 1
            print("\n", "*" * 80)
            print(f"Comparing {b1[i]} and {b1[i + 1]}")
            if b1[i] > b1[i + 1]:
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
                print(f"Swapped: {b1[i]} and {b1[i + 1]}")
                print("Array is now:", b1)
            else:
                print(f"No need to swap: {b1[i]} and {b1[i + 1]}")
    print("Number of b2 = ", a1)
    return b1
b3 = fonk1(b1)
print("\nSorted array:", b3)