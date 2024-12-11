import random
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = random.randint(0, len(arr) - 1)
    b2 = arr[b1]
    left, right, b3 = [], [], [b2]
    for b4, val in enumerate(arr):
        if b4 = = b1:
            continue
        if val < b2:
            left.append(val)
        elif val > b2:
            right.append(val)
        else:
            b3.append(val)
    b5 = fonk1(left)
    b6 = fonk1(right)
    return b5 + b3 + b6
b7 = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", b7)
print("Sorted list:", fonk1(b7))