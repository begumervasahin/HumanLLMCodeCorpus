import time
def fonk1(nums, item):
    a1 = 0
    b1 = len(nums)-1
    b2 = False
    b3 = time.time()
    while a1 <= b1 and not b2:
        b4 = (a1 + b1)
        if nums[b4] == item:
            b2 = True;
        else:
            if item < nums[b4]:
                b1 = b4 - 1
            else:
                a1 = b4 + 1
    return b2
def fonk2(binarySearch, nums, item):
    b3 = time.perf_counter()
    b5 = fonk1(nums, item)
    b6 = time.perf_counter()
    b7 = (b6 - b3) * 100000
    return b7
if(b8 = = "__main__"):
    b9 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    b10 = int(input("What number do you want to find? "))
    b11 = fonk1(b9, b10)
    b12 = fonk2(binarySearch, b9, b10)
    if(b11):
        print("Your item is in the b9")
        print("Time to find: ", b12)
    else:
        print("Your item is not in the b9")
        print("Time spent searching: ", b12)