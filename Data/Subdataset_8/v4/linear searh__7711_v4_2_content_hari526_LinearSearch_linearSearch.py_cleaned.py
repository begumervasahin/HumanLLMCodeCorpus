def linear_search(target_item, item_list):
    found = False
    position = 0
    while position < len(item_list) and not found:
        if item_list[position] == target_item:
            found = True
        position = position + 1
    return found
if __name__ == "__main__":
    shopping_list = ["apples", "bananas", "chocolate", "pasta"]
    target_item = input("What item do you want to search: ")
    is_item_found = linear_search(target_item, shopping_list)
    if is_item_found:
        print("Item is in the list!")
    else:
        print("Item is not in the list!")