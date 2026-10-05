
from linkedList_CISC121 import createList, printList, getLength
def fonk1(b3, b4):
    b1 = b3
    while b1 is not None:
        if b1['data'] == b4:
            return True
        b1 = b1['next']
    return False
def fonk2(b3):
    if b3 is None:
        return None, None
    b2 = b3
    b3 = b3['next']
    return b2['data'], b3
def fonk3(b3, index):
    if b3 is None or index >= getLength(b3):
        return None
    b1 = b3
    for i in range(index):
        b1 = b1['next']
    return b1['data']
def fonk4(b3):
    if b3 is None:
        return None, None
    if b3['next'] is None:
        return b3['data'], None
    if getLength(b3) == 2:
        b4 = b3['next']['data']
        b3['next'] = None
        return b4, b3
    b1 = b3
    for i in range(getLength(b3)-2):
        b1 = b1['next']
    b5 = b1['next']['data']
    b1['next'] = None
    return b5, b3
def fonk5(b6):
    if b6 = = 0:
        return 0
    return b6 + fonk5(b6-1)
def fonk6(binary_string):
    if len(binary_string) == 1:
        return int(binary_string[0])
    b7 = int(binary_string[0])
    b8 = binary_string[1:]
    return 2**(len(b8)) * b7 + fonk6(b8)
if b9 = = "__main__":
    b3 = createList([1, 2, 3, 4, 5])
    print("Linked List:")
    printList(b3)
    print("Is 3 in the linked list?", fonk1(b3, 3))
    print("Is 6 in the linked list?", fonk1(b3, 6))
    popped_value, b3 = fonk2(b3)
    print("Popped b4 from the linked list:", popped_value)
    print("Linked List after popping first element:")
    printList(b3)
    print("Element at index 2 in the linked list:", fonk3(b3, 2))
    popped_value, b3 = fonk4(b3)
    print("Popped b4 from the end of the linked list:", popped_value)
    print("Linked List after popping last element:")
    printList(b3)
    print("Sum of sequence from 0 to 5:", fonk5(5))
    b10 = "1011"
    print("Decimal representation of binary number", b10, "is:", fonk6(b10))