def binary_search(l, value, low=0, high=-1):
    if not l:
        return -1
    if high == -1:
        high = len(l) - 1
    if low == high:
        if l[low] == value:
            return low
        else:
            return -1
    mid = (low + high)
    if l[mid] > value:
        return binary_search(l, value, low, mid - 1)
    elif l[mid] < value:
        return binary_search(l, value, mid + 1, high)
    else:
        return mid
def binary_search_main():
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    value_to_find = 7
    result = binary_search(sorted_list, value_to_find)
    print(f"Index of {value_to_find} in the list: {result}")
if __name__ == "__main__":
    binary_search_main()