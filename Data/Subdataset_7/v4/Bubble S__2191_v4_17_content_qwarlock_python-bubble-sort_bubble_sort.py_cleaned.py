def fonk1(b3: list[int], a1: int) -> int:
    b1 = len(b3)
    for i in range(b1 - 1):
        b2 = False
        for j in range(b1 - i - 1):
            a1 += 1
            if b3[j] > b3[j + 1]:
                b2 = True
                b3[j], b3[j + 1] = b3[j + 1], b3[j]
        if not b2:
            break
    return a1
b3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", b3)
a1 = 0
a1 = fonk1(b3, a1)
print("Sorted list:", b3)
print("Number of comparisons:", a1)