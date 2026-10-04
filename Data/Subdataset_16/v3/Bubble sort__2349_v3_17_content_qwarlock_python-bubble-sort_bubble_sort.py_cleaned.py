def fonk1(lst):
    b1 = len(lst)
    a1 = 0
    for i in range(b1 - 1):
        b2 = False
        for j in range(b1 - 1 - i):
            a1 += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                b2 = True
        if not b2:
            break
    return a1
b3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", b3)
b4 = fonk1(b3)
print("Sorted list:", b3)
print("Number of b4:", b4)