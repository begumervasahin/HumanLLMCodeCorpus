from linkedList_CISC121 import createList, printList, getLength
def fonk1(b4, value):
    b1 = False
    b2 = b4
    while b2 is not None:
        if b2['data'] == value:
            b1 = True
        b2 = b2['next']
    return b1
def fonk2(b4):
    if b4 is None:
        return None, None
    b3 = b4
    b4 = b4['next']
    return b3['data'], b4
def fonk3(b4, ind):
    if b4 is None or ind >= getLength(b4):
        return None
    b5 = b4
    for i in range(ind):
        b5 = b5['next']
    return b5['data']
def fonk4(b4):
    if b4 is None:
        return None, None
    if b4['next'] is None:
        return b4['data'], None
    if getLength(b4) == 2:
        b6 = b4['next']['data']
        b4['next'] = None
        return b6, b4
    b5 = b4
    for i in range(getLength(b4)-2):
        b5 = b5['next']
    b7 = b5['next']['data']
    b5['next'] = None
    return b7, b4
def fonk5(b8):
    if b8 = = 0:
        return 0
    return b8 + fonk5(b8-1)
def fonk6(b10):
    if len(b10) == 1:
        return int(b10[0])
    b9 = int(b10[0])
    b10 = b10[1:len(b10)]
    return (2**(len(b10)) * b9) + fonk6(b10)