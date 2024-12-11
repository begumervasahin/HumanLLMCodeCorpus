from linkedList_CISC121 import createList, printList, getLength
def fonk1(b3, value):
    b1 = b3
    while b1 is not None:
        if b1['data'] == value:
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
    b1 = b3
    for _ in range(index):
        b1 = b1['next']
    return b1['data'] if b1 else None
def fonk4(b3):
    if b3 is None:
        return None, None
    if b3['next'] is None:
        return b3['data'], None
    b1 = b3
    while b1['next']['next']:
        b1 = b1['next']
    b4 = b1['next']['data']
    b1['next'] = None
    return b4, b3
def fonk5(n):
    return sum(range(n + 1))
def fonk6(binary):
    return int(binary, 2)