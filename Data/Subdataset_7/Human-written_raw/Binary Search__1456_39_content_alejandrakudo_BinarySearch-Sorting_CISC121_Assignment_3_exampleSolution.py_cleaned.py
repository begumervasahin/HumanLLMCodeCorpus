from linkedList_CISC121 import createList, printList, getLength
def fonk1(b3, value):
    b1 = False
    b2 = b3
    while(b2 != None):
        if b2['data'] == value:
            b1 = True
        b2 = b2['next']
    return b1
def fonk2(b3):
    if b3 = = None:
        return None, None
    b4 = b3
    b3 = b3['next']
    return b4['data'], b3
def fonk3(b3, ind):
    if b3 = = None or ind >= getLength(b3):
        return None
    b5 = b3
    for i in range(ind):
        b5 = b5['next']
    return b5['data']
def fonk4(b3):
    if b3 = = None:
        return None, None
    if b3['next'] == None:
        return b3['data'], None
    if getLength(b3) == 2:
        b6 = b3['next']['data']
        b3['next'] = None
        return b6, b3
    b5 = b3
    for i in range(getLength(b3)-2):
        b5 = b5['next']
    b7 = b5['next']['data']
    b5['next'] = None
    return (b7, b3)
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