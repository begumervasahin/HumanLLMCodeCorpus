def fonk1(array, low, high):
    b1 = (low - 1)
    b2 = array[high]
    for j in range(low, high):
        if array[j] <= b2:
            b1 = b1 + 1
            array[b1], array[j] = array[j], array[b1]
    array[b1 + 1], array[high] = array[high], array[b1 + 1]
    return (b1 + 1)
def fonk2(array, low, high):
    if low < high:
        b3 = fonk1(array, low, high)
        fonk2(array, low, b3 - 1)
        fonk2(array, b3 + 1, high)
if b4 = = '__main__':
    b5 = [3, 1, 6, 8, 0]
    fonk2(b5, 0, len(b5) - 1)
    print("Sorted array:", b5)