import time
def fonk1(target, lst):
    b1 = False
    for b2 in lst:
        if b2 = = target:
            b1 = True
            break
    return b1
def fonk2(search_function, target, lst):
    b3 = time.perf_counter()
    b4 = search_function(target, lst)
    b5 = time.perf_counter()
    b6 = (b5 - b3) * 100000
    return b6
if b7 = = "__main__":
    b8 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    b9 = int(input("What b2 do you want to find? "))
    b10 = fonk1(b9, b8)
    b11 = fonk2(linear_search, b9, b8)
    if b10:
        print("Your item is in the list")
    else:
        print("Your item is not in the list")
    print("Time to find: ", b11)