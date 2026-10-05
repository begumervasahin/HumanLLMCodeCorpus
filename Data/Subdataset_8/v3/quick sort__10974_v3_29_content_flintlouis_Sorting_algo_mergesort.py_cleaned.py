import sys
def merge(a, b):
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    c.extend(a)
    c.extend(b)
    return c
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst)
    a = lst[:mid]
    b = lst[mid:]
    a = merge_sort(a)
    b = merge_sort(b)
    return merge(a, b)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        lst = list(map(int, sys.argv[1].split()))
        print("Original list:", lst)
        sorted_list = merge_sort(lst)
        print("Sorted list:", sorted_list)
    else:
        print("Please provide a list of numbers as command line arguments.")