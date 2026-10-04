
b1 = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
def fonk1(array):
    for i in range(len(array)):
        b2 = i
        for j in range(i + 1, len(array)):
            if array[b2] > array[j]:
                b2 = j
        array[i], array[b2] = array[b2], array[i]
    return array
b3 = fonk1(b1)
print("Sorted array:", b3)