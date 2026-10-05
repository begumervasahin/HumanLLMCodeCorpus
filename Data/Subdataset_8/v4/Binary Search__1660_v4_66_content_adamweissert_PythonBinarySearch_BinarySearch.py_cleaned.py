import time
def binary_search(nums, item):
    first = 0
    last = len(nums) - 1
    found = False
    start_time = time.time()
    while first <= last and not found:
        middle = (first + last)
        if nums[middle] == item:
            found = True
        else:
            if item < nums[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found, (time.time() - start_time) * 100000
def calculate_runtime(search_function, nums, item):
    start_time = time.perf_counter()
    found, elapsed_time = search_function(nums, item)
    end_time = time.perf_counter()
    return found, elapsed_time, end_time - start_time
if __name__ == "__main__":
    number_list = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    number_to_find = int(input("Enter the number you want to find: "))
    is_found, time_to_find, total_time = calculate_runtime(binary_search, number_list, number_to_find)
    if is_found:
        print("Your item is in the list.")
        print("Time to find:", time_to_find, "microseconds")
    else:
        print("Your item is not in the list.")
        print("Time spent searching:", time_to_find, "microseconds")