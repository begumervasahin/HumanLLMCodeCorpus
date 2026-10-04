def fonk1(b10):
    for b7 in range(1, len(b10)):
        b1 = b10[b7]
        b2 = b7 - 1
        while b2 >= 0 and b10[b2] > b1:
            b10[b2 + 1] = b10[b2]
            b2 -= 1
        b10[b2 + 1] = b1
    return b10
def fonk2(b10):
    if len(b10) <= 1:
        return b10
    b3 = len(b10)
    b4 = fonk2(b10[:b3])
    b5 = fonk2(b10[b3:])
    return fonk3(b4, b5)
def fonk3(left, right):
    b6 = []
    b7 = b2 = 0
    while b7 < len(left) and b2 < len(right):
        if left[b7] <= right[b2]:
            b6.append(left[b7])
            b7 += 1
        else:
            b6.append(right[b2])
            b2 += 1
    b6.extend(left[b7:])
    b6.extend(right[b2:])
    return b6
if b8 = = '__main__':
    b9 = input("Enter the b10 items separated by space:\n")
    b10 = list(map(int, b9.split()))
    b11 = fonk1(b10.copy())
    print("Sorted b10 using insertion sort:", b11)
    b12 = fonk2(b10)
    print("Sorted b10 using merge sort:", b12)