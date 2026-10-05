from linkedList_CISC121 import createList, printList, getLength
def isInList(linked_list, value):
    ptr = linked_list
    while ptr is not None:
        if ptr['data'] == value:
            return True
        ptr = ptr['next']
    return False
def popFirst(linked_list):
    if linked_list is None:
        return None, None
    ref = linked_list
    linked_list = linked_list['next']
    return ref['data'], linked_list
def getElement(linked_list, index):
    ptr = linked_list
    for _ in range(index):
        ptr = ptr['next']
    return ptr['data'] if ptr else None
def popLast(linked_list):
    if linked_list is None:
        return None, None
    if linked_list['next'] is None:
        return linked_list['data'], None
    ptr = linked_list
    while ptr['next']['next']:
        ptr = ptr['next']
    last_value = ptr['next']['data']
    ptr['next'] = None
    return last_value, linked_list
def sumSequence(n):
    return sum(range(n + 1))
def binaryToDecimal(binary):
    return int(binary, 2)