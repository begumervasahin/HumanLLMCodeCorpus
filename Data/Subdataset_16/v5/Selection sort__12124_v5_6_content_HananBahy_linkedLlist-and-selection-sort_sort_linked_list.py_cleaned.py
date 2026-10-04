from linkedlistuno import LinkedListUno
def fonk1():
    b1 = LinkedListUno()
    b2 = [100, 500, 70, 1, -1, 8, 40, 70, 5, -1]
    for element in b2:
        b1.add(element)
    print("Linked list before sorting:")
    b1.print_linked()
    b1.selection_sort()
    print("Linked list after sorting:")
    b1.print_linked()
if b3 = = "__main__":
    fonk1()