def fonk1(array, start, end):
    b1 = array[end]
    b2 = start - 1
    for j in range(start, end):
        if array[j] <= b1:
            b2 += 1
            array[b2], array[j] = array[j], array[b2]
    array[b2 + 1], array[end] = array[end], array[b2 + 1]
    return b2 + 1
def fonk2(array, start, end):
    if start < end:
        b3 = fonk1(array, start, end)
        fonk2(array, start, b3 - 1)
        fonk2(array, b3 + 1, end)
if b4 = = '__main__':
    b5 = [3, 1, 6, 8, 0]
    fonk2(b5, 0, len(b5) - 1)
    print(b5)