import time
def fonk1(target, lst):
    b1 = False
    a1 = 0
    while a1 < len(lst) and not b1:
        if lst[a1] == target:
            b1 = True
        a1 += 1
    return b1
def fonk2(search_function, target, lst):
    b2 = time.perf_counter()
    b3 = search_function(target, lst)
    b4 = time.perf_counter()
    b5 = (b4 - b2) * 100000
    return b5
if b6 = = "__main__":
    b7 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    b8 = int(input("What number do you want to find? "))
    b9 = fonk1(b8, b7)
    b10 = fonk2(linear_search, b8, b7)
    if b9:
        print("Your item is in the list")
        print("Time to find: ", b10)
    else:
        print("Your item is not in the list")
        print("Time to find: ", b10)