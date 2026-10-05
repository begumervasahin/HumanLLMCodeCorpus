def fonk1(lst):
    b1 = len(lst)
    for j in range(1, b1):
        b2 = lst[j]
        b3 = j - 1
        while b3 >= 0 and lst[b3] > b2:
            lst[b3 + 1] = lst[b3]
            b3 -= 1
        lst[b3 + 1] = b2
    return lst
def fonk2(lst):
    b4 = len(lst)
    for b3 in range(0, b4):
        for j in range(b3 + 1, b4):
            if lst[b3] > lst[j]:
                lst[b3], lst[j] = lst[j], lst[b3]
    return lst
b5 = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", b5)
b6 = fonk1(b5.copy())
print("Sorted list (Insertion Sort):", b6)
b7 = fonk2(b5.copy())
print("Sorted list (Bubble Sort):", b7)