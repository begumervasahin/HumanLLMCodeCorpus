import random
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = random.randint(0, len(arr) - 1)
    b2 = arr[b1]
    print("Pivot element:", b2, "in list:", arr)
    b3 = []
    b4 = []
    b5 = [b2]
    for b6, num in enumerate(arr):
        if b6 = = b1:
            continue
        elif num < b2:
            b3.append(num)
        elif num > b2:
            b4.append(num)
        else:
            b5.append(num)
    print("Left sublist:", b3, "; Right sublist:", b4)
    b7 = fonk1(b3)
    b8 = fonk1(b4)
    return b7 + b5 + b8
b9 = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", b9)
print("Sorted list:", fonk1(b9))