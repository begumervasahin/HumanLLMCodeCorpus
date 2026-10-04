import sys
def merge(left, right):
    merged_list = []
    while left and right:
        if left[0] > right[0]:
            merged_list.append(right.pop(0))
        else:
            merged_list.append(left.pop(0))
    while left:
        merged_list.append(left.pop(0))
    while right:
        merged_list.append(right.pop(0))
    return merged_list
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)
    left_half = lst[:mid]
    right_half = lst[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)
def main():
    if len(sys.argv) > 1:
        input_list = sys.argv[1:]
        input_list = [int(x) for x in input_list]
        print("Original list:", input_list)
        sorted_list = merge_sort(input_list)
        print("Sorted list:", sorted_list)
    else:
        print("Please provide a list of numbers as command-line arguments.")
if __name__ == "__main__":
    main()