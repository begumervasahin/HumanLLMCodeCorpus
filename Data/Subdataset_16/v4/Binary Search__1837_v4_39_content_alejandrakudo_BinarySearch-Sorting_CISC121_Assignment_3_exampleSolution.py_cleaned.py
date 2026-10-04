from linkedList_CISC121 import createList, printList, getLength
def fonk1(linked_list, value):
    b1 = linked_list
    while b1 is not None:
        if b1['data'] == value:
            return True
        b1 = b1['next']
    return False
def fonk2(linked_list):
    if linked_list is None:
        return None, None
    b2 = linked_list['data']
    b3 = linked_list['next']
    return b2, b3
def fonk3(linked_list, index):
    if linked_list is None or index >= getLength(linked_list):
        return None
    b1 = linked_list
    for _ in range(index):
        b1 = b1['next']
    return b1['data']
def fonk4(linked_list):
    if linked_list is None:
        return None, None
    if linked_list['next'] is None:
        return linked_list['data'], None
    if getLength(linked_list) == 2:
        b4 = linked_list['next']['data']
        linked_list['next'] = None
        return b4, linked_list
    b1 = linked_list
    for _ in range(getLength(linked_list) - 2):
        b1 = b1['next']
    b4 = b1['next']['data']
    b1['next'] = None
    return b4, linked_list
def fonk5(b5):
    if b5 = = 0:
        return 0
    return b5 + fonk5(b5 - 1)
def fonk6(binary_string):
    if len(binary_string) == 1:
        return int(binary_string[0])
    b6 = int(binary_string[0])
    b7 = binary_string[1:]
    return (b6 * (2 ** len(b7))) + fonk6(b7)