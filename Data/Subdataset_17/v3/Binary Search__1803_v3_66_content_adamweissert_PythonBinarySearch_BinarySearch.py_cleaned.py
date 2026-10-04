import time
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high)
        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
def calculate_runtime(search_func, nums, target):
    start_time = time.perf_counter()
    search_func(nums, target)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1_000_000
def main():
    nums_list = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    try:
        target_number = int(input("Enter the number you want to find: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    is_found = binary_search(nums_list, target_number)
    search_time = calculate_runtime(binary_search, nums_list, target_number)
    if is_found:
        print("The number is in the list.")
    else:
        print("The number is not in the list.")
    print(f"Time spent searching: {search_time:.2f} microseconds")
if __name__ == "__main__":
    main()