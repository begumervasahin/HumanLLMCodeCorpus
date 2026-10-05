def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
if __name__ == "__main__":
    arr = [9, 8, 6, 6, 5, 4, 3, 2, 1, 0]
    bubble_sort(arr)
    print(arr)