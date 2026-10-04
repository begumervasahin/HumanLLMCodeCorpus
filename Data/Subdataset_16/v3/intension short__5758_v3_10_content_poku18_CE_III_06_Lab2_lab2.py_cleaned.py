def fonk1(array):
    for b7 in range(1, len(array)):
        b1 = array[b7]
        b2 = b7
        while b2 > 0 and array[b2 - 1] > b1:
            array[b2] = array[b2 - 1]
            b2 -= 1
        array[b2] = b1
    return array
def fonk2(array):
    if len(array) <= 1:
        return array
    b3 = len(array)
    b4 = fonk2(array[:b3])
    b5 = fonk2(array[b3:])
    return fonk3(b4, b5)
def fonk3(left, right):
    b6 = []
    b7 = j = 0
    while b7 < len(left) and j < len(right):
        if left[b7] <= right[j]:
            b6.append(left[b7])
            b7 += 1
        else:
            b6.append(right[j])
            j += 1
    b6.extend(left[b7:])
    b6.extend(right[j:])
    return b6
if b8 = = '__main__':
    b9 = input("Enter the array items separated by space: ")
    b10 = list(map(int, b9.split()))
    b11 = fonk1(b10.copy())
    print("Sorted array using insertion sort:", b11)
    b12 = fonk2(b10)
    print("Sorted array using merge sort:", b12)