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
    for b3 in range(b4):
        for j in range(0, b4 - b3 - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists
if b5 = = "__main__":
    b6 = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:")
    print(b6)
    b7 = fonk1(b6.copy())
    print("\nSorted list using insertion sort:")
    print(b7)
    b8 = fonk2(b6.copy())
    print("\nSorted list using bubble sort:")
    print(b8)