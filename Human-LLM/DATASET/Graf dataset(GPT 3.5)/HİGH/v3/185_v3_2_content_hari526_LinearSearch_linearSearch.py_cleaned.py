def fonk1(target_item, search_list):
    b1 = False
    a1 = 0
    while a1 < len(search_list) and not b1:
        if search_list[a1] == target_item:
            b1 = True
        else:
            a1 += 1
    return b1
if b2 = = "__main__":
    b3 = ["apples", "bananas", "chocolate", "pasta"]
    b4 = input("What item are you looking for: ")
    b5 = fonk1(b4, b3)
    if b5:
        print("The item is in the grocery list!")
    else:
        print("The item is not in the grocery list.")