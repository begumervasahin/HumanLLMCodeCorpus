def fonk1(my_item, my_list):
    b1 = False
    a1 = 0
    while a1 < len(my_list) and not b1:
        if my_list[a1] == my_item:
            b1 = True
        a1 += 1
    return b1
if b2 = = "__main__":
    b3 = ["apples", "bananas", "chocolate", "pasta"]
    b4 = input("What b4 do you want to search: ")
    b5 = fonk1(b4, b3)
    if b5:
        print("Item is in the list!")
    else:
        print("Item is not in the list!")