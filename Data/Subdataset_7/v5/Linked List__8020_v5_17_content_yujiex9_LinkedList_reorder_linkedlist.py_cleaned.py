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
def fonk2(b13):
    b5 = b13
    b6 = None
    while b5:
        b4 = b5.b4
        b5.b4 = b6
        b6 = b5
        b5 = b4
    return b6
def fonk3(b14):
    b7 = b12.head
    b8 = b14
    while b7.b4:
        b9 = b7.b4
        b7.b4 = b8
        b7 = b9
        b10 = b8.b4
        b8.b4 = b7
        b8 = b10
    b7.b4 = b8
if b11 = = '__main__':
    b12 = LinkedList()
    b13 = fonk1(b12)
    b14 = fonk2(b13)
    fonk3(b14)