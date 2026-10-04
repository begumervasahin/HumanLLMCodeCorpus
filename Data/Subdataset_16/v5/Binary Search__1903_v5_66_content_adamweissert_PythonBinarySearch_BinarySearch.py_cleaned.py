import time
def fonk1(nums, item):
    a1 = 0
    b1 = len(nums) - 1
    while a1 <= b1:
        b2 = (a1 + b1)
        if nums[b2] == item:
            return True
        elif item < nums[b2]:
            b1 = b2 - 1
        else:
            a1 = b2 + 1
    return False
def fonk2(search_function, nums, item):
    b3 = time.perf_counter()
    b4 = search_function(nums, item)
    b5 = time.perf_counter()
    b6 = (b5 - b3) * 1_000_000
    return b6, b4
if b7 = = "__main__":
    b8 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    b9 = int(input("What number do you want to find? "))
    time_to_find, b10 = fonk2(binary_search, b8, b9)
    if b10:
        print("Your item is in the list.")
    else:
        print("Your item is not in the list.")
    print(f"Time spent searching: {time_to_find:.2f} microseconds")