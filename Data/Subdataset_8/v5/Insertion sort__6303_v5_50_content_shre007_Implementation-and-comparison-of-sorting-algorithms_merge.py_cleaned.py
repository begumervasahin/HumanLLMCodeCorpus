def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)
    left_list = arr[:mid]
    right_list = arr[mid:]
    merge_sort(left_list)
    merge_sort(right_list)
    merge(left_list, right_list, arr)
def merge(left_list, right_list, arr):
    i = j = k = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            arr[k] = left_list[i]
            i += 1
        else:
            arr[k] = right_list[j]
            j += 1
        k += 1
    while i < len(left_list):
        arr[k] = left_list[i]
        i += 1
        k += 1
    while j < len(right_list):
        arr[k] = right_list[j]
        j += 1
        k += 1
number_of_elements = int(input("How many elements do you want in this list: "))
given_list = [int(input("Enter element: ")) for _ in range(number_of_elements)]
merge_sort(given_list)
print("Sorted list:", given_list)