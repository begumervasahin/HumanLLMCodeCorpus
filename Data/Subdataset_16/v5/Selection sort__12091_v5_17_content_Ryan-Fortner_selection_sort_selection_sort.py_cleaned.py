def fonk1(array):
    b1 = len(array)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if array[b2] > array[j]:
                b2 = j
        array[i], array[b2] = array[b2], array[i]
    return array
def fonk2():
    b3 = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    print("Original array:", b3)
    b4 = fonk1(b3)
    print("Sorted array:", b4)
if b5 = = "__main__":
    fonk2()