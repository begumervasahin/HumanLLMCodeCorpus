from LinkedList import Node, LinkedList
def fonk1(linked_list):
    b1 = linked_list.head
    b2 = linked_list.head
    while b2 and b2.b5:
        b1 = b1.b5
        b2 = b2.b5.b5
    return b1
def fonk2(b11):
    b3 = b11
    b4 = None
    while b3:
        b5 = b3.b5
        b3.b5 = b4
        b4 = b3
        b3 = b5
    return b4
def fonk3(b12):
    b6 = b10.head
    b7 = b12
    while b6 and b7:
        b8 = b6.b5
        b6.b5 = b7
        b6 = b8
        if b6:
            b8 = b7.b5
            b7.b5 = b6
            b7 = b8
if b9 = = "__main__":
    b10 = LinkedList()
    b10.append(1)
    b10.append(2)
    b10.append(3)
    b10.append(4)
    b10.append(5)
    b11 = fonk1(b10)
    b12 = fonk2(b11)
    fonk3(b12)
    b10.print_list()