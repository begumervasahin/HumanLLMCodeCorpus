def binary_search(arr: list, value: any, low: int = 0, high: int = -1) -> int:
    if not arr:
        return -1
    if high == -1:
        high = len(arr) - 1
    if low == high:
        return low if arr[low] == value else -1
    mid = (low + high)
    if arr[mid] > value:
        return binary_search(arr, value, low, mid - 1)
    elif arr[mid] < value:
        return binary_search(arr, value, mid + 1, high)
    else:
        return mid
def main() -> None:
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    value_to_find = 7
    result = binary_search(sorted_list, value_to_find)
    print(f"Index of {value_to_find} in the list: {result}")
if __name__ == "__main__":
    main()