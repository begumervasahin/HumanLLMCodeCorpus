def quickSort(arr, left, right):
    if left < right:
        pivot = arr[left]
        s = left
        for i in range(left + 1, right):
            if arr[i] < pivot:
                s += 1
                arr[s], arr[i] = arr[i], arr[s]
        arr[left], arr[s] = arr[s], arr[left]
        quickSort(arr, left, s)
        quickSort(arr, s + 1, right)
def main():
    array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("Original array:", array)
    quickSort(array, 0, len(array))
    print("Sorted array:", array)
if __name__ == "__main__":
    main()