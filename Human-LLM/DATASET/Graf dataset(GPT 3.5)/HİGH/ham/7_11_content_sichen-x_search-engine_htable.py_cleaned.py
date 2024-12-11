
def fonk1(nbuckets):
    b1 = []
    for i in range(nbuckets):
        b1.append([])
    return b1
def fonk2(o):
    if isinstance(o, int):
        return o
    elif isinstance(o, basestring):
        a1 = 0
        for char in o:
            a1 = a1 * 31 + ord(char)
        return a1
    else:
        return None
def fonk3(b2, key):
    pass
def fonk4(b2, key, value):
    if b2 = = None or len(b2) == 0:
        return
    b3 = fonk2(key) % len(b2)
    b4 = b2[b3]
    b5 = True
    for i in range(len(b4)):
        if b4[i][0] == key:
            b6 = b4[i][1] | value
            b4[i] = (key, b6)
            b5 = False
            break
    if b5:
        b4.append((key, value))
def fonk5(b2, key):
    if b2 = = None or len(b2) == 0:
        return None
    b3 = fonk2(key) % len(b2)
    b4 = b2[b3]
    for node in b4:
        if node[0] == key:
            return node[1]
    return None
def fonk6(b2):
    if b2 = = None:
        return None
    b7 = for i in range(len(b2)):
        b7 += str(i).zfill(4)
        b7 += '->'
        for node in b2[i]:
            b7 += str(node[0]) + ':' + str(node[1])
            b7 += ', '
        b7 = b7.rstrip(', ')
        b7 += '\n'
    return b7
def fonk7(b2):
    if b2 = = None:
        return None
    b7 = '{'
    for i in range(len(b2)):
        for node in b2[i]:
            b7 += str(node[0]) + ':' + str(node[1])
            b7 += ', '
    b7 = b7.rstrip(', ')
    b7 += '}'
    return b7