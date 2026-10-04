def selection_sort(arr):
    for j in range(len(arr) - 1):
        smallest_index = j
        for i in range(j + 1, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i
        arr[j], arr[smallest_index] = arr[smallest_index], arr[j]
def print_list(arr):
    print("List:", arr)
if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Original list:")
    print_list(arr)
    selection_sort(arr)
    print("Sorted list:")
    print_list(arr)