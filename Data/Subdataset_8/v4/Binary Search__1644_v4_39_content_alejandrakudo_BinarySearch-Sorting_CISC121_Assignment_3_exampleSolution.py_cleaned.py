from linkedList_CISC121 import createList, printList, getLength
def isInList(aLinkedList, value):
    found = False
    aPtr = aLinkedList
    while aPtr is not None:
        if aPtr['data'] == value:
            found = True
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
    w = w[1:len(w)]
    return (2**(len(w)) * d) + binaryToDecimal(w)