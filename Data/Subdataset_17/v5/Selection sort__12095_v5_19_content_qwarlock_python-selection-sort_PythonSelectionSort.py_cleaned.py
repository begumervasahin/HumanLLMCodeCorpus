def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
def main():
    arr = [6, 5, 8, 4, 3, 2, 8, 9, 10, 15, 0]
    print("Array before sorting:", arr)
    selection_sort(arr)
    print("Array after sorting:", arr)
if __name__ == "__main__":
    main()