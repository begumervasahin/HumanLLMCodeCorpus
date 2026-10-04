from linkedList_CISC121 import createList, printList, getLength
def fonk1(linked_list, value):
    b1 = linked_list
    while b1:
        if b1['data'] == value:
            return True
        b1 = b1['next']
    return False
def fonk2(linked_list):
    if not linked_list:
        return None, None
    b2 = linked_list['data']
    b3 = linked_list['next']
    return b2, b3
def fonk3(linked_list, index):
    if not linked_list or index < 0 or index >= getLength(linked_list):
        return None
    b1 = linked_list
    for _ in range(index):
        b1 = b1['next']
    return b1['data']
def fonk4(linked_list):
    if not linked_list:
        return None, None
    if not linked_list['next']:
        return linked_list['data'], None
    b1 = linked_list
    while b1['next']['next']:
        b1 = b1['next']
    b4 = b1['next']['data']
    b1['next'] = None
    return b4, linked_list
def fonk5(n):
    if n <= 0:
        return 0
    return n + fonk5(n - 1)
def fonk6(binary_string):
    if len(binary_string) == 1:
        return int(binary_string[0])
    b5 = int(binary_string[0])
    b6 = binary_string[1:]
    return (b5 * (2 ** len(b6))) + fonk6(b6)