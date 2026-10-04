import time
def fonk1(nums, item):
    b4, b1 = 0, len(nums) - 1
    b2 = False
    while b4 <= b1 and not b2:
        b3 = (b4 + b1)
        if nums[b3] == item:
            b2 = True
        elif item < nums[b3]:
            b1 = b3 - 1
        else:
            b4 = b3 + 1
    return b2
def fonk2(search_func, nums, item):
    b5 = time.perf_counter()
    b6 = search_func(nums, item)
    b7 = time.perf_counter()
    b8 = (b7 - b5) * 1_000_000
    return b8
if b9 = = "__main__":
    b10 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    b11 = int(input("Enter the number you want to find: "))
    b12 = fonk1(b10, b11)
    b13 = fonk2(binary_search, b10, b11)
    if b12:
        print("The number is in the list.")
    else:
        print("The number is not in the list.")
    print(f"Time spent searching: {b13:.2f} microseconds")