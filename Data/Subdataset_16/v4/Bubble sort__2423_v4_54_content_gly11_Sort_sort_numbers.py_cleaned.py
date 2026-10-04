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
        for j in range(b3 + 1, b4):
            if lists[b3] > lists[j]:
                lists[b3], lists[j] = lists[j], lists[b3]
    return lists
if b5 = = "__main__":
    b6 = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", b6)
    print("Sorted list using insertion sort:", fonk1(b6.copy()))
    print("Sorted list using bubble sort:", fonk2(b6.copy()))