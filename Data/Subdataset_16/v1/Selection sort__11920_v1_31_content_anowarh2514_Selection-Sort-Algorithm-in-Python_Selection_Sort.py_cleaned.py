def fonk1(b3):
    b1 = len(b3)
    for i in range(b1 - 1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
        print(f"Step {i + 1}: {b3}")
def fonk2():
    b3 = [5, 3, 7, 2, 4, 1, 11, 8, 10, 9, 6]
    print("Original list:", b3)
    fonk1(b3)
    print("Sorted list:", b3)
if b4 = = "__main__":
    fonk2()