def fonk1(array, low, high):
    b1 = array[high]
    b2 = low - 1
    for j in range(low, high):
        if array[j] <= b1:
            b2 += 1
            array[b2], array[j] = array[j], array[b2]
    array[b2 + 1], array[high] = array[high], array[b2 + 1]
    return b2 + 1
def fonk2(array, low, high):
    if low < high:
        b3 = fonk1(array, low, high)
        fonk2(array, low, b3 - 1)
        fonk2(array, b3 + 1, high)
def fonk3():
    b4 = [3, 1, 6, 8, 0]
    print("Original array:", b4)
    fonk2(b4, 0, len(b4) - 1)
    print("Sorted array:", b4)
if b5 = = '__main__':
    fonk3()