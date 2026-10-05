import time
def fonk1(item_to_find, my_list):
    b1 = False
    a1 = 0
    while a1 < len(my_list) and not b1:
        if my_list[a1] == item_to_find:
            b1 = True
        a1 += 1
    return b1
def fonk2(search_function, item, my_list):
    b2 = time.perf_counter()
    b3 = search_function(item, my_list)
    b4 = time.perf_counter()
    b5 = (b4 - b2) * 100000
    return b5
def fonk3():
    b6 = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
    b7 = int(input("What number do you want to find? "))
    b8 = fonk1(b7, b6)
    b9 = fonk2(linear_search, b7, b6)
    if b8:
        print("Your item is in the list.")
        print("Time taken to find: {:.6f} microseconds".format(b9))
    else:
        print("Your item is not in the list.")
        print("Time taken to search: {:.6f} microseconds".format(b9))
if b10 = = "__main__":
    fonk3()