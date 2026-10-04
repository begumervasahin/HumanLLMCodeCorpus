def fonk1(array, left, b4, right):
    b1 = array[left:b4 + 1]
    b2 = array[b4 + 1:right + 1]
    i, j, b3 = 0, 0, left
    while i < len(b1) and j < len(b2):
        if b1[i] <= b2[j]:
            array[b3] = b1[i]
            i += 1
        else:
            array[b3] = b2[j]
            j += 1
        b3 += 1
    array[b3:right + 1] = b1[i:] + b2[j:]
def fonk2(array, left, right):
    if left < right:
        b4 = (left + right)
        fonk2(array, left, b4)
        fonk2(array, b4 + 1, right)
        fonk1(array, left, b4, right)