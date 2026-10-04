def fonk1(b7, left, b5, right):
    b1 = b7[left:b5 + 1]
    b2 = b7[b5 + 1:right + 1]
    left_index, b3 = 0, 0
    b4 = left
    while left_index < len(b1) and b3 < len(b2):
        if b1[left_index] <= b2[b3]:
            b7[b4] = b1[left_index]
            left_index += 1
        else:
            b7[b4] = b2[b3]
            b3 += 1
        b4 += 1
    while left_index < len(b1):
        b7[b4] = b1[left_index]
        left_index += 1
        b4 += 1
    while b3 < len(b2):
        b7[b4] = b2[b3]
        b3 += 1
        b4 += 1
def fonk2(b7, left, right):
    if left < right:
        b5 = left + (right - left)
        fonk2(b7, left, b5)
        fonk2(b7, b5 + 1, right)
        fonk1(b7, left, b5, right)
if b6 = = "__main__":
    b7 = [12, 11, 13, 5, 6, 7]
    print("Original array:", b7)
    fonk2(b7, 0, len(b7) - 1)
    print("Sorted array:", b7)