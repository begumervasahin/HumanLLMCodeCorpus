def binary_search(arr: list, value: any, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(arr) - 1
    while low <= high:
        mid = (low + high)
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1
def main() -> None:
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    value_to_find = 7
    result = binary_search(sorted_list, value_to_find)
    print(f"Index of {value_to_find} in the list: {result}")
if __name__ == "__main__":
    main()