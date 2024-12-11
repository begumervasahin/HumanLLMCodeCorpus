from LinkedList import Node, LinkedList
def fonk1(linked_list):
    b1 = linked_list.head
    b2 = linked_list.head
    while b2 and b2.b4:
        b3 = b1
        b1 = b1.b4
        b2 = b2.b4.b4
    b3.b4 = None
    return b1
def fonk2(b11):
    b1 = b11
    b5 = b1.b4
    b1.b4 = None
    b3 = b1
    b1 = b5
    while b1.b4:
        b5 = b1.b4
        b1.b4 = b3
        b3 = b1
        b1 = b5
    b1.b4 = b3
    return b1
def fonk3(b12):
    b6 = b10.head
    b7 = b12
    while b6.b4:
        b8 = b6.b4
        b6.b4 = b7
        b6 = b8
        b8 = b7.b4
        b7.b4 = b6
        b7 = b8
    b6.b4 = b7
if b9 = = '__main__':
    b10 = LinkedList()
    b11 = fonk1(b10)
    b12 = fonk2(b11)
    fonk3(b12)