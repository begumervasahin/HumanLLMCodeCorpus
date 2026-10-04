def selection_sort(arr):
    n = len(arr)
    for last_pos in range(n - 1, 0, -1):
        largest_pos = 0
        for pos in range(1, last_pos + 1):
            if arr[pos] > arr[largest_pos]:
                largest_pos = pos
        arr[last_pos], arr[largest_pos] = arr[largest_pos], arr[last_pos]
def main():
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Array before sorting:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
if __name__ == "__main__":
    main()