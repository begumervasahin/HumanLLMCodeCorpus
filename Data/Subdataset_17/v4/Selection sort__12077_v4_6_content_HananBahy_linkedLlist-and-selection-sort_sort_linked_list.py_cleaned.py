from linkedlistuno import LinkedListUno
def main():
    my_list = LinkedListUno()
    elements = [100, 500, 70, 1, -1, 8, 40, 70, 5, -1]
    for element in elements:
        my_list.add(element)
    print("Linked list before sorting:")
    my_list.print_linked()
    my_list.selection_sort()
    print("Linked list after sorting:")
    my_list.print_linked()
if __name__ == "__main__":
    main()