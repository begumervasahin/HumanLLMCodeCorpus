import time
def binary_search(nums, item):
    first, last = 0, len(nums) - 1
    found = False
    while first <= last and not found:
        middle = (first + last)
        if nums[middle] == item:
            found = True
        elif item < nums[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return found
def calculate_runtime(search_func, nums, item):
    start = time.perf_counter()
    result = search_func(nums, item)
    end = time.perf_counter()
    elapsed_time = (end - start) * 1_000_000
    return elapsed_time
if __name__ == "__main__":
    nums_list = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    num_to_find = int(input("Enter the number you want to find: "))
    is_found = binary_search(nums_list, num_to_find)
    time_to_find = calculate_runtime(binary_search, nums_list, num_to_find)
    if is_found:
        print("The number is in the list.")
    else:
        print("The number is not in the list.")
    print(f"Time spent searching: {time_to_find:.2f} microseconds")