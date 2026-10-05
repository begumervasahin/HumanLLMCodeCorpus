def merge_sort(given_list):
    if len(given_list) <= 1:
        return given_list
    mid = len(given_list)
    left_list = given_list[:mid]
    right_list = given_list[mid:]
    merge_sort(left_list)
    merge_sort(right_list)
    merge(left_list, right_list, given_list)
def merge(left, right, merged):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1
number_of_elements = int(input("How many elements do you want in this list: "))
given_list = [int(input("Enter element: ")) for _ in range(number_of_elements)]
merge_sort(given_list)
print("Sorted list:", given_list)