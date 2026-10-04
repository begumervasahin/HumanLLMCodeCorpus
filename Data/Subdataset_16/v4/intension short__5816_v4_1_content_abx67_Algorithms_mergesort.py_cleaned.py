def fonk1(array, left, b5, right):
    b1 = array[left:b5+1]
    b2 = array[b5+1:right+1]
    b3 = j = 0
    b4 = left
    while b3 < len(b1) and j < len(b2):
        if b1[b3] <= b2[j]:
            array[b4] = b1[b3]
            b3 += 1
        else:
            array[b4] = b2[j]
            j += 1
        b4 += 1
    while b3 < len(b1):
        array[b4] = b1[b3]
        b3 += 1
        b4 += 1
    while j < len(b2):
        array[b4] = b2[j]
        j += 1
        b4 += 1
def fonk2(array, left, right):
    if left < right:
        b5 = left + (right - left)
        fonk2(array, left, b5)
        fonk2(array, b5 + 1, right)
        fonk1(array, left, b5, right)