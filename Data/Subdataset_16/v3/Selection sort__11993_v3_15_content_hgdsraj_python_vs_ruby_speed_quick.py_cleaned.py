def fonk1(array):
    b1 = len(array)
    for i in range(b1):
        for j in range(b1 - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
b2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
b3 = fonk1(b2)
print("Sorted array:")
print(b3)