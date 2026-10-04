import time
def fonk1(nums, item):
    a1 = 0
    b1 = len(nums) - 1
    b2 = False
    while a1 <= b1 and not b2:
        b3 = (a1 + b1)
        if nums[b3] == item:
            b2 = True
        else:
            if item < nums[b3]:
                b1 = b3 - 1
            else:
                a1 = b3 + 1
    return b2
def fonk2(search_function, nums, item):
    b4 = time.perf_counter()
    b5 = search_function(nums, item)
    b6 = time.perf_counter()
    b7 = (b6 - b4) * 100000
    return b7
if b8 = = "__main__":
    b9 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    b10 = int(input("What number do you want to find? "))
    b11 = fonk1(b9, b10)
    b12 = fonk2(binary_search, b9, b10)
    if b11:
        print("Your item is in the list.")
        print(f"Time to find: {b12:.2f} microseconds")
    else:
        print("Your item is not in the list.")
        print(f"Time spent searching: {b12:.2f} microseconds")