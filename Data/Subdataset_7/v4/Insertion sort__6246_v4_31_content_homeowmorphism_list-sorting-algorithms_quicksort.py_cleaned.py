import random
def fonk1(arr):
    b1 = len(arr)
    if b1 > 1:
        b2 = random.randint(0, b1 - 1)
        b3 = arr[b2]
        print("Pivoting", b3, "in", arr)
        b4 = []
        b5 = []
        b6 = [b3]
        for b7 in range(b1):
            if b7 = = b2:
                continue
            elif arr[b7] < b3:
                b4.append(arr[b7])
            elif arr[b7] > b3:
                b5.append(arr[b7])
            else:
                b6.append(arr[b7])
        print("Left becomes", b4, "; b5 becomes", b5)
        b8 = fonk1(b4)
        b9 = fonk1(b5)
        return b8 + b6 + b9
    return arr
b10 = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", b10)
print("Sorted list:", fonk1(b10))