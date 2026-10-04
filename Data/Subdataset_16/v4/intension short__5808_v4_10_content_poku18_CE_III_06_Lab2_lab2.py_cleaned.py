def fonk1(array):
    b1 = len(array)
    for index in range(1, b1):
        b2 = array[index]
        b3 = index
        while b3 > 0 and array[b3 - 1] > b2:
            array[b3] = array[b3 - 1]
            b3 -= 1
        array[b3] = b2
    return array
def fonk2(array):
    if len(array) <= 1:
        return array
    b4 = len(array)
    b5 = fonk2(array[:b4])
    b6 = fonk2(array[b4:])
    return fonk3(b5, b6)
def fonk3(left, right):
    b7 = []
    b8 = j = 0
    while b8 < len(left) and j < len(right):
        if left[b8] <= right[j]:
            b7.append(left[b8])
            b8 += 1
        else:
            b7.append(right[j])
            j += 1
    b7.extend(left[b8:])
    b7.extend(right[j:])
    return b7
if b9 = = '__main__':
    print("Enter the array items separated by space:")
    b10 = list(map(int, input().split()))
    b11 = fonk1(b10.copy())
    print("Sorted array using insertion sort is:", b11)
    b12 = fonk2(b10)
    print("Sorted array using merge sort is:", b12)