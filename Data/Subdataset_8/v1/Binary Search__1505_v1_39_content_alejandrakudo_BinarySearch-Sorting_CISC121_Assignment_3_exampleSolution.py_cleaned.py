
from linkedList_CISC121 import createList, printList, getLength
def isInList(aLinkedList, value):
    found = False
    aPtr = aLinkedList
    while aPtr is not None:
        if aPtr['data'] == value:
            found = True
            break
        aPtr = aPtr['next']
    return found
def popFirst(aLinkedList):
    if aLinkedList is None:
        return None, None
    ref = aLinkedList
    aLinkedList = aLinkedList['next']
    return ref['data'], aLinkedList
def getElement(aLinkedList, ind):
    if aLinkedList is None or ind >= getLength(aLinkedList):
        return None
    ptr = aLinkedList
    for i in range(ind):
        ptr = ptr['next']
    return ptr['data']
def popLast(aLinkedList):
    if aLinkedList is None:
        return None, None
    if aLinkedList['next'] is None:
        return aLinkedList['data'], None
    if getLength(aLinkedList) == 2:
        v = aLinkedList['next']['data']
        aLinkedList['next'] = None
        return v, aLinkedList
    ptr = aLinkedList
    for i in range(getLength(aLinkedList)-2):
        ptr = ptr['next']
    a = ptr['next']['data']
    ptr['next'] = None
    return a, aLinkedList
def sumSequence(n):
    if n == 0:
        return 0
    return n + sumSequence(n-1)
def binaryToDecimal(w):
    if len(w) == 1:
        return int(w[0])
    d = int(w[0])
    w = w[1:]
    return 2**(len(w)) * d + binaryToDecimal(w)
if __name__ == "__main__":
    linkedList = createList([1, 2, 3, 4, 5])
    print("Linked List:")
    printList(linkedList)
    print("Is 3 in the linked list?", isInList(linkedList, 3))
    print("Is 6 in the linked list?", isInList(linkedList, 6))
    popped_value, linkedList = popFirst(linkedList)
    print("Popped value from the linked list:", popped_value)
    print("Linked List after popping first element:")
    printList(linkedList)
    print("Element at index 2 in the linked list:", getElement(linkedList, 2))
    popped_value, linkedList = popLast(linkedList)
    print("Popped value from the end of the linked list:", popped_value)
    print("Linked List after popping last element:")
    printList(linkedList)
    print("Sum of sequence from 0 to 5:", sumSequence(5))
    binary_number = "1011"
    print("Decimal representation of binary number", binary_number, "is:", binaryToDecimal(binary_number))