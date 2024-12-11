import random
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = random.randint(0, len(arr) - 1)
    b2 = arr[b1]
    print("Pivoting", b2, "in", arr)
    b3 = []
    b4 = []
    b5 = [b2]
    for b6 in range(len(arr)):
        if b6 = = b1:
            continue
        elif arr[b6] < b2:
            b3.append(arr[b6])
        elif arr[b6] > b2:
            b4.append(arr[b6])
        else:
            b5.append(arr[b6])
    print("Left becomes", b3, "; b4 becomes", b4)
    b7 = fonk1(b3)
    b8 = fonk1(b4)
    return b7 + b5 + b8
b9 = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", b9)
print("Sorted list:", fonk1(b9))