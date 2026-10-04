import sys
def merge(left, right):
    merged_list = []
    while left and right:
        if left[0] <= right[0]:
            merged_list.append(left.pop(0))
        else:
            merged_list.append(right.pop(0))
    merged_list.extend(left)
    merged_list.extend(right)
    return merged_list
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)
def main():
    if len(sys.argv) > 1:
        try:
            input_list = [int(x) for x in sys.argv[1:]]
            print("Original list:", input_list)
            sorted_list = merge_sort(input_list)
            print("Sorted list:", sorted_list)
        except ValueError:
            print("Please provide a valid list of integers.")
    else:
        print("Usage: python script.py <num1> <num2> ... <numN>")
if __name__ == "__main__":
    main()