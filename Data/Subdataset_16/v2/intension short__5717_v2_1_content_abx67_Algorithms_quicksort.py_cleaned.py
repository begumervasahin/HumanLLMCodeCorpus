def fonk1(b4, left, right):
    b1 = b4[right]
    print(f"Pivot: {b1}")
    b2 = left
    for i in range(left, right + 1):
        print(f"Inspecting element at index {i}: {b4[i]}")
        if b4[i] <= b1:
            if i != b2:
                b4[i], b4[b2] = b4[b2], b4[i]
            b2 += 1
    return b2 - 1
def fonk2(b4, left, right):
    if left < right:
        b2 = fonk1(b4, left, right)
        print(f"Split at index {b2}: {b4}")
        fonk2(b4, left, b2 - 1)
        fonk2(b4, b2 + 1, right)
if b3 = = "__main__":
    b4 = [3, 6, 8, 10, 1, 2, 1]
    fonk2(b4, 0, len(b4) - 1)
    print("Sorted b4:", b4)