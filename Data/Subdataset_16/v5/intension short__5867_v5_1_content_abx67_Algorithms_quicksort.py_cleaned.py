def fonk1(b4, left, right):
    b1 = b4[right]
    b2 = left
    print(f"Pivot: {b1}")
    for i in range(left, right + 1):
        print(f"Index: {i}")
        if b4[i] <= b1:
            b4[i], b4[b2] = b4[b2], b4[i]
            b2 += 1
    return b2 - 1
def fonk2(b4, left, right):
    if left < right:
        b2 = fonk1(b4, left, right)
        print(f"Split index: {b2}, Left: {left}, Right: {right}")
        print(f"Array after partition: {b4}")
        fonk2(b4, left, b2 - 1)
        fonk2(b4, b2 + 1, right)
if b3 = = "__main__":
    b4 = [3, 6, 8, 10, 1, 2, 1]
    fonk2(b4, 0, len(b4) - 1)
    print(f"Sorted array: {b4}")