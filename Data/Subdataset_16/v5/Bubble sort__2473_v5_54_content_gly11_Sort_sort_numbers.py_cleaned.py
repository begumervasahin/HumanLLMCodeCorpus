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
    for b3 in range(b4):
        for j in range(0, b4 - b3 - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
if b5 = = "__main__":
    b6 = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", b6)
    print("Sorted list using insertion sort:", fonk1(b6.copy()))
    print("Sorted list using bubble sort:", fonk2(b6.copy()))