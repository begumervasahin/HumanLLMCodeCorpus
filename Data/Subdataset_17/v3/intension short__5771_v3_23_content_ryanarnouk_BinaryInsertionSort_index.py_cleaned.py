def binary_search(arr, val, start, end):
    while start <= end:
        mid = (start + end)
        if arr[mid] < val:
            start = mid + 1
        elif arr[mid] > val:
            end = mid - 1
        else:
            return mid
    return start
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        correct_position = binary_search(arr, val, 0, i - 1)
        arr = arr[:correct_position] + [val] + arr[correct_position:i] + arr[i+1:]
    return arr
if __name__ == "__main__":
    unsorted_arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    sorted_arr = insertion_sort(unsorted_arr)
    print("Sorted array:", sorted_arr)