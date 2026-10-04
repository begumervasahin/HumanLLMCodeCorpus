import time
def binary_search(nums, item):
    first = 0
    last = len(nums) - 1
    while first <= last:
        middle = (first + last)
        if nums[middle] == item:
            return True
        elif item < nums[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False
def calc_runtime(search_function, nums, item):
    start = time.perf_counter()
    result = search_function(nums, item)
    end = time.perf_counter()
    elapsed_time = (end - start) * 1_000_000
    return elapsed_time, result
if __name__ == "__main__":
    num_list = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    num_to_find = int(input("What number do you want to find? "))
    time_to_find, is_it_found = calc_runtime(binary_search, num_list, num_to_find)
    if is_it_found:
        print("Your item is in the list.")
    else:
        print("Your item is not in the list.")
    print(f"Time spent searching: {time_to_find:.2f} microseconds")