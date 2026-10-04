def fonk1(a, left, right):
    b1 = j = k = 0
    while b1 < len(left) and j < len(right):
        if left[b1] < right[j]:
            a[k] = left[b1]
            b1 += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while b1 < len(left):
        a[k] = left[b1]
        b1 += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
def fonk2(a):
    if len(a) > 1:
        b2 = len(a)
        b3 = a[:b2]
        b4 = a[b2:]
        fonk2(b3)
        fonk2(b4)
        fonk1(a, b3, b4)
def fonk3():
    b5 = [54, 45, 67, 12, 34, 98, 66]
    print("Array before sorting:", b5)
    fonk2(b5)
    print("Array after sorting:", b5)
if b6 = = "__main__":
    fonk3()