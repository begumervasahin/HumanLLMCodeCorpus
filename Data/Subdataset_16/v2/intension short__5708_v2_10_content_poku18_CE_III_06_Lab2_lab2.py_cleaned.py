def fonk1(array):
    for b9 in range(1, len(array)):
        b1 = array[b9]
        b2 = b9
        while b2 > 0 and array[b2 - 1] > b1:
            array[b2] = array[b2 - 1]
            b2 -= 1
        array[b2] = b1
    return array
def fonk2(array):
    if len(array) <= 1:
        return array
    b3 = len(array)
    b4 = array[:b3]
    b5 = array[b3:]
    b6 = fonk2(b4)
    b7 = fonk2(b5)
    return fonk3(b6, b7)
def fonk3(left, right):
    b8 = []
    b9 = j = 0
    while b9 < len(left) and j < len(right):
        if left[b9] <= right[j]:
            b8.append(left[b9])
            b9 += 1
        else:
            b8.append(right[j])
            j += 1
    b8.extend(left[b9:])
    b8.extend(right[j:])
    return b8
if b10 = = '__main__':
    b11 = input("Enter the array items separated by space: ")
    b12 = list(map(int, b11.split()))
    b13 = fonk1(b12.copy())
    print("Sorted array using insertion sort is:", b13)
    b14 = fonk2(b12)
    print("Sorted array using merge sort is:", b14)