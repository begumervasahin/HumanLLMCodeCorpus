
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def createList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
def printList(aLinkedList):
    current = aLinkedList
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next
def getLength(aLinkedList):
    length = 0
    current = aLinkedList
    while current:
        length += 1
        current = current.next
    return length
def isInList(aLinkedList, value):
    current = aLinkedList
    while current:
        if current.data == value:
            return True
        current = current.next
    return False
def popFirst(aLinkedList):
    if not aLinkedList:
        return None, None
    value = aLinkedList.data
    aLinkedList = aLinkedList.next
    return value, aLinkedList
def getElement(aLinkedList, ind):
    if not aLinkedList or ind >= getLength(aLinkedList):
        return None
    current = aLinkedList
    for _ in range(ind):
        current = current.next
    return current.data
def popLast(aLinkedList):
    if not aLinkedList:
        return None, None
    if not aLinkedList.next:
        return aLinkedList.data, None
    current = aLinkedList
    while current.next.next:
        current = current.next
    value = current.next.data
    current.next = None
    return value, aLinkedList
def sumSequence(n):
    if n == 0:
        return 0
    return n + sumSequence(n - 1)
def binaryToDecimal(binary_str):
    if len(binary_str) == 1:
        return int(binary_str)
    return int(binary_str[0]) * (2 ** (len(binary_str) - 1)) + binaryToDecimal(binary_str[1:])
if __name__ == "__main__":
    linked_list = createList([1, 2, 3, 4, 5])
    print("Original Linked List:")
    printList(linked_list)
    value_to_check = 3
    print(f"\nIs {value_to_check} in the list? {'Yes' if isInList(linked_list, value_to_check) else 'No'}")
    first_value, linked_list = popFirst(linked_list)
    print(f"\nPopped first value: {first_value}")
    print("Linked List after popping the first element:")
    printList(linked_list)
    index = 2
    print(f"\nElement at index {index}: {getElement(linked_list, index)}")
    last_value, linked_list = popLast(linked_list)
    print(f"\nPopped last value: {last_value}")
    print("Linked List after popping the last element:")
    printList(linked_list)
    n = 5
    print(f"\nSum of numbers from {n} to 0: {sumSequence(n)}")
    binary_str = "1101"
    print(f"\nBinary string '{binary_str}' to decimal: {binaryToDecimal(binary_str)}")