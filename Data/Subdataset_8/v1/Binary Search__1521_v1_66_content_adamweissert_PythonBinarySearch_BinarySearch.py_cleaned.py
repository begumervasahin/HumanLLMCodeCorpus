import time
def binary_search(nums, item):
    first = 0
    last = len(nums) - 1
    found = False
    start = time.time()
    while first <= last and not found:
        middle = (first + last)
        if nums[middle] == item:
            found = True
        else:
            if item < nums[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found
def calc_runtime(binary_search_func, nums, item):
    start = time.perf_counter()
    result = binary_search_func(nums, item)
    end = time.perf_counter()
    elapsed = (end - start) * 100000
    return elapsed
if __name__ == "__main__":
    num_list = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    num_to_find = int(input("What number do you want to find? "))
    is_found = binary_search(num_list, num_to_find)
    time_to_find = calc_runtime(binary_search, num_list, num_to_find)
    if is_found:
        print("Your item is in the list")
        print("Time to find: ", time_to_find, " microseconds")
    else:
        print("Your item is not in the list")
        print("Time spent searching: ", time_to_find, " microseconds")