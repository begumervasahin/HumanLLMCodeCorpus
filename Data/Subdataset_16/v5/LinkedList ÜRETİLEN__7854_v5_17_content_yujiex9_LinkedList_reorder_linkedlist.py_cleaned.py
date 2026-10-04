from LinkedList import Node, LinkedList
def fonk1(b13):
    b1 = b13.head
    b2 = b13.head
    b3 = None
    while b2 and b2.b4:
        b3 = b1
        b1 = b1.b4
        b2 = b2.b4.b4
    if b3:
        b3.b4 = None
    return b1
def fonk2(head):
    b5 = None
    b6 = head
    while b6:
        b4 = b6.b4
        b6.b4 = b5
        b5 = b6
        b6 = b4
    return b5
def fonk3(b13, b12):
    b7 = b13.head
    b8 = b12
    while b7 and b8:
        b9 = b7.b4
        b10 = b8.b4
        b7.b4 = b8
        if not b9:
            break
        b8.b4 = b9
        b7 = b9
        b8 = b10
def fonk4(b13):
    if not b13.head or not b13.head.b4:
        return
    b11 = fonk1(b13)
    b12 = fonk2(b11)
    fonk3(b13, b12)
b13 = LinkedList()
b13.add_to_end(1)
b13.add_to_end(2)
b13.add_to_end(3)
b13.add_to_end(4)
b13.add_to_end(5)
print("Original list:")
b13.display()
fonk4(b13)
print("Reordered list:")
b13.display()