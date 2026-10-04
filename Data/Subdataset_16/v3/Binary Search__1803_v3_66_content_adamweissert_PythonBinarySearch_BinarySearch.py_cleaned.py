import time
def fonk1(nums, target):
    b3, b1 = 0, len(nums) - 1
    while b3 <= b1:
        b2 = (b3 + b1)
        if nums[b2] == target:
            return True
        elif target < nums[b2]:
            b1 = b2 - 1
        else:
            b3 = b2 + 1
    return False
def fonk2(search_func, nums, target):
    b4 = time.perf_counter()
    search_func(nums, target)
    b5 = time.perf_counter()
    return (b5 - b4) * 1_000_000
def fonk3():
    b6 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    try:
        b7 = int(input("Enter the number you want to find: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    b8 = fonk1(b6, b7)
    b9 = fonk2(binary_search, b6, b7)
    if b8:
        print("The number is in the list.")
    else:
        print("The number is not in the list.")
    print(f"Time spent searching: {b9:.2f} microseconds")
if b10 = = "__main__":
    fonk3()