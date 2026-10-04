def bubsort(a):
    for i in range(len(a)):
        for x in range(0, len(a) - 1):
            if a[x] > a[x + 1]:
                a[x + 1], a[x] = a[x], a[x + 1]
    return a
def mergesort(a):
    if len(a) > 1:
        mid = len(a)
        left = a[:mid]
        right = a[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        print('Left:', left, 'Right:', right)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        print('Merged:', a)
if __name__ == "__main__":
    array1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array for bubble sort:", array1)
    sorted_array1 = bubsort(array1[:])
    print("Sorted array with bubble sort:", sorted_array1)
    array2 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array for merge sort:", array2)
    mergesort(array2)
    print("Sorted array with merge sort:", array2)