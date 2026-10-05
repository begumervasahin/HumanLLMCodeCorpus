
from linkedList_CISC121 import createList, printList, getLength
def isInList(linked_list, value):
    current = linked_list
    while current is not None:
        if current['data'] == value:
            return True
        current = current['next']
    return False
def popFirst(linked_list):
    if linked_list is None:
        return None, None
    first_element = linked_list
    linked_list = linked_list['next']
    return first_element['data'], linked_list
def getElement(linked_list, index):
    if linked_list is None or index >= getLength(linked_list):
        return None
    current = linked_list
    for i in range(index):
        current = current['next']
    return current['data']
def popLast(linked_list):
    if linked_list is None:
        return None, None
    if linked_list['next'] is None:
        return linked_list['data'], None
    if getLength(linked_list) == 2:
        value = linked_list['next']['data']
        linked_list['next'] = None
        return value, linked_list
    current = linked_list
    for i in range(getLength(linked_list)-2):
        current = current['next']
    last_value = current['next']['data']
    current['next'] = None
    return last_value, linked_list
def sumSequence(n):
    if n == 0:
        return 0
    return n + sumSequence(n-1)
def binaryToDecimal(binary_string):
    if len(binary_string) == 1:
        return int(binary_string[0])
    first_digit = int(binary_string[0])
    remaining_digits = binary_string[1:]
    return 2**(len(remaining_digits)) * first_digit + binaryToDecimal(remaining_digits)
if __name__ == "__main__":
    linked_list = createList([1, 2, 3, 4, 5])
    print("Linked List:")
    printList(linked_list)
    print("Is 3 in the linked list?", isInList(linked_list, 3))
    print("Is 6 in the linked list?", isInList(linked_list, 6))
    popped_value, linked_list = popFirst(linked_list)
    print("Popped value from the linked list:", popped_value)
    print("Linked List after popping first element:")
    printList(linked_list)
    print("Element at index 2 in the linked list:", getElement(linked_list, 2))
    popped_value, linked_list = popLast(linked_list)
    print("Popped value from the end of the linked list:", popped_value)
    print("Linked List after popping last element:")
    printList(linked_list)
    print("Sum of sequence from 0 to 5:", sumSequence(5))
    binary_number = "1011"
    print("Decimal representation of binary number", binary_number, "is:", binaryToDecimal(binary_number))