def fonk1(array):
    for b7 in range(1, len(array)):
        b1 = array[b7]
        b2 = b7 - 1
        while b2 >= 0 and array[b2] > b1:
            array[b2 + 1] = array[b2]
            b2 -= 1
        array[b2 + 1] = b1
    return array
def fonk2(array):
    if len(array) <= 1:
        return array
    b3 = len(array)
    b4 = array[:b3]
    b5 = array[b3:]
    b4 = fonk2(b4)
    b5 = fonk2(b5)
    return fonk3(b4, b5)
def fonk3(left, right):
    b6 = []
    b7 = b2 = 0
    while b7 < len(left) and b2 < len(right):
        if left[b7] <= right[b2]:
            b6.append(left[b7])
            b7 += 1
        else:
            b6.append(right[b2])
            b2 += 1
    b6.extend(left[b7:])
    b6.extend(right[b2:])
    return b6
if b8 = = '__main__':
    print("Enter the array items separated by space:")
    b9 = list(map(int, input().split()))
    b10 = fonk1(b9.copy())
    b11 = fonk2(b9.copy())
    print("Sorted array using insertion sort:", b10)
    print("Sorted array using merge sort:", b11)