def find_minimal_element(arr):
    minimal_element_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[minimal_element_index]:
            minimal_element_index = i
    return minimal_element_index
def selection_sort(arr):
    sorted_arr = []
    while arr:
        minimal_element_index = find_minimal_element(arr)
        sorted_arr.append(arr.pop(minimal_element_index))
    return sorted_arr
def main():
    unsorted_list = [5, 3, 6, 2, 10]
    print("Unsorted list:", unsorted_list)
    sorted_list = selection_sort(unsorted_list.copy())
    print("Sorted list:", sorted_list)
if __name__ == "__main__":
    main()