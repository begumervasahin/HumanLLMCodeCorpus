from LinkedList import Node, LinkedList
def fonk1(b12):
    b3, b1 = b12.head, b12.head
    b2 = None
    while b1 and b1.b4:
        b2 = b3
        b3 = b3.b4
        b1 = b1.b4.b4
    if b2:
        b2.b4 = None
    return b3
def fonk2(b10):
    b3 = b10
    b5 = b3.b4
    b3.b4 = None
    b2 = b3
    while b5:
        b3 = b5
        b5 = b3.b4
        b3.b4 = b2
        b2 = b3
    return b3
def fonk3(b12, b11):
    b6 = b12.head
    b7 = b11
    while b6 and b7:
        b8 = b6.b4
        b9 = b7.b4
        b6.b4 = b7
        if not b8:
            break
        b7.b4 = b8
        b6 = b8
        b7 = b9
def fonk4(b12):
    if not b12.head or not b12.head.b4:
        return
    b10 = fonk1(b12)
    b11 = fonk2(b10)
    fonk3(b12, b11)
b12 = LinkedList()
b12.add_to_end(1)
b12.add_to_end(2)
b12.add_to_end(3)
b12.add_to_end(4)
b12.add_to_end(5)
print("Original list:")
b12.display()
fonk4(b12)
print("Reordered list:")
b12.display()