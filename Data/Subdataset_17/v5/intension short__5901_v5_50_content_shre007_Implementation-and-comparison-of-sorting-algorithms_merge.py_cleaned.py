def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    return sorted_array
def get_input_list():
    number_of_elements = int(input("Enter the number of elements: "))
    return [int(input(f"Element {i+1}: ")) for i in range(number_of_elements)]
if __name__ == "__main__":
    input_list = get_input_list()
    sorted_list = merge_sort(input_list)
    print("Sorted list:", sorted_list)