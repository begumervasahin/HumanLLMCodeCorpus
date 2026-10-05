import sys
def merge(a, b):
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)
def process_and_print_sorted_list(input_str):
    input_list = input_str.split()
    input_list = [int(num) for num in input_list]
    print("Input list:", input_list)
    sorted_list = merge_sort(input_list)
    print("Sorted list:", sorted_list)
if len(sys.argv) > 1:
    process_and_print_sorted_list(sys.argv[1])