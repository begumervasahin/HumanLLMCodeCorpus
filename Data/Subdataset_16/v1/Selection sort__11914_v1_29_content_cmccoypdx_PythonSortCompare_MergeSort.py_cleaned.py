def fonk1(a, l, r):
    b1 = j = n = 0
    while b1 < len(l) and j < len(r):
        if l[b1] < r[j]:
            a[n] = l[b1]
            b1 += 1
        else:
            a[n] = r[j]
            j += 1
        n += 1
    while b1 < len(l):
        a[n] = l[b1]
        b1 += 1
        n += 1
    while j < len(r):
        a[n] = r[j]
        j += 1
        n += 1
    return a
def fonk2(a):
    if len(a) > 1:
        b2 = len(a)
        b3 = a[:b2]
        b4 = a[b2:]
        fonk2(b3)
        fonk2(b4)
        fonk1(a, b3, b4)
if b5 = = "__main__":
    b6 = [54, 45, 67, 12, 34, 98, 66]
    print("Array before sorting:", b6)
    fonk2(b6)
    print("Array after sorting:", b6)