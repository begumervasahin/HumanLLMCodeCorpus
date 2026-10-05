def linear_search(target_item, search_list):
    found = False
    current_position = 0
    while current_position < len(search_list) and not found:
        if search_list[current_position] == target_item:
            found = True
        current_position += 1
    return found
if __name__ == "__main__":
    grocery_list = ["apples", "bananas", "chocolate", "pasta"]
    item_to_search = input("What item are you looking for: ")
    is_item_found = linear_search(item_to_search, grocery_list)
    if is_item_found:
        print("The item is in the grocery list!")
    else:
        print("The item is not in the grocery list.")