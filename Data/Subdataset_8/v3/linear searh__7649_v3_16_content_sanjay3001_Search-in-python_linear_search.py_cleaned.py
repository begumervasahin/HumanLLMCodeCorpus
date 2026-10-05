def linear_search(elements_list, item_to_find):
    iteration_count = 0
    found = False
    for position, element in enumerate(elements_list):
        iteration_count += 1
        if element == item_to_find:
            found = True
            print("Found")
            break
    return iteration_count, found
def main():
    num_elements = int(input("Enter the number of elements: "))
    elements_list = [input("Enter element {}: ".format(i + 1)) for i in range(num_elements)]
    print("THE LIST IS", elements_list)
    item_to_find = input("Enter the item to find: ")
    iteration_count, found = linear_search(elements_list, item_to_find)
    print("Number of iterations:", iteration_count)
    if not found:
        print("Item not found.")
if __name__ == "__main__":
    main()