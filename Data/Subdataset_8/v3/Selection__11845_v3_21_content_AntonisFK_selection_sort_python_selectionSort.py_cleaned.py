def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
if __name__ == "__main__":
    arr = [5, 3, 2, 10, 45, 3, 1]
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)