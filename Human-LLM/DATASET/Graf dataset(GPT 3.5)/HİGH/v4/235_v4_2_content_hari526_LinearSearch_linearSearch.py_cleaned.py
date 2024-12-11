def fonk1(b4, item_list):
    b1 = False
    a1 = 0
    while a1 < len(item_list) and not b1:
        if item_list[a1] == b4:
            b1 = True
        a1 = a1 + 1
    return b1
if b2 = = "__main__":
    b3 = ["apples", "bananas", "chocolate", "pasta"]
    b4 = input("What item do you want to search: ")
    b5 = fonk1(b4, b3)
    if b5:
        print("Item is in the list!")
    else:
        print("Item is not in the list!")