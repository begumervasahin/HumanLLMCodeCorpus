def find_minimal_element(arr):
    minimal_element = arr[0]
    minimal_element_index = 0
    for i in range(1, len(arr)):
        if arr[i] < minimal_element:
            minimal_element = arr[i]
            minimal_element_index = i
    return minimal_element_index
def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        minimal_element = find_minimal_element(arr)
        new_arr.append(arr.pop(minimal_element))
    return new_arr
if __name__ == "__main__":
    input_array = [5, 3, 6, 2, 10]
    sorted_array = selection_sort(input_array)
    print(sorted_array)