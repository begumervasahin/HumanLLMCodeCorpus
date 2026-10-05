import time
def fonk1(nums, item):
    a1 = 0
    b1 = len(nums) - 1
    b2 = False
    b3 = time.time()
    while a1 <= b1 and not b2:
        b4 = (a1 + b1)
        if nums[b4] == item:
            b2 = True
        else:
            if item < nums[b4]:
                b1 = b4 - 1
            else:
                a1 = b4 + 1
    return b2, (time.time() - b3) * 100000
def fonk2(search_function, nums, item):
    b3 = time.perf_counter()
    b2, b5 = search_function(nums, item)
    b6 = time.perf_counter()
    return b2, b5, b6 - b3
if b7 = = "__main__":
    b8 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    b9 = int(input("Enter the number you want to find: "))
    is_found, time_to_find, b10 = fonk2(binary_search, b8, b9)
    if is_found:
        print("Your item is in the list.")
        print("Time to find:", time_to_find, "microseconds")
    else:
        print("Your item is not in the list.")
        print("Time spent searching:", time_to_find, "microseconds")