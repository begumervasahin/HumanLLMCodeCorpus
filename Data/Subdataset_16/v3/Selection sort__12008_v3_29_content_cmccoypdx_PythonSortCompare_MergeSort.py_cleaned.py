def fonk1(b5, left, right):
    b1 = j = k = 0
    while b1 < len(left) and j < len(right):
        if left[b1] < right[j]:
            b5[k] = left[b1]
            b1 += 1
        else:
            b5[k] = right[j]
            j += 1
        k += 1
    while b1 < len(left):
        b5[k] = left[b1]
        b1 += 1
        k += 1
    while j < len(right):
        b5[k] = right[j]
        j += 1
        k += 1
def fonk2(b5):
    if len(b5) > 1:
        b2 = len(b5)
        b3 = b5[:b2]
        b4 = b5[b2:]
        fonk2(b3)
        fonk2(b4)
        fonk1(b5, b3, b4)
def fonk3():
    b5 = [54, 45, 67, 12, 34, 98, 66]
    print("Array before sorting:", b5)
    fonk2(b5)
    print("Array after sorting:", b5)
if b6 = = "__main__":
    fonk3()