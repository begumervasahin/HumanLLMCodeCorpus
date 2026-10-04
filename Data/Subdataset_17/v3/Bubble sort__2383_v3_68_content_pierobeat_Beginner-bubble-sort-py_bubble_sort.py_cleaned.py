def bubble_sort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr
if __name__ == "__main__":
    print("Already sorted list:", bubble_sort([1, 2, 3, 4, 5, 6]))
    print("Unsorted list:", bubble_sort([2, 1, 4, 3, 6, 5]))
    print("Reverse sorted list:", bubble_sort([6, 5, 4, 3, 2, 1]))
