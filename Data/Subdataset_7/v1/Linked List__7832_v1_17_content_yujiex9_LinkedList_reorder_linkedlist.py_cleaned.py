from LinkedList import Node, LinkedList
def fonk1(b10):
    b3, b1 = b10.head, b10.head
    while b1 and b1.b4:
        b2 = b3
        b3 = b3.b4
        b1 = b1.b4.b4
    b2.b4 = None
    return b3
def fonk2(b11):
    b3 = b11
    b5 = b3.b4
    b3.b4 = None
    b2 = b3
    b3 = b5
    while b3.b4:
        b5 = b3.b4
        b3.b4 = b2
        b2 = b3
        b3 = b5
    b3.b4 = b2
    return b3
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
    b10.printList()