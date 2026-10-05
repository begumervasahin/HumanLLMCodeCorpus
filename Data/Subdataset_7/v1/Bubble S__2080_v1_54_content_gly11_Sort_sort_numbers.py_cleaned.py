def fonk1(lists):
    b1 = len(lists)
    for j in range(1, b1):
        b2 = lists[j]
        b3 = j - 1
        while b3 >= 0 and lists[b3] > b2:
            lists[b3 + 1] = lists[b3]
            b3 -= 1
        lists[b3 + 1] = b2
    return lists
def fonk2(lists):
    b4 = len(lists)
    for b3 in range(0, b4):
        for j in range(b3 + 1, b4):
            if lists[b3] > lists[j]:
                lists[b3], lists[j] = lists[j], lists[b3]
    return lists
b5 = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", b5)
b6 = fonk1(b5.copy())
print("Sorted list (Insertion Sort):", b6)
b7 = fonk2(b5.copy())
print("Sorted list (Bubble Sort):", b7)